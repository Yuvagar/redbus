
import pandas as pd
import streamlit as st
import mysql.connector as db
from streamlit_option_menu import option_menu
from datetime import datetime
import time 

st.set_page_config(
    page_title="redbus.in",
    page_icon=":metro:",
    layout="wide",
    initial_sidebar_state="expanded"
)


connection = db.connect(
    host="localhost",
    user="root",
    password="Yuva@4435",
    database="redbus"
)
curr = connection.cursor()

curr.execute("SELECT * FROM detail")
data = curr.fetchall()
column_names = [desc[0] for desc in curr.description]
df = pd.DataFrame(data, columns=column_names)

st.sidebar.image('heder.png', width=150)
with st.sidebar:
    st.markdown("# redBus")
    menu = option_menu (
        menu_title="Just click",  
        options=["Bus selection","States"],
        styles={"nav-link-selected": {"background-color": "red"}}
        
    )
    st.image("busi.png", width=350)



if menu == 'States':
    st.header("States")
    
    for i in df['States'].unique():
        st.write(i)

    st.image("rb.jpg")

if menu == 'Bus selection':
    st.header('Bus Routes')
    
    c1, c2, c3= st.columns(3)
    
    with c1:
        
        select_routes = st.selectbox("Select Bus Route", df['Bus_route'].unique())
 

    with c2:
        select_type = st.selectbox("Select Bus Type", ['Sleeper', 'Seater', 'All'])
        if select_type == 'Sleeper':
            filtered_data = df[df['Bus_type'].str.contains('Sleeper', case=False, na=False)]
        elif select_type == 'Seater':
            filtered_data = df[df['Bus_type'].str.contains('Seater|PUSH BACK', case=False, na=False, regex=True)]
        elif select_type == 'All':
            filtered_data = df
    
    with c3:
        select_price = st.select_slider("Select the Price", ['0-500', '500-1000', '1000+'])
        if select_price == '0-500':
            filtered_data = filtered_data[(filtered_data['Price'] >= 0) &(filtered_data['Price'] <=500)]
            
        elif select_price == '500-1000':
            filtered_data = filtered_data[(filtered_data['Price'] > 500) & (filtered_data['Price'] <= 1000)]
            
        elif select_price == '1000+':
            filtered_data = filtered_data[(filtered_data['Price'] > 1000)]
            
    
    

    c4, c5 = st.columns(2)
    
    with c4:
        select_rating = st.selectbox("Ratings", ['0-3', '3-4', '4-5', 'All'])
        if select_rating == '0-3':
            filtered_data = filtered_data[(filtered_data['star_rating'] >= 0) & (filtered_data['star_rating'] <= 3)]
        elif select_rating == '3-4':
            filtered_data = filtered_data[(filtered_data['star_rating'] > 3) & (filtered_data['star_rating'] <= 4)]
        elif select_rating == '4-5':
            filtered_data = filtered_data[(filtered_data['star_rating'] >= 4) & (filtered_data['star_rating'] <= 5)]
        elif select_rating == 'All':
            filtered_data = filtered_data
    
    with c5:
        Ac_type = st.radio("A/C Type", ['A/C', 'NON A/C', 'ALL'])
        if Ac_type == 'A/C':
            filtered_data = filtered_data[filtered_data['Bus_type'].apply(lambda x: ("A/C" in x or "A.C" in x) and not ("NON A/C" in x or "NON A/C" in x))]
        elif Ac_type == 'NON A/C':
            filtered_data = filtered_data[filtered_data['Bus_type'].apply(lambda x: "NON A/C" in x or "NON A/C" in x)]
        elif Ac_type == 'ALL':
            filtered_data = filtered_data
    
    filtered_data = filtered_data[filtered_data['Bus_route'] == select_routes]
    
    
    if filtered_data.empty:
        st.write("No buses matchs")
    else:
        st.write(filtered_data[['Bus_route', 'Bus_name', 'Bus_type','Duration', 'Price', 'star_rating', 'Seat_availability']])

    



