import streamlit as st

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(page_title="MTE Calculator", layout="centered")

# --------------------------------------------------
# MOBILE STYLE
# --------------------------------------------------
st.markdown("""
    <style>
        .block-container {
            max-width: 420px;
            padding-top: 20px;
            padding-bottom: 30px;
        }
        .main-box {
            border: 3px solid black;
            padding: 20px;
            margin-bottom: 20px;
        }
        .result-box {
            border: 3px solid black;
            padding: 20px;
        }
        div.stButton > button {
            height: 45px;
            font-weight: 600;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;'>MTE CALCULATOR</h1>", unsafe_allow_html=True)

# --------------------------------------------------
# SESSION STATE INIT
# --------------------------------------------------
if "result" not in st.session_state:
    st.session_state.result = None

# --------------------------------------------------
# MAIN SECTION
# --------------------------------------------------
st.markdown('<div class="main-box">', unsafe_allow_html=True)

# KEN + SEARCH
st.markdown("**KEN NO**")
col1, col2 = st.columns([3,1])

with col1:
    ken_no = st.text_input("", key="ken")

with col2:
    search_ken = st.button("SEARCH", use_container_width=True)

# Electrification (dummy auto fill)
if search_ken:
    st.session_state.electrification = "Standard Electrification"

electrification = st.text_input(
    "ELECTRIFICATION",
    value=st.session_state.get("electrification", "")
)

# --------------------------------------------------
# MODULES
# --------------------------------------------------
st.markdown("### MODULES")

modules = ["Module A", "Module B", "Module C", "Module D", "Module E", "Module F"]

selected_modules = st.multiselect(
    "Select Modules",
    modules,
    key="modules"
)

# --------------------------------------------------
# REPLACEMENT ACTIONS
# --------------------------------------------------
replacement_data = {
    "Module A": ["A - Replace Motor", "A - Replace Cable"],
    "Module B": ["B - Replace Board", "B - Replace Fuse"],
    "Module C": ["C - Replace Sensor"],
    "Module D": ["D - Replace Switch"],
    "Module E": ["E - Replace Controller"],
    "Module F": ["F - Replace Wiring"]
}

selected_actions = []

if selected_modules:
    st.markdown("**REPLACEMENT ACTIONS**")

    for module in selected_modules:
        action = st.selectbox(
            f"{module}",
            replacement_data[module],
            key=module
        )
        selected_actions.append(action)

# --------------------------------------------------
# CALCULATE & CLEAR
# --------------------------------------------------
col1, col2 = st.columns(2)

calculate = col1.button("CALCULATE MTE", use_container_width=True)
clear = col2.button("CLEAR", use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

# --------------------------------------------------
# CALCULATION LOGIC (SAMPLE)
# --------------------------------------------------
if calculate:

    preparation_time = len(selected_modules) * 10
    replacement_time = len(selected_actions) * 20
    finalization_time = 15

    total_time = preparation_time + replacement_time + finalization_time
    manpower = max(1, len(selected_modules))
    overall_mte = total_time * manpower

    st.session_state.result = {
        "modules": selected_modules,
        "electrification": electrification,
        "actions": selected_actions,
        "prep": preparation_time,
        "replace": replacement_time,
        "final": finalization_time,
        "manpower": manpower,
        "mte": overall_mte
    }

# --------------------------------------------------
# RESULT SECTION
# --------------------------------------------------
if st.session_state.result:

    data = st.session_state.result

    st.markdown('<div class="result-box">', unsafe_allow_html=True)

    st.subheader("RESULT")

    st.write("Selected Modules:", data["modules"])
    st.write("Electrification:", data["electrification"])
    st.write("Replacement Action(s):", data["actions"])

    with st.expander("Time Details"):
        st.write("Preparation Time:", data["prep"], "mins")
        st.write("Replacement Time:", data["replace"], "mins")
        st.write("Finalization Time:", data["final"], "mins")

    st.write("Manpower Required:", data["manpower"])
    st.write("Overall MTE:", data["mte"])

    st.markdown('</div>', unsafe_allow_html=True)

# --------------------------------------------------
# CLEAR FUNCTION
# --------------------------------------------------
if clear:
    st.session_state.clear()
    st.rerun()
