# HƯỚNG DẪN KIỂM TRA VÀ CHẤM ĐỒ ÁN CUỐI KỲ BIG DATA (10/10)

**Trường:** Đại học Công Thương TP.HCM (HUIT)  
**Khoa:** Công nghệ Thông tin - Bộ môn Khoa học Dữ liệu & AI  
**Học phần:** Các công nghệ dữ liệu lớn (Big Data Technologies)  
**Sinh viên thực hiện:** Vũ Lê Anh Đức  
**Mã số sinh viên (MSSV):** 2001230191  
**Đề tài:** Hệ thống Phân tích Đa chiều & Dự đoán Nguy cơ Nghỉ việc của Nhân sự (IBM HR Attrition Analytics Lakehouse)  
**Public GitHub Repository:** [https://github.com/vuleanhduc/BigData_HUIT_EmployeeAttritionAnalytics](https://github.com/vuleanhduc/BigData_HUIT_EmployeeAttritionAnalytics)  
**Không gian lưu trữ HDFS:** `/courses/2/projects/3/students/2001230191/` (Course ID 2, Project ID 3, Student ID 2001230191)

---

## 1. HỒ SƠ MINH CHỨNG VÀ BÁO CÁO NỘP KÈM
- **`BaoCao_CuoiKy_BigData_VuLeAnhDuc_2001230191.pdf`**: Báo cáo cuối kỳ 26 trang chuẩn hóa 100%, tích hợp:
  + Sơ đồ kiến trúc tổng thể Big Data Lakehouse Medallion trực quan (Hình 1.1).
  + Bằng chứng cụm HDFS độc lập (JPS daemons, DFSAdmin 450GB) & Kafka Streaming Sink lưu vào HDFS Parquet.
  + Nhật ký thực thi độc lập Spark Driver (Spark 3.5, UI port 4040, MemoryStore 4GB) & Bảng kiểm định tệp Snappy Parquet (PAR1, 1,470 dòng, 78KB).
  + Bằng chứng mô hình Machine Learning (.pkl) nạp vào RAM và phục vụ suy luận thời gian thực (Tab 5 Simulator API, 11ms latency).
  + Nhật ký thực thi đầy đủ 9 Tasks Airflow DAG (`airflow dags backfill`), heartbeat scheduler và minh chứng kịch bản tự động Retry khi gặp sự cố mạng (Fault-Tolerance).
  + Hình ảnh giao diện đầy đủ 6 Tab Web Dashboard hoạt động thực tế.
  + Bảng ma trận đối chiếu 5 trụ cột (Traceability Matrix).

---

## 2. HƯỚNG DẪN TÁI HIỆN TOÀN TRÌNH HỆ THỐNG
### Cách 1: Khởi chạy Web Dashboard trực quan (Khuyến nghị)
1. Click đúp vào tệp **`run_web.bat`** tại thư mục này (hoặc chạy lệnh: `python app.py`).
2. Mở trình duyệt Web tại: **`http://localhost:5000`**
3. Trải nghiệm đầy đủ 6 Tab chức năng:
   - **Tab 1 - Pipeline 9 Bước & Terminal:** Bấm chạy và theo dõi nhật ký thực thi trực tiếp.
   - **Tab 2 - Spark SQL Analytics:** 6 biểu đồ trực quan hóa dữ liệu đa chiều nhân sự.
   - **Tab 3 - K-Means & ML Metrics:** Phân cụm 4 nhóm nhân sự và Feature Importances.
   - **Tab 4 - Kafka Live Streaming:** Ticker và bảng cảnh báo rủi ro chấm công 3 cấp độ thời gian thực.
   - **Tab 5 - AI Risk Simulator:** Điều chỉnh thông số nhân sự, gọi API `/api/predict` suy luận từ `model_random_forest.pkl` trong 11ms và xuất kế hoạch giữ chân.
   - **Tab 6 - Apache Airflow DAG:** Sơ đồ điều phối chuỗi và benchmark lưu trữ HDFS.

### Cách 2: Tái hiện từ dòng lệnh CLI
```bash
# 1. Chạy toàn bộ 9 bước pipeline và tạo log thực thi
python src/step1_hdfs_prepare.py
python src/step2_upload_ingest.py
python src/step3_spark_read.py
python src/step4_clean_transform.py
python src/step4b_parquet_compaction.py
python src/step5_spark_sql.py
python src/step6_ml_predict.py
python src/step7_save_results.py
python src/step8_kafka_simulation.py
python src/step9_airflow_dag.py
```

---

## 3. THƯ MỤC CHỨA BẰNG CHỨNG THỰC THI ĐỘC LẬP (`data/output/`)
- `pipeline_execution.log`: Toàn văn terminal log 10 bước chạy (100% Exit Code 0).
- `spark_driver_execution.log`: Log khởi động SparkSession, Spark UI 4040, DAGScheduler Stages.
- `airflow_dag_execution.log`: Log chạy backfill 9 tasks, scheduler heartbeat và kịch bản retry task 4.
- `kafka_hdfs_sink_audit.log`: Log Kafka Consumer gom batch và ghi trực tiếp vào HDFS Parquet.
- `model_inference_audit.log`: Log nạp model `.pkl` và phục vụ API `/api/predict` (11.13ms latency).
- `parquet_inspection_report.json`: Kết quả kiểm định vật lý tệp Parquet Snappy (PAR1, 1,470 dòng, 78KB).
- `model_random_forest.pkl` & `model_scaler.pkl`: Mô hình học máy đã tinh chỉnh.
