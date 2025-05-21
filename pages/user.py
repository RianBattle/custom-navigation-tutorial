import streamlit as st
from menu import menu_with_redirect

# Redirect to app.py if not logged in
menu_with_redirect()

st.title("This page is available to all users")
st.markdown(f"You are currently logged in with the role of {st.session_state.role}")
