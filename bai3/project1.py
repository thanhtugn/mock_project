# 1. Tạo web bằng streamlit, tensorflow . Có chức năng : cộng trừ nhằn chia ma trận
#     - Nhập vào kích thước ma trận 1 ,2 
#     - Nhập vào ma trận 1,2 
#     - 4 Button : Cộng, Trừ, Nhân , Chia 
#     - 1 Button : Sử dụng GPU để tính toán 
#     - Hiển thị ma trận kết quả 

import streamlit as st
import numpy as np
import tensorflow as tf

st.title("Máy tính ma trận")

def perform_matrix_operation(matrices, operation):
    if operation == 'Cộng':
        result = sum(matrices)
    elif operation == 'Trừ':
        result = matrices[0]
        for matrix in matrices[1:]:
            result = matrices[0] - sum(matrices[1:])
    elif operation == 'Nhân':
        result = matrices[0]
        for matrix in matrices[1:]:
            result = np.dot(result, matrix)
    elif operation == 'Chia':
        result = matrices[0]
        for matrix in matrices[1:]:
            result = np.divide(result, matrix, out=np.zeros_like(result), where=matrix != 0)
    return result

num_matrices = st.number_input("Nhập số ma trận", min_value=2, step=1)

matrices = []

for i in range(num_matrices):
    st.write(f"Nhập ma trận {i + 1}:")
    rows = st.number_input(f"Số hàng (dòng) của ma trận {i + 1}", min_value=1, step=1)
    cols = st.number_input(f"Số cột của ma trận {i + 1}", min_value=1, step=1)
    matrix = np.zeros((rows, cols))

    st.write(f"Nhập giá trị cho ma trận {i + 1}:")
    for j in range(rows):
        for k in range(cols):
            value = st.number_input(f"Hàng {j + 1}, cột {k + 1} (ma trận {i + 1})", value=str(matrix[j, k]))
    matrices.append(matrix)

operation = st.selectbox("Chọn phép tính", ["Cộng", "Trừ", "Nhân", "Chia"])

use_gpu = st.button("Tính toán")

def check_matrix_sizes(matrices, operation):
    if operation in ['Cộng', 'Trừ']:
        num_rows, num_cols = matrices[0].shape

        for matrix in matrices[1:]:
            if matrix.shape != (num_rows, num_cols):
                return False
            
    elif operation == 'Nhân':
        for i in range(len(matrices) - 1):
            if matrices[i].shape[1] != matrices[i+1].shape[0]:
                return False
            
    elif operation == 'Chia':
        for i in range(len(matrices) - 1):
            if matrices[i].shape != matrices[i+1].shape:
                return False

    return True

if use_gpu:
    with tf.device("/GPU:0"):
        if check_matrix_sizes(matrices, operation):
            result = perform_matrix_operation(matrices, operation)
            st.subheader("Kết quả:")
            for i in range(num_matrices):
                st.write(f"Ma trận {i + 1}:")
                st.dataframe(matrices[i])
                if i < num_matrices - 1:
                    st.markdown(f"<span>{' + ' if operation == 'Cộng' else ' - ' if operation == 'Trừ' else ' x ' if operation == 'Nhân' else ' / '}</span>", unsafe_allow_html=True)
            st.write("= ")
            st.dataframe(result)
        else:
            st.write("Kích thước của các ma trận không phù hợp cho phép tính")
else:
    if check_matrix_sizes(matrices, operation):
        result = perform_matrix_operation(matrices, operation)
        st.subheader("Kết quả:")
        for i in range(num_matrices):
            st.write(f"Ma trận {i + 1}:")
            st.dataframe(matrices[i])
            if i < num_matrices - 1:
                st.markdown(f"<span>{' + ' if operation == 'Cộng' else ' - ' if operation == 'Trừ' else ' x ' if operation == 'Nhân' else ' / '}</span>", unsafe_allow_html=True)
        st.write("= ")
        st.dataframe(result)
    else:
        st.write("Kích thước của các ma trận không phù hợp cho phép tính")
