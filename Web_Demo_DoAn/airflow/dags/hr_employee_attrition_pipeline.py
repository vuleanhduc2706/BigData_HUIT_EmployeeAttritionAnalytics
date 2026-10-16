"""
DAG: hr_employee_attrition_pipeline
Mục đích: Tự động hóa toàn trình thu thập, xử lý, gộp Parquet, Spark SQL, K-Means & Random Forest dự đoán nguy cơ nghỉ việc
"""
import os
import sys

# Thiết lập UTF-8 cho Windows console
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# Đảm bảo nạp đúng module airflow trên cả môi trường Windows và Docker/Linux
_CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
_AIRFLOW_PARENT = os.path.dirname(os.path.dirname(_CURRENT_DIR))
if _AIRFLOW_PARENT not in sys.path:
    sys.path.insert(0, _AIRFLOW_PARENT)
_SRC_DIR = os.path.join(_AIRFLOW_PARENT, "src").replace("\\", "/")

from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'VuLeAnhDuc_2001230191',
    'depends_on_past': False,
    'start_date': datetime(2026, 1, 1),
    'email': ['anhduc.vule@huit.edu.vn'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'hr_employee_attrition_pipeline',
    default_args=default_args,
    description='Pipeline tu dong hoa du doan nguy co nghi viec nhan vien',
    schedule_interval='@daily',
    catchup=False,
    tags=['bigdata', 'hdfs', 'pyspark', 'parquet_compaction', 'spark_sql', 'ml_tuning', 'kafka']
) as dag:

    t1_hdfs_prep = BashOperator(
        task_id='1_hdfs_prepare',
        bash_command=f'python "{_SRC_DIR}/step1_hdfs_prepare.py"',
        execution_timeout=timedelta(minutes=5)
    )

    t2_upload = BashOperator(
        task_id='2_upload_ingest',
        bash_command=f'python "{_SRC_DIR}/step2_upload_ingest.py"',
        execution_timeout=timedelta(minutes=5)
    )

    t3_spark_read = BashOperator(
        task_id='3_spark_read',
        bash_command=f'python "{_SRC_DIR}/step3_spark_read.py"',
        execution_timeout=timedelta(minutes=10)
    )

    t4_clean_parquet = BashOperator(
        task_id='4_clean_parquet_snappy',
        bash_command=f'python "{_SRC_DIR}/step4_clean_transform.py"',
        execution_timeout=timedelta(minutes=10)
    )

    t4b_compact_parquet = BashOperator(
        task_id='4b_compact_parquet_files',
        bash_command=f'python "{_SRC_DIR}/step4b_parquet_compaction.py"',
        execution_timeout=timedelta(minutes=5)
    )

    t5_spark_sql = BashOperator(
        task_id='5_spark_sql_analytics',
        bash_command=f'python "{_SRC_DIR}/step5_spark_sql.py"',
        execution_timeout=timedelta(minutes=10)
    )

    t6_ml_predict = BashOperator(
        task_id='6_ml_tune_and_train',
        bash_command=f'python "{_SRC_DIR}/step6_ml_predict.py"',
        execution_timeout=timedelta(minutes=15)
    )

    t7_save_results = BashOperator(
        task_id='7_save_results_hdfs',
        bash_command=f'python "{_SRC_DIR}/step7_save_results.py"',
        execution_timeout=timedelta(minutes=5)
    )

    t8_kafka_stream = BashOperator(
        task_id='8_kafka_streaming_health',
        bash_command=f'python "{_SRC_DIR}/step8_kafka_simulation.py"',
        execution_timeout=timedelta(minutes=5)
    )

    # Thiet lap thu tu dependencies
    t1_hdfs_prep >> t2_upload >> t3_spark_read >> t4_clean_parquet >> t4b_compact_parquet >> t5_spark_sql >> t6_ml_predict >> t7_save_results >> t8_kafka_stream

if __name__ == "__main__":
    print("=" * 70)
    print(">>> KIỂM TRA TÍNH TOÀN VẸN CÚ PHÁP AIRFLOW DAG THÀNH CÔNG")
    print(f"    DAG ID: {dag.dag_id}")
    print(f"    Lịch trình: {dag.schedule_interval} | Tags: {dag.tags}")
    print("    Chuỗi 9 Tasks: t1 >> t2 >> t3 >> t4 >> t4b >> t5 >> t6 >> t7 >> t8: OK")
    print("=" * 70)
