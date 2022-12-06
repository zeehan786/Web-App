import streamlit as st
import streamlit.components.v1 as components
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
    st.header("Welcome to our Airline Data Visualization Homepage! 👋")

elif rad == "Data Visualization":
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Visualization 1", "Visualization 2", "Visualization 3",
                                                         "Visualization 4", "Visualization 5", "Visualization 6"])
    
    with tab1:
        st.header("Domestic Airlines trend during covid-19")
        st.image('images/V1-Price.png')
        
        st.image('images/V1-Miles.png')
    
    with tab2:
        st.header("Factors that plays a crucial role in airline tickets")
        st.image('images/V2-Bar.png')
        st.image('images/V2-Pie.png')

    with tab3:
        st.header("Which state has the highest market fare?")
        HtmlFile = open("images/V3-Map.html", 'r', encoding='utf-8')
        source_code = HtmlFile.read() 
        # print(source_code)
        components.html(source_code, height = 450)
        
    
    with tab4:
        st.header("Ideal time to book a fare?")
        st.image('images/V4-Ideal_time.png')
    
    with tab5:
        st.header("Which airline company has the highest fare ticket price?")
        st.image('images/V5-Airline_price.png')
    
    with tab6:
        st.header("America's Favorite Airline")
        st.image('images/V6-AmericaFav.png')
    
elif rad == "About Us":
    st.header("About Us")

    col1, col2, col3 = st.columns([1,1,1])

    with col1:
        st.image('images/Hamza.jfif')
        st.write("Junior at Brooklyn College")
        st.write("Computer Science Major")
        st.write('<a href="https://www.linkedin.com/in/hamza-khalil-a7a784210">Linkedin</a>', unsafe_allow_html=True)
    
    with col2:
        st.image('images/Sameer.jfif')
        st.write("Senior at Lehman's College")
        st.write("Computer Science Major")
        st.write('<a href="https://www.linkedin.com/in/mohammed-sameer-uddin/">Linkedin</a>', unsafe_allow_html=True)

    with col3:
        st.image('images/Zeehan.jfif')
        st.write("Senior at Queens College")
        st.write("Computer Science Major")
        st.write('<a href="https://www.linkedin.com/in/zeehan-rahman">Linkedin</a>', unsafe_allow_html=True)
