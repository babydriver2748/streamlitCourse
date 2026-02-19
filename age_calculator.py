import streamlit as st
import datetime as dt

st.time_input("Age Calculator")

st.subheader("Enter your birth date. Know How Old👴 are You !")

dob = st.date_input("Select Your DOB")

today = dt.date

st.write(f"Entered date : {dob}")

st.write(f"Today date : {today}")