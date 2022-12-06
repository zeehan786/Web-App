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




rad = st.sidebar.radio("Navigation", ["Home", "Data Visualization", "Our Data", "About Us"])

if rad == "Home":
    st.header("Welcome to our Airline Data Visualization Homepage! 👋")
    st.image('images/q2.png')
    st.subheader("For our project we will be using a dataset that is derived from the Bureau of Transportation Statistics that tracks airplane flights in the United States from 2019, 2020, 2021, and 2022. We will be visualizing how flights have changed throughout these years, the activities of domestic flights throughout the USA, and the effect of covid 19 on air travel.")

elif rad == "Data Visualization":
    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Visualization 1", "Visualization 2", "Visualization 3",
                                                         "Visualization 4", "Visualization 5", "Visualization 6", "Visualization 7"])
    
    with tab1:
        st.header("Domestic Airlines trend during covid-19")
        st.image('images/V1_4.png', width=210)
        st.image('images/V1-Price.png')        
        st.image('images/V1-Miles.png')
    
    with tab2:
        st.header("Factors that plays a crucial role in airline tickets")
        st.image('images/V2-Bar.png')
        st.image('images/V2-Pie.png')

    with tab3:
        st.header("Which state has the highest count of flight departures/arrivals?")
        HtmlFile = open("images/V3-Map.html", 'r', encoding='utf-8')
        source_code = HtmlFile.read() 
        # print(source_code)
        components.html(source_code, height = 450)
        
    
    with tab4:
        st.header("Ideal time to book a fare?")
        st.image('images/V1_4.png', width=210)
        st.image('images/V4-Ideal_time.png')        
    
    with tab5:
        st.header("Which airline company has the highest fare ticket price?")
        st.image('images/V5_6.png', width=810)
        st.image('images/V5-Airline_price.png')
        
    
    with tab6:
        st.header("America's Favorite Airline")
        st.image('images/V5_6.png', width=810)
        st.image('images/V6-AmericaFav.png')
        
    
    with tab7:
        st.header("Which state has the highest airline miles? (Destination/Arrival)")
        HtmlFile2 = open("images/V7-Arr.html", 'r', encoding='utf-8')
        source_code2 = HtmlFile2.read()
        components.html(source_code2, height = 450)

        HtmlFile3 = open("images/V7-Dep.html", 'r', encoding='utf-8')
        source_code3 = HtmlFile3.read()
        components.html(source_code3, height = 450)

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

elif rad == "Our Data":
    st.header("Data")
    st.image('images/Our_Data_df.png')
    st.subheader("Our data holds values for domestic airline flights in the US from 2019 to 2022. The data was collected from the bureau of transportation statistics. We have about 30 million records of flight travels. Each record has unique attributes which are year and quarter. These variables help give us an insight on the time people booked their flights. ")
    st.write('<a href="https://www.transtats.bts.gov/">Data Source</a>', unsafe_allow_html=True)
    st.image('images/Our_Data_table.png')
    st.subheader("There are a lot of different variables that go into air travel. With these variables, we were able to determine which one has the most significant impact on the price of an airplane ticket. Were also able to use these variables to check air travel activities throughout the years from 2019-2022. They will also help us identify the trends caused by covid 19. ")
    st.subheader("Because of this dataset, we are able to ask so many questions and get answers in return. Feel free to explore these questions.")

