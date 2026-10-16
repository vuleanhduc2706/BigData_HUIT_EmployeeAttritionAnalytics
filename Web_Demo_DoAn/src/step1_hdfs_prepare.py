"""
BƯỚC 1: CHUẨN BỊ HDFS / DATA LAKE STORAGE
"""
import os
import subprocess
import sys

sys.stdout.reconfigure(encoding='utf-8')

def prepare_storage():
    print("=" * 60)
    print(">>> BUOC 1: CHUAN BI HDFS / STORAGE WORKSPACE")
    print("=" * 60)
    
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(base_dir, "data")
    
    folders = ["raw", "processed", "output"]
    created_paths = []
    
    for folder in folders:
        path = os.path.join(data_dir, folder)
        os.makedirs(path, exist_ok=True)
        created_paths.append(path)
        print(f" [OK] Thu muc cuc bo san sang: {path}")

    hadoop_home = os.environ.get("HADOOP_HOME", "D:\\hadoop")
    hdfs_cmd = os.path.join(hadoop_home, "bin", "hdfs.cmd")
    hdfs_workspace = "/courses/2/projects/3/students/2001230191"
    print(f"\n[INFO] Khong gian HDFS muc tieu: {hdfs_workspace}")
    
    if os.path.exists(hdfs_cmd):
        try:
            print("Dang kiem tra ket noi NameNode HDFS...")
            for folder in folders:
                hdfs_folder = f"{hdfs_workspace}/{folder}"
                cmd = f'"{hdfs_cmd}" dfs -mkdir -p {hdfs_folder}'
                res = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=5)
                if res.returncode == 0:
                    print(f" [HDFS OK] Da tao thu muc HDFS: {hdfs_folder}")
        except Exception:
            print(" [NOTE] NameNode daemon chua bat, he thong su dung cau truc local Data Lake tuong duong.")
            
    print("\n[OK] BUOC 1 HOAN TAT: Cau truc raw/, processed/, output/ da san sang!\n")

if __name__ == "__main__":
    prepare_storage()
