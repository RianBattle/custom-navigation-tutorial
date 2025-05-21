import streamlit as st
from menu import menu

# Initialize st.session_state.role to None
if "role" not in st.session_state:
    st.session_state.role = None

# Retrieve the role from session state to initialize the widget
st.session_state._role = st.session_state.role

def set_role():
    # Callback function to save the role selection
    st.session_state.role = st.session_state._role

# Selectbox to choose role
st.selectbox(
    "Select your role:",
    [None, "user", "admin", "super-admin"],
    key="_role",
    on_change=set_role
)
menu() # Show the dynamic menu

tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])
