import streamlit as st

st.set_page_config(page_title="MTE Calculator", layout="wide")

# -----------------------------
# MOCK DATA (Converted from React)
# -----------------------------

MODULES = [
    {"id": "mod-1", "name": "Transformer Module"},
    {"id": "mod-2", "name": "Circuit Breaker Module"},
    {"id": "mod-3", "name": "Metering Module"},
    {"id": "mod-4", "name": "Cable Module"},
    {"id": "mod-5", "name": "Switchgear Module"},
    {"id": "mod-6", "name": "Earthing Module"},
]

REPLACEMENT_ACTIONS = [
    {"id": "act-1", "name": "Replace Primary Winding", "module": "mod-1", "prep": 2, "rep": 8, "fin": 2, "man": 4},
    {"id": "act-2", "name": "Replace Circuit Breaker Unit", "module": "mod-2", "prep": 1, "rep": 4, "fin": 1, "man": 2},
    {"id": "act-3", "name": "Install Smart Meter", "module": "mod-3", "prep": 0.5, "rep": 1.5, "fin": 0.5, "man": 1},
    {"id": "act-4", "name": "Underground Cable Replacement", "module": "mod-4", "prep": 3, "rep": 12, "fin": 3, "man": 5},
]

# -----------------------------
# SESSION STATE INIT
# -----------------------------

if "ken" not in st.session_state:
    st.session_state.ken = None

if "modules" not in st.session_state:
    st.session_state.modules = []

if "actions" not in st.session_state:
    st.session_state.actions = []

if "show_results" not in st.session_state:
    st.session_state.show_results = False

# -----------------------------
# HEADER
# -----------------------------

st.title("MTE CALCULATOR")

# -----------------------------
# STEP 1: KEN SEARCH
# -----------------------------

if not st.session_state.ken:
    ken_input = st.text_input("Enter KEN Number")

    if st.button("Search"):
        if ken_input:
            st.session_state.ken = ken_input
            st.rerun()
        else:
            st.error("Please enter KEN Number")

# -----------------------------
# MAIN FLOW
# -----------------------------

if st.session_state.ken and not st.session_state.show_results:

    st.success(f"KEN Found: {st.session_state.ken}")

    st.subheader("Electrification Type")
    electrification_type = st.radio("Select Type", ["LCE"], horizontal=True)

    st.subheader("Select Modules")

    selected_modules = []
    for module in MODULES:
        if st.checkbox(module["name"], key=module["id"]):
            selected_modules.append(module["id"])

    st.session_state.modules = selected_modules

    if selected_modules:
        st.subheader("Replacement Actions")

        available_actions = [
            action for action in REPLACEMENT_ACTIONS
            if action["module"] in selected_modules
        ]

        selected_actions = []
        for action in available_actions:
            if st.checkbox(action["name"], key=action["id"]):
                selected_actions.append(action["id"])

        st.session_state.actions = selected_actions

    if st.session_state.modules and st.session_state.actions:
        if st.button("Calculate MTE"):
            st.session_state.show_results = True
            st.rerun()

# -----------------------------
# RESULTS
# -----------------------------

if st.session_state.show_results:

    st.header("MTE Results")

    st.write("### KEN Number")
    st.write(st.session_state.ken)

    total_time = 0
    total_mte = 0

    st.write("### Selected Actions")

    for action in REPLACEMENT_ACTIONS:
        if action["id"] in st.session_state.actions:

            time = action["prep"] + action["rep"] + action["fin"]
            mte = time * action["man"]

            total_time += time
            total_mte += mte

            with st.expander(action["name"]):
                st.write(f"Preparation: {action['prep']} h")
                st.write(f"Replacement: {action['rep']} h")
                st.write(f"Finalization: {action['fin']} h")
                st.write(f"Manpower: {action['man']}")
                st.write(f"Total Time: {time} h")
                st.write(f"MTE: {mte} man-hours")

    st.divider()
    st.subheader(f"Total Time: {total_time:.1f} hours")
    st.subheader(f"Overall MTE: {total_mte:.1f} man-hours")

    if st.button("New Calculation"):
        st.session_state.clear()
        st.rerun()
