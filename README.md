
# Giới thiệu về trang web CareerViet

Dữ liệu trong đồ án này được thu thập từ trang web CareerViet.vn, một trong những nền tảng tuyển dụng hàng đầu tại Việt Nam. Dữ liệu bao gồm các thông tin tuyển dụng từ nhiều công ty thuộc các ngành nghề khác nhau, giúp cung cấp cái nhìn tổng quan về thị trường lao động hiện nay. Việc phân tích dữ liệu này có thể hỗ trợ trong việc hiểu rõ xu hướng tuyển dụng, mức lương, yêu cầu kinh nghiệm và các yếu tố quan trọng khác trong tuyển dụng.

# Giới thiệu về dữ liệu

Dữ liệu được lưu trữ trong tệp `jobs_data_careerviet.csv`, bao gồm một sheet chính chứa 15,140 dòng và 11 cột chứa thông tin chi tiết về các tin tuyển dụng.

## Thông tin về các vị trí tuyển dụng

- **title**: Tên vị trí tuyển dụng.
- **company**: Tên công ty đăng tuyển.
- **place**: Địa điểm làm việc.
- **publish day**: Ngày đăng tin tuyển dụng.
- **field**: Ngành nghề liên quan đến công việc.
- **employee status**: Hình thức làm việc (nhân viên chính thức, bán thời gian,...).
- **salary**: Mức lương đề xuất.
- **experiment**: Yêu cầu kinh nghiệm cho vị trí ứng tuyển.
- **level**: Cấp bậc công việc (Nhân viên, Trưởng nhóm, Quản lý,...).
- **due day**: Hạn cuối để nộp hồ sơ ứng tuyển.
- **welfares**: Các chế độ đãi ngộ mà công ty cung cấp (bảo hiểm, du lịch, thưởng, phụ cấp, v.v.).

# Phương pháp crawl dữ liệu
- Đầu tiên sử dụng BeautifulSoup và Request để thực hiện nhưng gặp lỗi 403. Website đã chặn request từ máy.  
- Chuyển sang sử dụng selenium và chromedriver. Khắc phục được lỗi 403.  
- Thực hiện crawl thông thường bằng phương pháp trích xuất HTML từ web.  
- Các thông tin từ các trường đưa ra trên trang thông tin tổng quát không được đầy đủ. Phải thực hiện thêm một bước phụ.  
- Thực hiện tạo các tab mới là các bài đăng tin cụ thể, sau đó chuyển hướng vào tab rồi thực hiện trích xuất HTML như thông thường. Sau khi thực hiện xong đóng tab và trở về trang chính.  
- Quá trình thực hiện tùy thuộc vào mạng và độ load của trang nên phải đặt delay các thao tác đi một khoảng. Làm kéo dài quá trình crawl.  
- Quá trình crawl một lượng lớn trong thời gian dài làm máy bị màn xanh. Giải pháp đưa ra là chia thành từng đoạn nhỏ, lưu từng dòng tức thì khi đã crawl về.  

---


