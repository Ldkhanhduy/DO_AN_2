# Hệ thống Gợi ý Laptop

## Tổng quan
Dự án này xây dựng một hệ thống gợi ý laptop sử dụng thuật toán Random Forest và giao diện Streamlit. Hệ thống gợi ý laptop dựa trên bốn nhu cầu sử dụng: **Chơi game**, **Văn phòng**, **Thiết kế đồ họa**, và **Sinh viên Công nghệ thông tin**, sử dụng tập dữ liệu thông số laptop.

## Cấu trúc dự án
- `app.py`: Ứng dụng Streamlit chính cung cấp giao diện người dùng.
- `train_model.py`: Tệp xử lý dữ liệu, huấn luyện mô hình Random Forest và đánh giá.
- `requirements.txt`: Danh sách các gói Python cần thiết.
- `preprocessed_laptop.xlsx`: Tập dữ liệu chứa thông số laptop.
- `README.md`: Tài liệu hướng dẫn dự án.

## Cài đặt
1. Sao chép kho lưu trữ:
   ```bash
   git clone <repository-url>
   cd laptop_recommender
   ```
2. Cài đặt các gói phụ thuộc:
   ```bash
   pip install -r requirements.txt
   ```
3. Đảm bảo tệp `preprocessed_laptop.xlsx` nằm trong thư mục dự án.

## Sử dụng
1. Huấn luyện mô hình:
   ```bash
   python train_model.py
   ```
   Tệp này sẽ xử lý dữ liệu, huấn luyện mô hình Random Forest và lưu mô hình cùng bộ mã hóa.

2. Chạy ứng dụng Streamlit:
   ```bash
   streamlit run app.py
   ```
   Mở URL được cung cấp trong trình duyệt, chọn nhu cầu sử dụng và xem top 5 laptop được gợi ý.

## Chi tiết mô hình
- **Thuật toán**: Random Forest Classifier
- **Đặc trưng**: CPU, GPU, RAM, ROM, Kích thước màn hình, CPU Tier, GPU Tier, Screen Tier
- **Mục tiêu**: Nhu cầu sử dụng (Chơi game, Văn phòng, Thiết kế đồ họa, Sinh viên CNTT)
- **Chỉ số đánh giá**: Precision (trung bình có trọng số)
- **Xử lý dữ liệu**:
  - Xử lý giá trị thiếu trong cột `Prices` bằng cách điền giá trị trung bình.
  - Trích xuất kích thước màn hình số từ cột `Screen`.
  - Mã hóa các biến phân loại (Brand, CPU, GPU, OS) bằng `LabelEncoder`.
  - Gán nhu cầu sử dụng dựa trên các quy tắc được xác định trước.

## Đánh giá
Hiệu suất mô hình được đánh giá bằng chỉ số **precision**, đo lường tỷ lệ dự đoán chính xác cho mỗi lớp. Điểm precision được in ra trong quá trình huấn luyện mô hình.

## Lưu ý
- Đảm bảo tệp dữ liệu `preprocessed_laptop.xlsx` có sẵn trong thư mục dự án.
- Hệ thống gợi ý tối đa 5 laptop cho mỗi nhu cầu, hiển thị thông tin như Tên, Thương hiệu, CPU, GPU, RAM, ROM, Màn hình, Giá và link sản phẩm.
- Mô hình giả định dữ liệu có định dạng nhất quán cho các cột như `Screen` và `Prices`.

## Yêu cầu
- Python 3.8 trở lên
- Xem `requirements.txt` để biết phiên bản các gói.
