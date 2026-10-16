# Big Data HR Attrition - NestJS API Backend

Dự án API Backend xây dựng bằng **NestJS (TypeScript)** nhằm đáp ứng yêu cầu:
> *"Xây dựng API Backend (sử dụng NestJS) để truy xuất kết quả từ Spark SQL phục vụ cho giao diện Web."*
> Sinh viên: **Vũ Lê Anh Đức** - MSSV: **2001230191**

---

## 1. Cấu trúc thư mục NestJS
```text
backend-nestjs/
├── src/
│   ├── main.ts                       # Entry point (port 3000, CORS enabled)
│   ├── app.module.ts                 # Root Application Module
│   ├── spark-sql/                    # Module truy xuất kết quả 6 truy vấn Spark SQL
│   │   ├── spark-sql.controller.ts
│   │   ├── spark-sql.service.ts
│   │   └── spark-sql.module.ts
│   ├── ml-analytics/                 # Module MLlib, K-Means & AI suy luận nguy cơ
│   │   ├── ml-analytics.controller.ts
│   │   ├── ml-analytics.service.ts
│   │   └── ml-analytics.module.ts
│   ├── streaming/                    # Module Kafka streaming & Cảnh báo 3 cấp độ
│   │   ├── streaming.controller.ts
│   │   ├── streaming.service.ts
│   │   └── streaming.module.ts
│   └── pipeline/                     # Module trạng thái Data Lake & Airflow DAG
│       ├── pipeline.controller.ts
│       ├── pipeline.service.ts
│       └── pipeline.module.ts
├── package.json
├── tsconfig.json
└── nest-cli.json
```

---

## 2. Hướng dẫn cài đặt và khởi chạy

### Bước 1: Cài đặt dependencies
```bash
cd backend-nestjs
npm install
```

### Bước 2: Chạy ở chế độ Development (Hot-reload)
```bash
npm run start:dev
```
Server sẽ khởi chạy tại: **http://localhost:3000**

---

## 3. Danh sách REST Endpoints cung cấp cho Web Client

| Phương thức | Đường dẫn API | Chức năng |
|---|---|---|
| `GET` | `/api/spark-sql/overview` | Lấy dữ liệu 6 truy vấn Spark SQL đa chiều & KPIs |
| `GET` | `/api/spark-sql/query/:id` | Lấy dữ liệu chi tiết của 1 truy vấn SQL (1 đến 6) |
| `GET` | `/api/ml/metrics` | Lấy chỉ số đánh giá Random Forest, Logistic Regression |
| `GET` | `/api/ml/kmeans` | Lấy kết quả phân cụm K-Means 4 nhóm nhân sự |
| `GET` | `/api/ml/risk-distribution` | Thống kê phân bổ nhân viên theo 3 cấp độ cảnh báo |
| `GET` | `/api/ml/high-risk-employees` | Danh sách Top nhân viên có nguy cơ nghỉ việc cao nhất |
| `POST`| `/api/ml/predict-risk` | AI suy luận rủi ro nghỉ việc tức thời từ form nhập liệu |
| `GET` | `/api/streaming/latest` | Lấy danh sách sự kiện Kafka Streaming thời gian thực |
| `POST`| `/api/streaming/simulate` | Phát sinh sự kiện streaming mới và chấm điểm AI tức thì |
| `GET` | `/api/pipeline/status` | Thông tin workspace, cấu trúc thư mục Data Lake HDFS |
| `GET` | `/api/pipeline/benchmark` | Số liệu benchmark nén Snappy Parquet vs CSV |
| `GET` | `/api/pipeline/airflow-dag` | Trạng thái điều phối và lịch chạy của Apache Airflow |
