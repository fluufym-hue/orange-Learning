import streamlit as st

st.title("Interactive Streamlit App")

mame = st.text_input("Enter your name:")


if st.button("Submit"):
   st.write(f"Hello, {name}! Welcome to Streamlit.")