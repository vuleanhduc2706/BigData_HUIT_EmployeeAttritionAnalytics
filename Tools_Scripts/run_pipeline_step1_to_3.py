"""
PIPELINE ĐIỀU PHỐI TỪ BƯỚC 1 ĐẾN BƯỚC 3
Thực hiện toàn diện:
  1. Chuẩn bị HDFS / Data Lake (Storage)
  2. Upload & Ingest dữ liệu nguồn (Ingestion)
  3. Đọc và suy luận Schema bằng Spark (Processing)
"""
import sys
import os
import time

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.step1_hdfs_prepare import prepare_storage
from src.step2_upload_ingest import upload_and_ingest
from src.step3_spark_read import spark_read_data

def run():
    start_time = time.time()
    print("=" * 70)
    print("      HE THONG PIPELINE DU LIEU LON (BIG DATA PIPELINE)")
    print("               THUC HIEN TU BUOC 1 DEN BUOC 3")
    print("=" * 70)
    
    # Bước 1
    prepare_storage()
    time.sleep(1)
    
    # Bước 2
    upload_and_ingest()
    time.sleep(1)
    
    # Bước 3
    spark_read_data()
    
    elapsed = time.time() - start_time
    print("=" * 70)
    print(f"[*] TAT CA 3 BUOC DA HOAN TAT THANH CONG trong {elapsed:.2f} giay!")
    print("=" * 70)

if __name__ == "__main__":
    run()
