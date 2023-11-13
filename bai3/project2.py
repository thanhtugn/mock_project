import streamlit as st
import cv2
import numpy as np

def rotate_image(image, angle):
    height, width = image.shape[:2]
    rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), angle, 1)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))
    return rotated_image

def adjust_brightness(image, factor):
    adjusted_image = cv2.convertScaleAbs(image, alpha=factor, beta=0)
    return adjusted_image

def filter_color(image, color):
    if color == 'anh':
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    elif color == 'đỏ' :
        return cv2.merge((image[:, :, 2], np.zeros_like(image[:, :, 2]), np.zeros_like(image[:, :, 2])))
    elif color == 'xanh':
        return cv2.merge((np.zeros_like(image[:, :, 2]), np.zeros_like(image[:, :, 2]), image[:, :, 0]))

def crop_image(image, x1, y1, x2, y2):
    cropped_image = image[y1:y2, x1:x2]
    return cropped_image

st.title("Ứng dụng xử lý hình ảnh")

uploaded_image = st.file_uploader("Chọn một hình ảnh", type=["jpg", "jpeg", "png"])

# Để hiển thị hai cột
col1, col2 = st.beta_columns(2)

if uploaded_image is not None:
    image = cv2.imdecode(np.fromstring(uploaded_image.read(), np.uint8), 1)

    # Hiển thị hình ảnh gốc ở cột đầu tiên
    with col1:
        st.image(image, caption="Hình ảnh gốc", use_column_width=True)

    # Hiển thị hình ảnh sau chỉnh sửa ở cột thứ hai
    with col2:
        st.image(image, caption="Hình ảnh sau khi chỉnh sửa", use_column_width=True)

    # Chức năng chỉnh sửa hình ảnh
    if st.button("Xoay ảnh"):
        angle = st.slider("Chọn góc xoay", -180, 180, 0)
        image = rotate_image(image, angle)

    if st.button("Chỉnh đậm/nhạt"):
        factor = st.slider("Chọn độ đậm/nhạt", 0.1, 3.0, 1.0)
        image = adjust_brightness(image, factor)

    color_filter = st.selectbox("Lọc màu", ["None", "anh", "đỏ", "xanh"])
    if color_filter != "None":
        image = filter_color(image, color_filter)

    if st.button("Cắt ảnh"):
        x1 = st.number_input("X1", 0, image.shape[1], 0)
        y1 = st.number_input("Y1", 0, image.shape[0], 0)
        x2 = st.number_input("X2", 0, image.shape[1], image.shape[1])
        y2 = st.number_input("Y2", 0, image.shape[0], image.shape[0])
        image = crop_image(image, x1, y1, x2, y2)