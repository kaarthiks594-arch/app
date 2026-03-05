import streamlit as st

st.set_page_config(page_title="MTE Calculator", layout="centered")

# -----------------------------
# FIGMA STYLE CSS
# -----------------------------
st.markdown("""
<style>

.block-container{
    max-width:420px;
}

.title{
    text-align:center;
    font-size:28px;
    font-weight:bold;
    margin-bottom:20px;
}

.main-box{
    border:3px solid black;
    padding:20px;
    margin-bottom:20px;
}

.result-box{
    border:3px solid black;
    padding:20px;
}

label{
    font-weight:600;
}

div.stButton > button{
    height:40px;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# SESSION STATE
# -----------------------------
if "ken" not in st.session_state:
    st.session_state.ken=""

if "modules" not in st.session_state:
    st.session_state.modules=[]

if "actions" not in st.session_state:
    st.session_state.actions=[]

if "result" not in st.session_state:
    st.session_state.result=False

# -----------------------------
# TITLE
# -----------------------------
st.markdown('<div class="title">MTE CALCULATOR</div>',unsafe_allow_html=True)

# -----------------------------
# MAIN UI BOX
# -----------------------------
st.markdown('<div class="main-box">',unsafe_allow_html=True)

# KEN NUMBER
st.write("Ken number")

c1,c2 = st.columns([3,1])

with c1:
    ken_input = st.text_input("", value=st.session_state.ken)

with c2:
    search = st.button("search", key="search1")

if search:
    st.session_state.ken = ken_input

# ELECTRIFICATION
st.write("Electrification")

st.text_input("", value="LCE", disabled=True)

# MODULES
st.write("modules")

col1,col2,col3 = st.columns(3)

with col1:
    m1 = st.checkbox("module 1")

with col2:
    m2 = st.checkbox("module 2")

with col3:
    m3 = st.checkbox("module 3")

col4,col5,col6 = st.columns(3)

with col4:
    m4 = st.checkbox("module 4")

with col5:
    m5 = st.checkbox("module 5")

with col6:
    m6 = st.checkbox("module 6")

# REPLACEMENT ACTIONS
st.write("Replacement actions")

c1,c2 = st.columns([3,1])

with c1:
    action = st.selectbox("",[
        "Select Action",
        "Action 1",
        "Action 2",
        "Action 3"
    ])

with c2:
    add = st.button("search", key="search2")

if add and action!="Select Action":
    if action not in st.session_state.actions:
        st.session_state.actions.append(action)

# SELECTED ACTIONS
st.write("selected replacement actions")

st.text_area("", value="\n".join(st.session_state.actions), height=120)

# BUTTONS
b1,b2 = st.columns(2)

with b1:
    calc = st.button("calculate mte")

with b2:
    clear = st.button("clear")

if clear:
    st.session_state.clear()
    st.rerun()

if calc:
    st.session_state.result=True

st.markdown('</div>',unsafe_allow_html=True)

# -----------------------------
# RESULT BOX
# -----------------------------
if st.session_state.result:

    st.markdown('<div class="result-box">',unsafe_allow_html=True)

    st.write("result")

    st.write("ken no")
    st.write(st.session_state.ken)

    st.write("modules")

    st.write("replacement action")

    st.write("time")

    st.write("1) preparation")

    st.write("2) replacement")

    st.write("3) finalisation")

    st.write("overall mte")

    st.markdown('</div>',unsafe_allow_html=True)
