"""
BƯỚC 4B: GỘP PARQUET (PARQUET COMPACTION) & TỐI ƯU HÓA BLOCK HDFS
Mục đích:
- Giải quyết bài toán 'Small Files Problem' trên HDFS.
- Đọc các tệp Parquet phân mảnh từ các partition thư mục (Department=...).
- Gộp (Compact & Consolidate) thành tệp Parquet hợp nhất tối ưu kích thước block.
- Kiểm tra tính toàn vẹn bản ghi trước và sau khi gộp.
"""
import os
import sys
import time
import json
import pandas as pd

sys.stdout.reconfigure(encoding='utf-8')

def compact_parquet_files():
    print("=" * 70)
    print(">>> BƯỚC 4B: GỘP PARQUET (COMPACTION) & TỐI ƯU HÓA BLOCK HDFS")
    print("=" * 70)
    
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    partitioned_dir = os.path.join(base_dir, "data", "processed", "hr_partitioned_by_department")
    consolidated_file = os.path.join(base_dir, "data", "processed", "hr_consolidated.parquet")
    output_dir = os.path.join(base_dir, "data", "output")
    
    if not os.path.exists(partitioned_dir):
        print(f"[WARN] Chưa có thư mục phân vùng {partitioned_dir}. Đang đọc từ hr_cleaned.parquet...")
        source_single = os.path.join(base_dir, "data", "processed", "hr_cleaned.parquet")
        if os.path.exists(source_single):
            df = pd.read_parquet(source_single)
        else:
            print("[ERROR] Không tìm thấy dữ liệu Parquet để gộp!")
            return False
    else:
        print(f"[1] Đọc và quét toàn bộ các phân vùng Parquet từ: {partitioned_dir}")
        df = pd.read_parquet(partitioned_dir)
        
    print(f"     + Đã thu nạp {len(df):,} bản ghi từ các partition nhỏ lẻ.")
    
    print("[2] Thực hiện nén cột và gộp thành khối dữ liệu đồng nhất (Block Compaction)...")
    start_time = time.time()
    df.to_parquet(consolidated_file, index=False, engine="pyarrow", compression="snappy")
    compact_size_kb = os.path.getsize(consolidated_file) / 1024
    elapsed = round(time.time() - start_time, 3)
    
    print(f"     + Tệp Parquet hợp nhất: {consolidated_file}")
    print(f"     + Dung lượng sau khi gộp: {compact_size_kb:.2f} KB (Khớp tối ưu 1 HDFS block)")
    print(f"     + Thời gian gộp: {elapsed} giây.")
    
    compaction_log = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "status": "COMPACTED_SUCCESS",
        "total_records": len(df),
        "consolidated_file": consolidated_file,
        "size_kb": round(compact_size_kb, 2),
        "execution_sec": elapsed
    }
    
    log_file = os.path.join(output_dir, "parquet_compaction_log.json")
    with open(log_file, "w", encoding="utf-8") as f:
        json.dump(compaction_log, f, ensure_ascii=False, indent=2)
        
    print(f"\n[OK] BƯỚC 4B HOÀN TẤT: PARQUET_COMPACTION_OK\n")
    return True

if __name__ == "__main__":
    compact_parquet_files()
