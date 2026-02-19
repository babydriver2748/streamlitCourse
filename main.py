import streamlit as st

st.title("Welcome Streamlit Full Course")
st.subheader("Stream is Hero")
st.text("Streamlit is very easy and magic")
st.write("Magic")
st.chat_input("Enter you message")

st.audio_input("Record Message for Me")
chai = st.selectbox("Select you favroit Chai:",["Desi Chai", "Masala Chai","Lemon chai", "black tea"])

st.write(f"You Choice is great {chai}")

st.success("your Order is placed")