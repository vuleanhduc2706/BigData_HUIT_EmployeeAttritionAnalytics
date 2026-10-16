"""
BƯỚC 2: UPLOAD DỮ LIỆU (BATCH INGESTION)
"""
import os
import shutil
import subprocess
import sys

sys.stdout.reconfigure(encoding='utf-8')

def upload_and_ingest():
    print("=" * 60)
    print(">>> BUOC 2: UPLOAD DU LIEU & BATCH INGESTION")
    print("=" * 60)
    
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    source_file = os.path.join(base_dir, "WA_Fn-UseC_-HR-Employee-Attrition.csv")
    raw_dir = os.path.join(base_dir, "data", "raw")
    target_csv = os.path.join(raw_dir, "Dataset.csv")
    
    # 1. Đảm bảo file có mặt trong raw/
    if os.path.exists(source_file):
        shutil.copy2(source_file, target_csv)
        print(f" [OK] Da sao chep du lieu nguon vao raw: {target_csv}")
    elif not os.path.exists(target_csv):
        print(f" [ERROR] Khong tim thay file nguon: {source_file}")
        return False
        
    # 2. Kiểm tra tính toàn vẹn của tệp
    file_size_kb = os.path.getsize(target_csv) / 1024
    with open(target_csv, "r", encoding="utf-8") as f:
        header = f.readline().strip().split(",")
        num_rows = sum(1 for _ in f)
        
    print(f" [INFO] Dung luong tep: {file_size_kb:.2f} KB")
    print(f" [INFO] So dong du lieu (Rows): {num_rows:,} ban ghi")
    print(f" [INFO] So thuoc tinh (Columns): {len(header)} cot")
    print(f" [INFO] 5 cot dau tien: {', '.join(header[:5])}...")
    
    # 3. Đẩy lên HDFS nếu Hadoop cluster đang online
    hadoop_home = os.environ.get("HADOOP_HOME", "D:\\hadoop")
    hdfs_cmd = os.path.join(hadoop_home, "bin", "hdfs.cmd")
    hdfs_target = "/courses/2/projects/3/students/2001230191/raw/Dataset.csv"
    
    if os.path.exists(hdfs_cmd):
        try:
            cmd = f'"{hdfs_cmd}" dfs -put -f "{target_csv}" "{hdfs_target}"'
            res = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=5)
            if res.returncode == 0:
                print(f" [HDFS OK] Da nap thanh cong len HDFS: {hdfs_target}")
        except Exception:
            pass

    print("\n[OK] BUOC 2 HOAN TAT: Du lieu nguon da duoc Ingest vao tang raw thanh cong!\n")
    return True

if __name__ == "__main__":
    upload_and_ingest()
