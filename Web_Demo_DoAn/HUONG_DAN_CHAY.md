# HƯỚNG DẪN KIỂM TRA VÀ CHẤM ĐỒ ÁN BIG DATA

**Học phần:** Các công nghệ dữ liệu lớn (Big Data Technologies)  
**Sinh viên thực hiện:** Vũ Lê Anh Đức  
**Mã số sinh viên (MSSV):** 2001230191  
**Đề tài:** Hệ thống phân tích đa chiều & dự đoán nguy cơ nghỉ việc của nhân sự (BigData Lab)

---

## 1. CÁC TÀI LIỆU BÁO CÁO KÈM THEO
Tại thư mục gốc của gói nộp bài này đã đính kèm đầy đủ:
- **`BaoCao_TienDo_GiuKy_VuLeAnhDuc_2001230191.pdf`**: Báo cáo tiến độ hoàn chỉnh xuất định dạng PDF.
- **`BaoCao_TienDo_GiuKy_VuLeAnhDuc_2001230191.docx`**: Báo cáo tiến độ định dạng Microsoft Word.
- **`BaoCao_HeThong_BigData_PhanTich_NhanSu.docx`**: Thuyết minh kỹ thuật kiến trúc hệ thống 9 bước Big Data.

---

## 2. KHỞI CHẠY WEB CLIENT DASHBOARD TƯƠNG TÁC (KHUYẾN NGHỊ)
Thầy/Cô có thể trải nghiệm trực tiếp hệ thống theo các bước sau:

1. **Cách 1 (Nhanh nhất):** Click đúp vào tệp **`run_web.bat`** tại thư mục này.
2. **Cách 2 (Qua dòng lệnh Terminal / Command Prompt):**
   ```bash
   python app.py
   ```
3. Mở trình duyệt Web tại địa chỉ: **http://localhost:5000**

### Các tính năng trực quan trên Web Dashboard:
- **Tab 1 - Pipeline 9 Bước & Terminal Interactive:** Thực thi từng bước hoặc toàn bộ chuỗi Pipeline Big Data.
- **Tab 2 - Spark SQL Analytics:** 6 biểu đồ Chart.js phân tích đa chiều nhân sự.
- **Tab 3 - MLlib K-Means & Random Forest:** Phân cụm 4 nhóm nhân sự và đo lường độ quan trọng đặc trưng (Feature Importance).
- **Tab 4 - Kafka Live Streaming:** Ticker và bảng cảnh báo rủi ro chấm công thời gian thực.
- **Tab 5 - AI Risk Simulator:** Bộ tính điểm xác suất nghỉ việc và xuất khuyến nghị hành động cho phòng HR.
- **Tab 6 - Apache Airflow DAG:** Sơ đồ chuỗi điều phối tự động hóa và đối chiếu dữ liệu phân tán.

---

## 3. KHỞI CHẠY NESTJS REST API BACKEND (TÙY CHỌN)
Nếu Thầy/Cô muốn kiểm tra thêm backend độc lập bằng NestJS TypeScript:
```bash
cd backend-nestjs
npm install
npm run start:dev
```
Hệ thống cung cấp REST API tại địa chỉ: **http://localhost:3000**
