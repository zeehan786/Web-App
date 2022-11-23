import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

# Create a page header
st.header("Welcome to the homepage! 👋")

st.write('<a href="/Titanic">Interact with my ML algorithm.</a>', unsafe_allow_html=True)