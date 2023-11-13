# Tạo một ứng dụng cho phép người dùng tải lên một tệp hình ảnh.
        # Khi họ tải lên, hiển thị hình ảnh trong ứng dụng.


import streamlit as st

# Application title
st.title("Streamlit App for Uploading and Displaying Images")

# Allow users to upload an image file
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

# Display the image if the user has uploaded one
if uploaded_image is not None:
    st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)
