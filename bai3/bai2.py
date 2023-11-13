# Tạo một ứng dụng với một ô văn bản và một nút nhấn.
#         Khi người dùng nhập văn bản và nhấn nút, hiển thị thông điệp dựa trên văn bản họ đã nhập.

import streamlit as st

st.title("Streamlit Application with Text Input and Button")

user_input = st.text_input("Enter text here:")

if st.button("Display Message"):
    if user_input:
        st.write("Your message:", user_input)
    else:
        st.write("You haven't entered any text.")
