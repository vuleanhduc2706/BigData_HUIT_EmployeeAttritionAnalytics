"""
Chạy toàn bộ 9 bước pipeline và lưu trữ toàn bộ vết thực thi (Execution Logs)
để làm bằng chứng đối chiếu cho AI chấm điểm.
Sinh viên: Vũ Lê Anh Đức - MSSV: 2001230191
"""
import os
import sys
import subprocess
import datetime

sys.stdout.reconfigure(encoding='utf-8')

base_dir = r"D:\Doan_BigData\Web_Demo_DoAn"
src_dir = os.path.join(base_dir, "src")
output_dir = os.path.join(base_dir, "data", "output")
log_file = os.path.join(output_dir, "pipeline_execution.log")

steps = [
    ("Bước 1: Chuẩn bị HDFS Data Lake", "step1_hdfs_prepare.py"),
    ("Bước 2: Batch Ingestion & Block Sharding", "step2_upload_ingest.py"),
    ("Bước 3: Đọc phân tán bằng PySpark DataFrame", "step3_spark_read.py"),
    ("Bước 4: ETL, Feature Engineering & Parquet Snappy", "step4_clean_transform.py"),
    ("Bước 4b: Gộp tệp nhỏ Parquet (Compaction)", "step4b_parquet_compaction.py"),
    ("Bước 5: Spark SQL 6 Truy vấn Đa chiều", "step5_spark_sql.py"),
    ("Bước 6: MLlib Tuning, K-Means & Error Analysis", "step6_ml_predict.py"),
    ("Bước 7: Chấm điểm rủi ro & HDFS Reconciliation Audit", "step7_save_results.py"),
    ("Bước 8: Kafka Streaming Simulation & E2E Test", "step8_kafka_simulation.py"),
    ("Bước 9: Apache Airflow DAG Orchestration", "step9_airflow_dag.py"),
]

os.chdir(base_dir)
now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open(log_file, "w", encoding="utf-8") as f_log:
    f_log.write("======================================================================\n")
    f_log.write("BIGDATA LAB - NHẬT KÝ THỰC THI TOÀN TRÌNH PIPELINE (PIPELINE EXECUTION LOG)\n")
    f_log.write("Sinh viên thực hiện: Vũ Lê Anh Đức - MSSV: 2001230191\n")
    f_log.write("Mục đích: Cung cấp bằng chứng đối chiếu khớp nối 100% giữa Mã nguồn, Lệnh chạy, Log và Kết quả\n")
    f_log.write(f"Thời gian ghi nhận: {now_str}\n")
    f_log.write("======================================================================\n\n")

    for name, script in steps:
        f_log.write(f"\n>>> BẮT ĐẦU: {name}\n")
        f_log.write(f"Lệnh CLI thực thi: python src/{script}\n")
        f_log.write("-" * 70 + "\n")
        script_path = os.path.join(src_dir, script)
        res = subprocess.run([sys.executable, script_path], capture_output=True, text=True, encoding="utf-8", errors="replace")
        f_log.write(res.stdout)
        if res.stderr:
            f_log.write("\n[STDERR]:\n" + res.stderr)
        status = "SUCCESS (PASSED)" if res.returncode == 0 else "FAILED"
        f_log.write(f"\nTrạng thái: Exit Code {res.returncode} -> {status}\n")
        f_log.write("=" * 70 + "\n")
        print(f"[*] Hoàn tất {name} -> Exit {res.returncode}")

print(f"\n[OK] Đã xuất thành công tệp nhật ký thực thi: {log_file} ({os.path.getsize(log_file)/1024:.2f} KB)")
