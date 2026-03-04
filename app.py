import streamlit as st

st.set_page_config(page_title="MTE Calculator UI", layout="wide")

st.title("MTE Calculation Application")

# -------------------------------
# KEN Search Section
# -------------------------------

st.subheader("KEN Search")

col1, col2 = st.columns([3, 1])

with col1:
    ken_number = st.text_input("Enter KEN Number")

with col2:
    search_ken = st.button("Search")

# Placeholder Electrification Details
st.markdown("### Electrification Details")
st.info("Electrification details will appear here (UI placeholder).")

# -------------------------------
# Module Selection Section
# -------------------------------

st.subheader("Module Selection")

modules = ["Module A", "Module B", "Module C", "Module D"]
selected_modules = st.multiselect(
    "Select One or More Modules",
    modules
)

# -------------------------------
# Replacement Action Section
# -------------------------------

if selected_modules:
    st.subheader("Replacement Actions")

    replacement_actions = {
        "Module A": ["Action A1", "Action A2"],
        "Module B": ["Action B1", "Action B2"],
        "Module C": ["Action C1", "Action C2"],
        "Module D": ["Action D1", "Action D2"],
    }

    selected_actions = []

    for module in selected_modules:
        st.markdown(f"**{module} Replacement Actions**")

        col1, col2 = st.columns([4, 1])

        with col1:
            action = st.selectbox(
                f"Select Replacement Action for {module}",
                replacement_actions[module],
                key=module
            )

        with col2:
            st.button("Search", key=f"search_{module}")

        selected_actions.append(action)

# Display Selected Replacement Actions
if selected_modules:
    st.markdown("### Selected Replacement Actions")
    st.write(selected_actions)

# -------------------------------
# MTE Calculation Section
# -------------------------------

st.subheader("MTE Calculation")

calculate = st.button("Calculate MTE")
clear = st.button("Clear")

# -------------------------------
# Result Section (UI Placeholder)
# -------------------------------

if calculate:
    st.markdown("## Result (UI Preview)")

    st.write("**Selected Modules:**", selected_modules)
    st.write("**Selected Replacement Actions:**", selected_actions if selected_modules else [])

    st.write("**Manpower:** Placeholder")
    st.write("**Overall MTE:** Placeholder")

    # Time Popup Simulation
    with st.expander("View Time Breakdown"):
        st.write("Preparation Time: Placeholder")
        st.write("Replacement Time: Placeholder")
        st.write("Finalization Time: Placeholder")

if clear:
    st.experimental_rerun()
