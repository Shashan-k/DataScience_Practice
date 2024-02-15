"""
### Streamlit - A library used to make  web apps in Python. 
- Can be used to make interactive dashboards and visualizations/websites with just a few lines of code.
- Streamlit is using  React, an open-source JavaScript library for building user interfaces, as its main toolkit. And python as the backend
- Flask vs Streamlit -  Flask is more flexible, but requires manual server management whereas Streamlit handles the backend for you.
- But the disadvantage of streamlit is limited customizations
"""

import streamlit as st
import pandas as pd
import time

# To run - streamlit run app.py

################# Text Based Utility #################
# Title
st.title('Startup Dashboard')

# Header/Subheader
st.header('This is a header')
st.subheader('This is a subheader')

# Write Function
st.write('This is a normal text')

# Markdown
st.markdown("""
### My favourite sports
- Cricket
- Football
- Badminton           
            
            """)

# Code display
st.code("""
def square(intput):
    return input*input
    
x = square(5)
        """)

# LaTex
st.latex('x^2 + y^2 = z^2')

##### Display Elements ######
df = pd.DataFrame({
    'name': ['Ankit', 'Raj', 'Rahul'],
    'Age': [34, 19, 60],
    'package': [12, 14, 15]
})
st.dataframe(df)

st.metric(label='Total Revenue', value='$1000', delta='$100')

st.json({
    'name': ['Ankit', 'Raj', 'Rahul'],
    'Age': [34, 19, 60],
    'package': [12, 14, 15]
})

## Displaying Media ##

# Image
st.image('Landscape.png')

# Video
#st.video('C:/Users/OP.mp4')

#### Creating Layouts ####
# Sidebar 
st.sidebar.header('Sidebar me Header')

# Columns
st.columns(2)
col1, col2 = st.columns(2)

with col1:
    st.header('Column 1')
    st.image('Landscape.png')
    
with col2:
    st.header('Column 2')
    st.image('Landscape.png')
    
##### Showing Status #####

# Error Msg
st.error('This is an error')
st.success('This is a success')
st.warning('This is a warning')
st.info('This is an info')

# Progress Bar

bar = st.progress(0)
for i in range(100):
    #time.sleep(0.1)
    bar.progress(i+1)
    

# Taking User input

# Text Input
name = st.text_input('Enter your name', 'Type here...')
number  = st.number_input('Enter a number', 1, 100)
data = st.date_input('Enter a date')

# Buttons 
# Making A Login Page 

email = st.text_input('Enter your email')
password = st.text_input('Enter your password', type='password')
gender = st.selectbox('Select a number', ["male",'Female','Others']) # Dropdowns

btn = st.button('Login')

if btn:
    if email == 'shashank@gmail.com' and password == '12345':
        st.success('Login successful')
        st.balloons() # Baloons will be displayed on the screen
        st.write(gender)
    else:
        st.error('Login failed')
