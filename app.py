import streamlit as st

st.set_page_config(page_title="MTE Calculator", layout="centered")

# -----------------------------
# MOBILE STYLE
# -----------------------------
st.markdown("""
<style>

.block-container{
    max-width:420px;
    padding-top:20px;
}

.container-box{
    border:2px solid black;
    padding:20px;
    margin-bottom:20px;
}

.result-box{
    border:2px solid black;
    padding:20px;
}

.module-btn{
    border:1px solid black;
    padding:10px;
    text-align:center;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# TITLE
# -----------------------------
st.markdown("<h2 style='text-align:center;'>MTE CALCULATOR</h2>", unsafe_allow_html=True)

# -----------------------------
# MAIN BOX
# -----------------------------
st.markdown('<div class="container-box">', unsafe_allow_html=True)

# KEN NUMBER
st.write("Ken number")

col1, col2 = st.columns([3,1])

with col1:
    ken = st.text_input("", placeholder="Enter KEN number")

with col2:
    st.button("search", key="search1")

# ELECTRIFICATION
st.write("Electrification")

st.text_input("", placeholder="Electrification type")

# MODULES
st.write("modules")

c1,c2,c3 = st.columns(3)

with c1:
    st.checkbox("", key="m1")

with c2:
    st.checkbox("", key="m2")

with c3:
    st.checkbox("", key="m3")

c4,c5,c6 = st.columns(3)

with c4:
    st.checkbox("", key="m4")

with c5:
    st.checkbox("", key="m5")

with c6:
    st.checkbox("", key="m6")

# REPLACEMENT ACTIONS
st.write("Replacement actions")

col1, col2 = st.columns([4,1])

with col1:
    st.selectbox("",[
        "Select replacement action",
        "Action 1",
        "Action 2",
        "Action 3"
    ])

with col2:
    st.button("▼", key="dropdown")

# SELECTED ACTIONS
st.write("selected replacements actions")

st.text_area("", height=130)

# BUTTONS
col1, col2 = st.columns(2)

with col1:
    st.button("calculate mte", key="calc")

with col2:
    st.button("clear", key="clear")

st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# RESULT SECTION
# -----------------------------
st.markdown('<div class="result-box">', unsafe_allow_html=True)

st.write("result")

st.write("ken no")

st.write("modules")

st.write("replacement action")

st.write("time")

st.write("1) preparation")

st.write("2) replacement")

st.write("3) finalisation")

st.write("overall mte")

st.markdown('</div>', unsafe_allow_html=True)
