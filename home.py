import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

# Create a page header
st.header("Welcome to my homepage! 👋")

st.write('<a href="/titanic">Interact with my ML algorithm.</a>', unsafe_allow_html=True)