import streamlit as st

st.title("Welcome Streamlit Full Course")
st.subheader("Streamlit is Hero")
st.text("Streamlit is very easy and magic")

course = st.selectbox("Select Course :",["Python", "C++","Java","Kotlin","Web Devlopment"])

st.write(f"You selected {course}")

st.success(f"You are succeessfuly Registred with {course} course")