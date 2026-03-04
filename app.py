import streamlit as st

# -------------------------
# Page Configuration
# -------------------------
st.set_page_config(
    page_title="MTE Calculator",
    layout="centered"
)

# -------------------------
# Mobile Width Styling
# -------------------------
st.markdown("""
    <style>
        .block-container {
            max-width: 420px;
            padding-top: 1rem;
            padding-bottom: 2rem;
        }
        div.stButton > button {
            border-radius: 8px;
            height: 45px;
            font-weight: 600;
        }
        .section-card {
            padding: 15px;
            border-radius: 10px;
            background-color: #f7f7f7;
            margin-bottom: 15px;
        }
    </style>
""", unsafe_allow_html=True)

st.title("MTE Calculator")

# -------------------------
# KEN Section
# -------------------------
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.subheader("KEN Search")

ken_number = st.text_input("Enter KEN Number")

st.button("Search", use_container_width=True)

st.markdown("### Electrification Details")
st.info("Electrification details will appear here.")

st.markdown('</div>', unsafe_allow_html=True)

# -------------------------
# Module Selection
# -------------------------
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.subheader("Module Selection")

modules = ["Module A", "Module B", "Module C", "Module D"]
selected_modules = st.multiselect(
    "Select Modules",
    modules
)

st.markdown('</div>', unsafe_allow_html=True)

# -------------------------
# Replacement Actions
# -------------------------
if selected_modules:
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.subheader("Replacement Actions")

    replacement_actions = {
        "Module A": ["Action A1", "Action A2"],
        "Module B": ["Action B1", "Action B2"],
        "Module C": ["Action C1", "Action C2"],
        "Module D": ["Action D1", "Action D2"],
    }

    selected_actions = []

    for module in selected_modules:
        st.markdown(f"**{module}**")
        action = st.selectbox(
            f"Select Replacement Action for {module}",
            replacement_actions[module],
            key=module
        )
        selected_actions.append(action)

    st.button("Search", use_container_width=True)

    st.markdown("### Selected Replacement Actions")
    st.write(selected_actions)

    st.markdown('</div>', unsafe_allow_html=True)

# -------------------------
# MTE Section
# -------------------------
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.subheader("MTE Calculation")

calculate = st.button("Calculate MTE", use_container_width=True)
clear = st.button("Clear", use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

# -------------------------
# Result Section
# -------------------------
if calculate:
    st.markdown("## Result")

    st.write("**Selected Modules:**", selected_modules)
    st.write("**Selected Replacement Actions:**", selected_actions if selected_modules else [])

    st.write("**Manpower:** Placeholder")
    st.write("**Overall MTE:** Placeholder")

    with st.expander("View Time Breakdown"):
        st.write("Preparation Time: Placeholder")
        st.write("Replacement Time: Placeholder")
        st.write("Finalization Time: Placeholder")

if clear:
    st.experimental_rerun()
