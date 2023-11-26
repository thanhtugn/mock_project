import os
import numpy as np
import matplotlib.pyplot as plt
import random
from PIL import Image
from keras.models import load_model
from tensorflow.python.keras.utils import np_utils
from streamlit_drawable_canvas import st_canvas
import streamlit as st

model = load_model('dense_model.h5')

def process_image(image):
    image = image.resize((28, 28))
    image = image.convert('L')
    image = np.array(image)
    image = image.reshape(1, 784)
    image = image.astype('float32')
    image /= 255
    return image

st.title("Handwritten Digit Recognition")

col1, col_space, col2 = st.columns([10,1,10])

with col1:
    st.header("Draw and Predict")
    prefix = st.selectbox("Choose the prefix of the filename:", ["anh0", "anh1", "anh2", "anh3", "anh4", "anh5", "anh6", "anh7", "anh8", "anh9"])

    stroke_width = st.slider("Stroke width: ", min_value=1, max_value=25, value=10)

    st.write("Draw a digit:")
    canvas_result = st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)",  
        stroke_width=stroke_width,  
        stroke_color='#ffffff',
        background_color="#000000",
        width=280,
        height=280,
        drawing_mode="freedraw",
        key="canvas",
    )

    if canvas_result.image_data is not None:
        img = Image.fromarray(np.uint8(canvas_result.image_data)).convert('L')
        img = img.resize((28,28))
        img_arr = np.array(img)
        if np.any(img_arr):
            if st.button('Predict'):
                processed_image = process_image(img)
                prediction = model.predict(processed_image).argmax()
                st.write(f"Predicted digit: {prediction}")

with col_space:
    st.write("")

with col2:
    st.header("Upload and Predict")
    uploaded_file = st.file_uploader("Choose an image...", type="png")

    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        img = img.resize((28,28))
        img_arr = np.array(img)

        st.image(img, caption='Uploaded Image.')
        
        if np.any(img_arr):
            if st.button('Predict Uploaded Image'):
                processed_image = process_image(img)
                prediction = model.predict(processed_image).argmax()
                st.write(f"Predicted digit: {prediction}")
