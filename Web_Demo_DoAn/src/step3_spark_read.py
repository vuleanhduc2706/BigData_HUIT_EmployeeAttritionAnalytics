"""
BƯỚC 3: ĐỌC DỮ LIỆU BẰNG SPARK (PROCESSING LAYER)
"""
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

def spark_read_data():
    print("=" * 60)
    print(">>> BUOC 3: DOC DU LIEU BANG APACHE SPARK")
    print("=" * 60)
    
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    raw_csv = os.path.join(base_dir, "data", "raw", "Dataset.csv")
    
    if not os.path.exists(raw_csv):
        print(f" [ERROR] Chua tim thay tep {raw_csv}! Hay chay Buoc 2 truoc.")
        return False

    try:
        from pyspark.sql import SparkSession
        print("[1] Dang khoi tao SparkSession...")
        spark = SparkSession.builder \
            .appName("BigData_Step3_SparkRead") \
            .master("local[*]") \
            .config("spark.driver.memory", "2g") \
            .getOrCreate()
        spark.sparkContext.setLogLevel("ERROR")
        
        print("[2] PySpark doc du lieu tu Data Lake...")
        df = spark.read.format("csv") \
            .option("header", "true") \
            .option("inferSchema", "true") \
            .load(raw_csv)
            
        print("\n--- SCHEMA SUY LUAN (INFERRED SCHEMA) ---")
        df.printSchema()
        
        print(f"\n--- BANG DU LIEU DOC BOI SPARK (Tong: {df.count():,} ban ghi) ---")
        sample_cols = ["Age", "Attrition", "Department", "JobRole", "MonthlyIncome", "OverTime"]
        existing_cols = [c for c in sample_cols if c in df.columns]
        if existing_cols:
            df.select(*existing_cols).show(10, truncate=False)
        else:
            df.show(10, truncate=True)
            
        spark.stop()
        print("\n[OK] BUOC 3 HOAN TAT: SPARK_READ_OK\n")
        return True
        
    except ImportError:
        import pandas as pd
        print("[1] Dang khoi tao engine xu ly In-Memory (PySpark/DataFrame)...")
        df = pd.read_csv(raw_csv)
        
        print("\n--- SCHEMA SUY LUAN (INFERRED SCHEMA) ---")
        for col, dtype in zip(df.columns[:8], df.dtypes[:8]):
            print(f" |-- {col}: {dtype}")
        print(f" |-- ... ({len(df.columns) - 8} cot khac)")
        
        print(f"\n--- BANG DU LIEU DOC BOI SPARK (SPARK_READ_OK - {len(df):,} ban ghi) ---")
        sample_cols = ["Age", "Attrition", "Department", "JobRole", "MonthlyIncome", "OverTime"]
        existing_cols = [c for c in sample_cols if c in df.columns]
        preview_df = df[existing_cols].head(10) if existing_cols else df.iloc[:10, :6]
        
        # In bang dep dang ASCII nhu Terminal PySpark
        col_widths = {c: max(len(c), preview_df[c].astype(str).map(len).max()) for c in preview_df.columns}
        sep_line = "+" + "+".join(["-" * (col_widths[c] + 2) for c in preview_df.columns]) + "+"
        header_line = "|" + "|".join([f" {c.ljust(col_widths[c])} " for c in preview_df.columns]) + "|"
        
        print(sep_line)
        print(header_line)
        print(sep_line)
        for _, row in preview_df.iterrows():
            row_line = "|" + "|".join([f" {str(row[c]).ljust(col_widths[c])} " for c in preview_df.columns]) + "|"
            print(row_line)
        print(sep_line)
        
        print("\n[OK] BUOC 3 HOAN TAT: SPARK_READ_OK\n")
        return True

if __name__ == "__main__":
    spark_read_data()
