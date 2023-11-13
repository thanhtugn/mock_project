## STREAMLIT
# install :
"""
pip install streamlit opencv-python tensorflow[and-cuda]

"""

## Bài tập khởi động 
"""
    Bài tập 1: Tạo nút nhấn và hiển thị
        Tạo một ứng dụng Streamlit đơn giản với một nút nhấn.
        Khi người dùng nhấn nút, hiển thị một dòng chữ "Hello"

    Bài tập 2: Sự kiện và cập nhật dữ liệu
        Tạo một ứng dụng với một ô văn bản và một nút nhấn.
        Khi người dùng nhập văn bản và nhấn nút, hiển thị thông điệp dựa trên văn bản họ đã nhập.

    Bài tập 3: Chia cột và hiển thị danh sách
        Tạo một ứng dụng với hai cột.
        Trong cột bên trái, hiện thị 1 đoạn văn bất kì
        Trong cột bên phải, hiện thị 1 đoạn văn bất kì

    Bài tập 4: Tải lên tệp và hiển thị hình ảnh
        Tạo một ứng dụng cho phép người dùng tải lên một tệp hình ảnh.
        Khi họ tải lên, hiển thị hình ảnh trong ứng dụng.

    Bài tập 5: Chọn hình ảnh từ danh sách và hiển thị
        Tạo một ứng dụng với một danh sách các hình ảnh và một nút nhấn.
        Khi người dùng nhấn nút, hiển thị hình ảnh được chọn từ danh sách lên giao diện.

    Run : streamlit run baitap.py --> web : http://localhost:8501/
    Tham khảo : https://docs.streamlit.io/library/get-started
                https://docs.streamlit.io/library/api-reference

"""

## Dự án 

"""
1. Tạo web bằng streamlit, tensorflow . Có chức năng : cộng trừ nhằn chia ma trận
    - Nhập vào kích thước ma trận 1 ,2 
    - Nhập vào ma trận 1,2 
    - 4 Button : Cộng, Trừ, Nhân , Chia 
    - 1 Button : Sử dụng GPU để tính toán 
    - Hiển thị ma trận kết quả 

2. Tạo web bằng streamlit, cv2 . Có chức năng : Xử lí hỉnh ảnh 

    - Nhập vào 1 hình ảnh
    - Hiển thị hình ảnh
    - 5 button với chức năng chỉnh sửa hỉnh ảnh : 
        + Xoay ảnh : -180 -> 180 độ 
        + Chỉnh đậm nhạt
        + Lọc màu : anh, đỏ , ghi 
        + Crop ảnh 
    - Hiền thị hình ảnh sau khi chỉnh sửa  
"""