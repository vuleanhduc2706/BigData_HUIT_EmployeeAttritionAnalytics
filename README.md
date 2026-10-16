# HỆ THỐNG PHÂN TÍCH ĐA CHIỀU & DỰ ĐOÁN NGUY CƠ NGHỈ VIỆC (BIG DATA LAB)

**Sinh viên thực hiện:** Vũ Lê Anh Đức  
**Mã số sinh viên (MSSV):** 2001230191  
**Học phần:** Các công nghệ dữ liệu lớn (Big Data Technologies)

---

## 📁 CẤU TRÚC 3 THƯ MỤC PHÂN TÁCH HOÀN TOÀN (GỌN GÀNG & ĐÚNG MỤC ĐÍCH)

Cây thư mục đã được phân tách rõ ràng thành 3 phần độc lập tuyệt đối:

```text
D:\Doan_BigData\
│
├── 📂 Web_Demo_DoAn/               # [GÓI NỘP BÀI DEMO] CHỈ CHỨA DUY NHẤT MÃ NGUỒN CHẠY WEB & ĐỒ ÁN
│   ├── 🚀 run_web.bat              # Phím tắt click đúp để giáo viên chạy Web ngay lập tức
│   ├── 📄 HUONG_DAN_CHAY.md        # Hướng dẫn chấm bài dành riêng cho giáo viên
│   ├── 🐍 app.py                   # Flask Server điều khiển toàn bộ 6 Tab Web Client (Port 5000)
│   ├── 📁 src/                     # Toàn bộ 9 Bước Pipeline PySpark, MLlib, Kafka, Airflow
│   │   ├── step1_hdfs_prepare.py
│   │   ├── step2_upload_ingest.py
│   │   ├── step3_spark_read.py
│   │   ├── step4_clean_transform.py
│   │   ├── step4b_parquet_compaction.py
│   │   ├── step5_spark_sql.py
│   │   ├── step6_ml_predict.py
│   │   ├── step7_save_results.py
│   │   ├── step8_kafka_simulation.py
│   │   └── step9_airflow_dag.py
│   ├── 📁 data/                    # Medallion Data Lake: raw/, processed/, output/ (18 file KPIs, Model .pkl)
│   ├── 📁 templates/ & static/     # Giao diện Web Dashboard tương tác cao cấp
│   ├── 📁 airflow/                 # DAGs và module tương thích Airflow
│   ├── 📁 backend-nestjs/          # REST API Backend NestJS TypeScript (Port 3000)
│   └── 📄 Dataset.csv & WA_Fn-UseC_-HR-Employee-Attrition.csv
│
├── 📂 BaoCao_Word/                 # [TÀI LIỆU RIÊNG] TẤT CẢ FILE WORD, PDF, SLIDE BÀI GIẢNG
│   ├── 📄 BaoCao_TienDo_GiuKy_VuLeAnhDuc_2001230191.pdf
│   ├── 📄 BaoCao_TienDo_GiuKy_VuLeAnhDuc_2001230191.docx
│   ├── 📄 BaoCao_HeThong_BigData_PhanTich_NhanSu.docx
│   ├── 📊 Lecture_4_Ingestion_Revised.pptx
│   └── 📁 LyThuyet/                # Slide bài giảng lý thuyết C1 - C4
│
├── 📂 Tools_Scripts/               # [CÔNG CỤ RIÊNG] CÁC TOOL SINH FILE & KIỂM THỬ
│   ├── create_progress_report.py   # Tool sinh báo cáo tiến độ Word & PDF
│   ├── create_report_word.py       # Tool sinh thuyết minh hệ thống Word
│   └── run_pipeline_step1_to_3.py  # Script test pipeline
│
├── 📦 Web_Demo_DoAn.zip            # TỆP NÉN SẴN GÓI WEB DEMO ĐỂ GỬI GIÁO VIÊN (0.96 MB)
├── 🚀 run_web.bat                  # Phím tắt mở Web từ thư mục gốc
├── 🐍 run_web.py                   # Script Python mở Web từ thư mục gốc
└── 📄 README.md                    # Tài liệu tổng quan này
```

---

## 🚀 HƯỚNG DẪN NỘP BÀI WEB DEMO CHO GIÁO VIÊN

Khi nộp bài cho giáo viên chấm phần chạy demo:
1. Bạn chỉ cần nộp file nén **`Web_Demo_DoAn.zip`** (đã đóng gói sẵn ngay tại thư mục gốc `D:\Doan_BigData\`).
2. Hoặc nén trực tiếp thư mục **`Web_Demo_DoAn`**.
3. Giáo viên giải nén ra sẽ có sẵn file **`run_web.bat`** để click đúp chạy ngay hệ thống tại `http://localhost:5000` mà không cần cấu hình phức tạp.
