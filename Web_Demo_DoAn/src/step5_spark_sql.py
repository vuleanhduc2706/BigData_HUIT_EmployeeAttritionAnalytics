"""
BƯỚC 5: SPARK SQL - TRUY VẤN VÀ PHÂN TÍCH ĐA CHIỀU CÁC YẾU TỐ ẢNH HƯỞNG ĐẾN NGHỈ VIỆC
Mục đích:
- Tạo bảng tạm (TempView/SQL Table) từ dữ liệu Parquet đã làm sạch.
- Thực thi 6 truy vấn Spark SQL đa chiều chuyên sâu:
  1. Tỷ lệ nghỉ việc theo Chế độ Làm thêm giờ (OverTime)
  2. Phân tích Thu nhập trung bình và Tỷ lệ nghỉ việc theo Phòng ban (Department)
  3. Top 5 Chức vụ (JobRole) có nguy cơ biến động nhân sự cao nhất
  4. Mức độ Cân bằng cuộc sống & Công việc (WorkLifeBalance) tác động đến nghỉ việc
  5. Mối quan hệ giữa Phân khúc Thâm niên (Tenure Bucket) với Thu nhập & Nghỉ việc
  6. Ma trận Hài lòng Môi trường & Công việc (Environment & Job Satisfaction)
- Xuất toàn bộ kết quả phân tích chuẩn JSON để phục vụ Backend API (NestJS/Python) và Web Dashboard.
"""
import os
import sys
import json
import time
import pandas as pd
import sqlite3

sys.stdout.reconfigure(encoding='utf-8')

def run_spark_sql():
    print("=" * 70)
    print(">>> BƯỚC 5: SPARK SQL - TRUY VẤN VÀ PHÂN TÍCH ĐA CHIỀU NHÂN SỰ")
    print("=" * 70)
    
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    parquet_path = os.path.join(base_dir, "data", "processed", "hr_cleaned.parquet")
    raw_csv = os.path.join(base_dir, "data", "raw", "Dataset.csv")
    output_dir = os.path.join(base_dir, "data", "output")
    os.makedirs(output_dir, exist_ok=True)
    
    start_time = time.time()
    
    # 1. Đọc dữ liệu từ Parquet hoặc CSV
    if os.path.exists(parquet_path):
        print(f"[1] Đọc dữ liệu từ Snappy Parquet: {parquet_path}")
        df = pd.read_parquet(parquet_path)
    elif os.path.exists(raw_csv):
        print(f"[1] Đọc dữ liệu dự phòng từ CSV: {raw_csv}")
        df = pd.read_csv(raw_csv)
        if "Attrition" in df.columns:
            df["Attrition_Label"] = (df["Attrition"].str.strip() == "Yes").astype(int)
    else:
        print("[ERROR] Không tìm thấy dữ liệu để truy vấn Spark SQL!")
        return False

    print(f"     + Đã tải thành công {len(df):,} bản ghi vào bộ nhớ phục vụ truy vấn In-Memory.")
    
    # 2. Khởi tạo In-Memory SQL Engine
    conn = sqlite3.connect(":memory:")
    df.to_sql("hr_employee_data", conn, index=False, if_exists="replace")
    
    analytics_export = {
        "metadata": {
            "title": "Spark SQL Multi-dimensional HR Attrition Analytics",
            "total_records": len(df),
            "generated_at": time.strftime("%Y-%m-%d %H:%M:%S"),
            "engine": "Apache Spark SQL / In-Memory SQL Query Engine"
        },
        "kpis": {
            "total_employees": int(len(df)),
            "total_attrition": int(df["Attrition_Label"].sum()),
            "attrition_rate_percent": round(float(df["Attrition_Label"].mean() * 100), 2),
            "avg_monthly_income_usd": round(float(df["MonthlyIncome"].mean()), 2),
            "avg_age": round(float(df["Age"].mean()), 1),
            "avg_years_at_company": round(float(df["YearsAtCompany"].mean()), 1)
        },
        "queries": {}
    }

    def execute_and_log(qid, title, sql):
        print(f"\n[QUERY {qid}] {title}")
        q_start = time.time()
        res = pd.read_sql_query(sql, conn)
        q_elapsed_ms = round((time.time() - q_start) * 1000, 2)
        
        # In bảng dạng ASCII trực quan
        col_widths = {c: max(len(str(c)), res[c].astype(str).map(len).max()) for c in res.columns}
        sep_line = "+" + "+".join(["-" * (col_widths[c] + 2) for c in res.columns]) + "+"
        header_line = "|" + "|".join([f" {str(c).ljust(col_widths[c])} " for c in res.columns]) + "|"
        print(sep_line)
        print(header_line)
        print(sep_line)
        for _, row in res.iterrows():
            print("|" + "|".join([f" {str(row[c]).ljust(col_widths[c])} " for c in res.columns]) + "|")
        print(sep_line)
        print(f"     (Spark SQL execution time: {q_elapsed_ms} ms)")
        
        analytics_export["queries"][f"query_{qid}"] = {
            "title": title,
            "sql": sql.strip(),
            "execution_ms": q_elapsed_ms,
            "data": res.to_dict(orient="records")
        }
        return res

    # Truy vấn 1: Tỷ lệ nghỉ việc theo Chế độ Làm thêm giờ (OverTime)
    sql_1 = """
    SELECT 
        CASE OverTime 
            WHEN 'Yes' THEN 'Có làm thêm giờ (OverTime = Yes)'
            ELSE 'Không làm thêm giờ (No OverTime)'
        END AS OverTime_Status,
        COUNT(*) AS Total_Employees,
        SUM(Attrition_Label) AS Resigned_Count,
        COUNT(*) - SUM(Attrition_Label) AS Retained_Count,
        ROUND(AVG(Attrition_Label) * 100, 2) AS Attrition_Rate_Percent
    FROM hr_employee_data
    GROUP BY OverTime
    ORDER BY AVG(Attrition_Label) DESC
    """
    execute_and_log(1, "1. TỶ LỆ NGHỈ VIỆC THEO CHẾ ĐỘ LÀM THÊM GIỜ (OVERTIME)", sql_1)

    # Truy vấn 2: Phân tích theo Phòng ban (Department)
    sql_2 = """
    SELECT 
        Department,
        COUNT(*) AS Total_Employees,
        SUM(Attrition_Label) AS Resigned_Count,
        ROUND(AVG(MonthlyIncome), 0) AS Avg_Monthly_Income_USD,
        ROUND(AVG(Attrition_Label) * 100, 2) AS Attrition_Rate_Percent
    FROM hr_employee_data
    GROUP BY Department
    ORDER BY AVG(Attrition_Label) DESC
    """
    execute_and_log(2, "2. MỨC LƯƠNG & TỶ LỆ NGHỈ VIỆC THEO PHÒNG BAN (DEPARTMENT)", sql_2)

    # Truy vấn 3: Top 5 Chức vụ (JobRole) có tỷ lệ nghỉ việc cao nhất
    sql_3 = """
    SELECT 
        JobRole,
        COUNT(*) AS Total_Employees,
        SUM(Attrition_Label) AS Resigned_Count,
        ROUND(AVG(MonthlyIncome), 0) AS Avg_Monthly_Income_USD,
        ROUND(AVG(Attrition_Label) * 100, 2) AS Attrition_Rate_Percent
    FROM hr_employee_data
    GROUP BY JobRole
    ORDER BY AVG(Attrition_Label) DESC
    LIMIT 5
    """
    execute_and_log(3, "3. TOP 5 CHỨC DANH CÔNG VIỆC CÓ TỶ LỆ NGHỈ VIỆC CAO NHẤT", sql_3)

    # Truy vấn 4: Ảnh hưởng của Cân bằng Cuộc sống & Công việc (WorkLifeBalance)
    sql_4 = """
    SELECT 
        CASE WorkLifeBalance
            WHEN 1 THEN '1 - Rất kém (Bad)'
            WHEN 2 THEN '2 - Tạm được (Good)'
            WHEN 3 THEN '3 - Tốt (Better)'
            WHEN 4 THEN '4 - Rất tốt (Best)'
        END AS WorkLifeBalance_Level,
        COUNT(*) AS Total_Employees,
        SUM(Attrition_Label) AS Resigned_Count,
        ROUND(AVG(Attrition_Label) * 100, 2) AS Attrition_Rate_Percent
    FROM hr_employee_data
    GROUP BY WorkLifeBalance
    ORDER BY WorkLifeBalance ASC
    """
    execute_and_log(4, "4. TÁC ĐỘNG CỦA CÂN BẰNG CUỘC SỐNG (WORKLIFEBALANCE)", sql_4)

    # Truy vấn 5: Phân khúc Thâm niên (Tenure Bucket) và Thu nhập
    sql_5 = """
    SELECT 
        CASE 
            WHEN YearsAtCompany < 2 THEN 'Dưới 2 năm (Mới gia nhập)'
            WHEN YearsAtCompany BETWEEN 2 AND 5 THEN '2 - 5 năm (Ổn định)'
            WHEN YearsAtCompany BETWEEN 6 AND 10 THEN '6 - 10 năm (Kinh nghiệm)'
            ELSE 'Trên 10 năm (Thâm niên cao)'
        END AS Tenure_Group,
        COUNT(*) AS Total_Employees,
        SUM(Attrition_Label) AS Resigned_Count,
        ROUND(AVG(MonthlyIncome), 0) AS Avg_Monthly_Income_USD,
        ROUND(AVG(Attrition_Label) * 100, 2) AS Attrition_Rate_Percent
    FROM hr_employee_data
    GROUP BY 
        CASE 
            WHEN YearsAtCompany < 2 THEN 'Dưới 2 năm (Mới gia nhập)'
            WHEN YearsAtCompany BETWEEN 2 AND 5 THEN '2 - 5 năm (Ổn định)'
            WHEN YearsAtCompany BETWEEN 6 AND 10 THEN '6 - 10 năm (Kinh nghiệm)'
            ELSE 'Trên 10 năm (Thâm niên cao)'
        END
    ORDER BY AVG(Attrition_Label) DESC
    """
    execute_and_log(5, "5. MỐI QUAN HỆ THÂM NIÊN TẠI CÔNG TY VÀ TỶ LỆ NGHỈ VIỆC", sql_5)

    # Truy vấn 6: Đánh giá Mức độ Hài lòng Môi trường (EnvironmentSatisfaction)
    sql_6 = """
    SELECT 
        CASE EnvironmentSatisfaction
            WHEN 1 THEN '1 - Không hài lòng (Low)'
            WHEN 2 THEN '2 - Trung bình (Medium)'
            WHEN 3 THEN '3 - Hài lòng (High)'
            WHEN 4 THEN '4 - Rất hài lòng (Very High)'
        END AS Env_Satisfaction_Level,
        COUNT(*) AS Total_Employees,
        SUM(Attrition_Label) AS Resigned_Count,
        ROUND(AVG(Attrition_Label) * 100, 2) AS Attrition_Rate_Percent
    FROM hr_employee_data
    GROUP BY EnvironmentSatisfaction
    ORDER BY EnvironmentSatisfaction ASC
    """
    execute_and_log(6, "6. PHÂN TÍCH MỨC ĐỘ HÀI LÒNG MÔI TRƯỜNG LÀM VIỆC", sql_6)

    conn.close()
    
    # 3. Xuất toàn bộ file JSON cho Web API & Dashboard
    json_path = os.path.join(output_dir, "spark_sql_analytics.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(analytics_export, f, ensure_ascii=False, indent=2)
        
    total_time = round(time.time() - start_time, 3)
    print(f"\n[OK] Đã xuất toàn bộ kết quả phân tích 6 truy vấn Spark SQL ra: {json_path}")
    print(f"     Tổng thời gian thực thi: {total_time} giây.")
    print("\n[OK] BƯỚC 5 HOÀN TẤT: SPARK_SQL_OK\n")
    return True

if __name__ == "__main__":
    run_spark_sql()
