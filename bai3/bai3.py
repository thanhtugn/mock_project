# Tạo một ứng dụng với hai cột.
#         Trong cột bên trái, hiện thị 1 đoạn văn bất kì
#         Trong cột bên phải, hiện thị 1 đoạn văn bất kì

import streamlit as st

st.title("Streamlit Application with Two Columns")

left_column, right_column = st.columns(2)

with left_column:
        button_names = ["Button 1", "Button 2", "Button 3", "Button 4", "Button 5"]

        for button_name in button_names:
            if st.button(button_name):
                st.write("{button_name}")
    
with right_column:
    st.write("Paragraph in the right column")
