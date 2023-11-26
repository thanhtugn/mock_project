import os
import numpy as np
import matplotlib.pyplot as plt
import random
from PIL import Image
from keras.models import load_model
from tensorflow.python.keras.utils import np_utils
from streamlit_drawable_canvas import st_canvas
import streamlit as st

# Load the model
model = load_model('dense_model.h5')

# Create a function to preprocess the image
def process_image(image):
    image = image.resize((28, 28))
    image = image.convert('L')
    image = np.array(image)
    image = image.reshape(1, 784)
    image = image.astype('float32')
    image /= 255
    return image

# Create the web app
st.title("Handwritten Digit Recognition")

# Create two columns
col1, col_space, col2 = st.columns([10,1,10])

# Column 1: Draw and predict
with col1:
    st.header("Draw and Predict")
    # Create a selectbox for the user to choose the prefix of the filename
    prefix = st.selectbox("Choose the prefix of the filename:", ["anh0", "anh1", "anh2", "anh3", "anh4", "anh5", "anh6", "anh7", "anh8", "anh9"])

    # Create a slider to adjust the stroke width
    stroke_width = st.slider("Stroke width: ", min_value=1, max_value=25, value=10)

    # Create a canvas for the user to draw on
    st.write("Draw a digit:")
    canvas_result = st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)",  # Fixed drawing color with alpha
        stroke_width=stroke_width,  # Use the value from the slider
        stroke_color='#ffffff',
        background_color="#000000",
        width=280,
        height=280,
        drawing_mode="freedraw",
        key="canvas",
    )

    # If the user has drawn on the canvas
    if canvas_result.image_data is not None:
        img = Image.fromarray(np.uint8(canvas_result.image_data)).convert('L')
        img = img.resize((28,28))
        img_arr = np.array(img)
        # Check if the image is not blank
        if np.any(img_arr):
            # Add a predict button
            if st.button('Predict'):
                # Process the image and predict the digit
                processed_image = process_image(img)
                prediction = model.predict(processed_image).argmax()
                # Display the prediction
                st.write(f"Predicted digit: {prediction}")

# Cột trống giữa hai cột khác
with col_space:
    st.write("")

# Column 2: Upload and predict
with col2:
    st.header("Upload and Predict")
    # Thêm một nút để tải lên ảnh
    uploaded_file = st.file_uploader("Choose an image...", type="png")

    # Nếu một tệp đã được tải lên
    if uploaded_file is not None:
        # Mở và xử lý hình ảnh
        img = Image.open(uploaded_file)
        img = img.resize((28,28))
        img_arr = np.array(img)

        # Hiển thị hình ảnh đã tải lên
        st.image(img, caption='Uploaded Image.')
        
        # Nếu hình ảnh không trống
        if np.any(img_arr):
            # Thêm một nút để dự đoán chữ số
            if st.button('Predict Uploaded Image'):
                # Xử lý hình ảnh và dự đoán chữ số
                processed_image = process_image(img)
                prediction = model.predict(processed_image).argmax()
                # Hiển thị dự đoán
                st.write(f"Predicted digit: {prediction}")
