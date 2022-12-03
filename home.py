import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

# st.markdown("""
#                 # zeehan #
#                 ## uzma ##
#                 ### zara ###
#                 Streamlit is **_really_ cool**.
#                 _isnt it_ <br>
#                 :moon: <br>


# """, True)

# df = pd.read_csv('data/iris.csv')
# select_condition = df['sepal_width'] < 20
# df = df[select_condition]


# fig, ax = plt.subplots()
# ax.scatter(df['petal_length'], df['petal_width'])
# plt.title("Flower information")
# st.pyplot(fig)

# st.map()




rad = st.sidebar.radio("Navigation", ["Home", "Data Visualization", "About Us"])

if rad == "Home":
    st.header("Welcome to our Afirline Data Visualization Homepage! 👋")

elif rad == "Data Visualization":
    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Visualization 1", "Visualization 2", "Visualization 3",
                                                         "Visualization 4", "Visualization 5", "Visualization 6", "Visualization 7"])
    
    with tab1:
        st.header("Domestic Airlines trend during covid-19")
        st.write("Work in Progress, please come back later")
    
    with tab2:
        st.header("Factors that plays a crucial role in airline tickets")
        st.write("Work in Progress, please come back later")

    with tab3:
        st.header("Which state has the highest count of flight departures/arrivals?")
        st.image('images/q2.png')
        st.write("Work in Progress, please come back later")
    
    with tab4:
        st.header("Ideal time to book a fare?")
        st.write("Work in Progress, please come back later")
    
    with tab5:
        st.header("Which airline company has the highest fare ticket price?")
        st.write("Work in Progress, please come back later")
    
    with tab6:
        st.header("How airline price has changed throughout the years?")
        st.write("Work in Progress, please come back later")
    
    with tab7:
        st.header("America's favorite airline")
        st.write("Work in Progress, please come back later")
    

elif rad == "About Us":
    st.header("About Us")