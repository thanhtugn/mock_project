# Tạo một ứng dụng Streamlit đơn giản với một nút nhấn.
#         Khi người dùng nhấn nút, hiển thị một dòng chữ "Hello"

import streamlit as st

st.title("Simple Streamlit Application")

if st.button("Click here"):
    st.write("Hello")

if st.button("Reset"):
    st.text("")  # Clear the previous output when the "Reset" button is clicked
