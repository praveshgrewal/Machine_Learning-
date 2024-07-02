import streamlit as st
import pandas as pd
import numpy as np

#title
st.title("My first Web App")

#display a simple text
st.write("Hello, *World!* :smile:")

#create a simple dataframe
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

#display the dataframe
st.write(df)

#create a line chart
chart = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(chart)    

#widgets
st.markdown("----")
st.title("Widgets")

name= st.text_input("Enter your name: ")
if name:
    st.write("Hello " + name)

#slider
age = st.slider('How old are you?', 0, 100, 18)
st.write("I'm ", age, "years old")

#checkbox
agree = st.checkbox('I agree')
if agree:
    st.write("Great! Let's proceed.")

#options
option= ['python', 'R', 'Julia', 'C', 'C++','javescript']
language = st.selectbox('Select a language:', option)

st.write("You selected:", language)

data={
    'Name': ['Pravesh', 'Grewal'],
    'Age': [22, 23],
    'city': ['Pune', 'Mumbai']
}
df= pd.DataFrame(data)
st.dataframe(df)
df.to_csv('data.csv')

#table
st.table(df)

#create a upload button
uploaded_file = st.file_uploader("Choose a file", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)

