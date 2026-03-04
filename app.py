import streamlit as st

st.set_page_config(page_title="MTE Calculator", layout="centered")

# -----------------------------
# Mobile Layout Styling
# -----------------------------
st.markdown("""
    <style>
        .block-container {
            max-width: 500px;
            padding-top: 20px;
            padding-bottom: 40px;
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

# -----------------------------
# MAIN INPUT SECTION
# -----------------------------
st.markdown('<div class="main-box">', unsafe_allow_html=True)

# KEN NO + SEARCH
st.markdown("**KEN NO**")
col1, col2 = st.columns([3,1])

with col1:
    st.text_input("", placeholder="Enter KEN Number", label_visibility="collapsed")

with col2:
    st.button("SEARCH", use_container_width=True)

# ELECTRIFICATION
st.markdown("**ELECTRIFICATION**")
st.text_input("", placeholder="Electrification Type", label_visibility="collapsed")

# MODULES
st.markdown("### MODULES")

col1, col2, col3 = st.columns(3)
col1.button("Transformer Module")
col2.button("Circuit Breaker Module")
col3.button("Metering Module")

col4, col5, col6 = st.columns(3)
col4.button("Cable Module")
col5.button("Switchgear Module")
col6.button("Earthing Module")

# REPLACEMENT ACTIONS
st.markdown("**REPLACEMENT ACTIONS**")
col1, col2 = st.columns([3,1])

with col1:
    st.selectbox(
        "",
        ["Select Replacement Action"],
        label_visibility="collapsed"
    )

with col2:
    st.button("SEARCH", use_container_width=True)

# CALCULATE + CLEAR
st.markdown("<br>", unsafe_allow_html=True)
col1, col2 = st.columns(2)

col1.button("CALCULATE MTE", use_container_width=True)
col2.button("CLEAR", use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# RESULT SECTION (UI ONLY)
# -----------------------------
st.markdown('<div class="result-box">', unsafe_allow_html=True)

st.subheader("RESULT")

st.write("Selected Modules:")
st.write("Electrification:")
st.write("Replacement Action(s):")

st.write("Time:")
st.write("1) Preparation time")
st.write("2) Replacement time")
st.write("3) Finalization time")

st.write("Manpower:")
st.write("Overall MTE:")

st.markdown('</div>', unsafe_allow_html=True)
