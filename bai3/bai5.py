# Tạo một ứng dụng với một danh sách các hình ảnh và một nút nhấn.
#         Khi người dùng nhấn nút, hiển thị hình ảnh được chọn từ danh sách lên giao diện.

import streamlit as st

image_urls = {
    "Image 1": "images.jpeg",
    "Image 2": "images (1).jpeg",
    "Image 3": "images (2).jpeg",
}

st.title("Streamlit App with Image Selection")

selected_image = st.selectbox("Select an image:", list(image_urls.keys()))

if st.button("Display Image"):
    if selected_image:
        image_url = image_urls[selected_image]
        st.image(image_url, caption=f"Image {selected_image}", use_column_width=True)
    else:
        st.write("Please select an image.")
