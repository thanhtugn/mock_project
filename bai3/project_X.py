import streamlit as st
import pandas as pd
import numpy as np

st.title("VTI MOCK")

column1, column2 = st.columns(2)

if "add" not in st.session_state:
    st.session_state.add = False
if "subtract" not in st.session_state:
    st.session_state.subtract = False
if "multiply" not in st.session_state:
    st.session_state.multiply = False
if "divide" not in st.session_state:
    st.session_state.divide = False

with column1:
    st.write("Nhập kích thước ma trận A")
    rows_A = st.number_input("Số hàng của ma trận A", min_value=1, value=1)
    cols_A = st.number_input("Số cột của ma trận A", min_value=1, value=1)

    st.write("Nhập giá trị cho ma trận A:")
    dfa = pd.DataFrame(data=[[0.0] * cols_A] * rows_A)

    for i in range(rows_A):
        for j in range(cols_A):
            dfa.iloc[i, j] = st.number_input(f"Giá trị ở hàng {i+1}, cột {j+1}", key=f'A_{i}_{j}')

    st.write("Ma trận A:")
    st.write(dfa)

with column2:
    st.write("Nhập kích thước ma trận B")
    rows_B = st.number_input("Số hàng của ma trận B", min_value=1, value=1)
    cols_B = st.number_input("Số cột của ma trận B", min_value=1, value=1)

    st.write("Nhập giá trị cho ma trận B:")
    dfb = pd.DataFrame(data=[[0.0] * cols_B] * rows_B)

    for i in range(rows_B):
        for j in range(cols_B):
            dfb.iloc[i, j] = st.number_input(f"Giá trị ở hàng {i+1}, cột {j+1}", key=f'B_{i}_{j}')

    st.write("Ma trận B:")
    st.write(dfb)

st.sidebar.markdown("# Function")

add_button = st.sidebar.button("Cộng")
subtract_button = st.sidebar.button("Trừ")
multiply_button = st.sidebar.button("Nhân")
divide_button = st.sidebar.button("Chia")

use_GPU = st.sidebar.checkbox("Sử dụng GPU")

if use_GPU:
    st.sidebar.write("GPU is enabled.")
else:
    st.sidebar.write("GPU is not enabled.")

if add_button:
    st.session_state.add = True
    st.session_state.subtract = False
    st.session_state.multiply = False
    st.session_state.divide = False

if subtract_button:
    st.session_state.add = False
    st.session_state.subtract = True
    st.session_state.multiply = False
    st.session_state.divide = False

if multiply_button:
    st.session_state.add = False
    st.session_state.subtract = False
    st.session_state.multiply = True
    st.session_state.divide = False

if divide_button:
    st.session_state.add = False
    st.session_state.subtract = False
    st.session_state.multiply = False
    st.session_state.divide = True

# Đảm bảo kiểm tra điều kiện cho phép cộng trừ nhân chia
if not st.session_state.add:
    add_button_placeholder = st.sidebar.empty()
if not st.session_state.subtract:
    subtract_button_placeholder = st.sidebar.empty()
if not st.session_state.multiply:
    multiply_button_placeholder = st.sidebar.empty()
if not st.session_state.divide:
    divide_button_placeholder = st.sidebar.empty()

result_button = st.sidebar.button("Kết quả")

if result_button:
    if st.session_state.add:
        if rows_A == rows_B and cols_A == cols_B:
            result = dfa.add(dfb, fill_value=0)
            st.write("Kết quả (Cộng):")
            st.dataframe(result)
        else:
            st.sidebar.write("Số hàng và số cột của ma trận A và B phải giống nhau để thực hiện phép cộng.")
    elif st.session_state.subtract:
        if rows_A == rows_B and cols_A == cols_B:
            result = dfa.sub(dfb, fill_value=0)
            st.write("Kết quả (Trừ):")
            st.dataframe(result)
        else:
            st.sidebar.write("Số hàng và số cột của ma trận A và B phải giống nhau để thực hiện phép trừ.")
    elif st.session_state.multiply:
        if cols_A == rows_B:
            result = dfa.dot(dfb)
            st.write("Kết quả (Nhân):")
            st.dataframe(result)
        else:
            st.sidebar.write("Số cột của ma trận A phải bằng số hàng của ma trận B để thực hiện phép nhân.")
    elif st.session_state.divide:
        if cols_A == rows_B:
            try:
                inv_dfb = np.linalg.inv(dfb)
                result = dfa.dot(inv_dfb)
                st.write("Kết quả (Chia):")
                st.dataframe(result)
            except np.linalg.LinAlgError:
                st.sidebar.write("Ma trận B không khả nghịch, không thể thực hiện phép chia.")
        else:
            st.sidebar.write("Số cột của ma trận A phải bằng số hàng của ma trận B để thực hiện phép chia.")


