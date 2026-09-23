import streamlit as st
import pandas as pd

st.write("Hello world")

st.title("Hello streamlit")
st.write("This is my first streamlit App")

st.header("Welcome to streamlit")
st.subheader("This is subheader")
st.text("This is plain text")


## buttons , checkbox , and sliders

if st.button("Click me"):
    st.write("Button clicked")

agre=st.checkbox("I agree")
if  agre:
    st.write("You agree")

level =st.slider("select a level : ", 1,10,5)
st.write(f"selected level : {level}")


uploaded_file= st.file_uploader("Upload a file",type=["csv","txt"])

if uploaded_file is not None :
    df=pd.read_csv(uploaded_file)
    st.write(df.head())
    

