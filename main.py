# importing required dependencies
import streamlit as st
from landing_page import show_landing_page
from startup_generator_page import show_startup_generator_page

# setting page title and layout
st.set_page_config(page_title="Startup Idea Generator", layout="centered")

# elements in sidebar 
page = st.sidebar.radio("Navigation", ("Home", "Generate Startup Idea"))

# ensuring only landing page or startup page to show
if page == "Home":
    show_landing_page()
elif page == "Generate Startup Idea":
    show_startup_generator_page()
