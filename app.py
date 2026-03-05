import streamlit as st

st.set_page_config(page_title="MTE Calculator", layout="centered")

# ---------- SESSION STATE ----------
if "page" not in st.session_state:
    st.session_state.page = "search"

if "ken_number" not in st.session_state:
    st.session_state.ken_number = ""

if "electrification" not in st.session_state:
    st.session_state.electrification = None

if "selected_modules" not in st.session_state:
    st.session_state.selected_modules = []

if "selected_actions" not in st.session_state:
    st.session_state.selected_actions = []

if "results" not in st.session_state:
    st.session_state.results = {}

# ---------- MODULE LIST ----------
MODULES = [f"Module {i}" for i in range(1,13)]

REPLACEMENT_ACTIONS = [
    "Replace Component A",
    "Replace Component B",
    "Replace Component C",
    "Repair Module",
    "Upgrade System",
    "Install New Part",
    "Remove Old Part",
    "Test and Verify",
]

# ---------- HEADER ----------
st.markdown(
"""
<div style='background:#2563eb;padding:15px;border-radius:10px'>
<h2 style='color:white;text-align:center'>MTE Calculator</h2>
</div>
""",
unsafe_allow_html=True
)

st.write("")

# ---------- PAGE 1 ----------
if st.session_state.page == "search":

    st.subheader("KEN Search")

    ken = st.text_input("Enter KEN Number")

    if st.button("Search"):

        if ken.strip() == "":
            st.error("Please enter a KEN number")
        else:
            st.session_state.ken_number = ken
            st.session_state.electrification = f"AC 25kV | Zone: Central | Section: {ken}"
            st.session_state.page = "details"
            st.rerun()

# ---------- PAGE 2 ----------
else:

    st.subheader("Electrification")
    st.info(st.session_state.electrification)

    # ---------- MODULE GRID ----------
    st.subheader("Modules")

    cols = st.columns(3)

    for i,module in enumerate(MODULES):

        col = cols[i%3]
        selected = module in st.session_state.selected_modules

        if col.button(module, key=module, use_container_width=True):

            if selected:
                st.session_state.selected_modules.remove(module)
            else:
                st.session_state.selected_modules.append(module)

    st.write(f"Selected Modules: {len(st.session_state.selected_modules)}")

    # ---------- REPLACEMENT ACTIONS (UPDATED) ----------
    st.subheader("Replacement Actions")

    if len(st.session_state.selected_modules) == 0:
        st.warning("Select modules first")

    else:

        options = []

        for m in st.session_state.selected_modules:
            for a in REPLACEMENT_ACTIONS:
                options.append(f"{a} - {m}")

        # LIKE VARIANTS
        st.session_state.selected_actions = st.multiselect(
            "Actions",
            options,
            default=st.session_state.selected_actions
        )

    st.write("---")

    # ---------- BUTTONS ----------
    col1,col2 = st.columns(2)

    if col1.button("Calculate MTE"):

        if len(st.session_state.selected_modules)==0:
            st.error("Select at least one module")

        elif len(st.session_state.selected_actions)==0:
            st.error("Select at least one action")

        else:

            st.session_state.results = {
                "time":"4.5 hours",
                "manpower":"3 persons",
                "overall":"13.5 hours",
                "prep":"1 hour",
                "replace":"2.5 hours",
                "final":"1 hour"
            }

            st.success("MTE Calculated")

    if col2.button("Clear"):

        st.session_state.page="search"
        st.session_state.ken_number=""
        st.session_state.electrification=None
        st.session_state.selected_modules=[]
        st.session_state.selected_actions=[]
        st.session_state.results={}

        st.rerun()

    # ---------- RESULTS ----------
    if st.session_state.results:

        st.write("---")
        st.subheader("Result")

        st.write("KEN Number")
        st.text(st.session_state.ken_number)

        st.write("Electrification")
        st.text(st.session_state.electrification)

        st.write("Selected Replacement Actions")

        for a in st.session_state.selected_actions:
            st.write("-",a)

        st.write("Time")

        col1,col2 = st.columns([4,1])

        col1.text(st.session_state.results["time"])

        if col2.button("Details"):

            st.info(
f"""
Preparation : {st.session_state.results['prep']}

Replacement : {st.session_state.results['replace']}

Finalisation : {st.session_state.results['final']}
"""
            )

        st.write("Man Power")
        st.text(st.session_state.results["manpower"])

        st.write("Overall MTE")

        st.success(st.session_state.results["overall"])
