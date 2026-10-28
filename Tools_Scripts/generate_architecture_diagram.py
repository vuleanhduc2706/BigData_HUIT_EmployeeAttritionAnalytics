"""
Tạo sơ đồ kiến trúc tổng thể Big Data Lakehouse Medallion Pipeline
Sinh viên: Vũ Lê Anh Đức - MSSV: 2001230191
"""
import os
import sys
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_architecture_diagram():
    fig, ax = plt.subplots(figsize=(16, 9), dpi=300)
    fig.patch.set_facecolor('#0B0F19')
    ax.set_facecolor('#0B0F19')
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 9)
    ax.axis('off')

    # Title Banner
    ax.text(8.0, 8.55, "KIẾN TRÚC TỔNG THỂ HỆ THỐNG BIG DATA LAKEHOUSE MEDALLION & AI PREDICTION", 
            ha='center', va='center', color='#38BDF8', fontsize=16, fontweight='bold', family='sans-serif')
    ax.text(8.0, 8.22, "Học phần: Big Data & Ứng dụng | Đồ án: Phân tích & Dự đoán Nguy cơ Nghỉ việc Nhân sự (IBM HR Attrition)", 
            ha='center', va='center', color='#94A3B8', fontsize=11, family='sans-serif')
    ax.text(8.0, 7.95, "Sinh viên: Vũ Lê Anh Đức — MSSV: 2001230191 — HUIT 2026", 
            ha='center', va='center', color='#F59E0B', fontsize=10, fontweight='bold', family='sans-serif')

    # Columns / Layers
    # Layer 1: Sources (x=0.5 to 2.8)
    # Layer 2: Ingestion & Storage - HDFS (x=3.3 to 6.3)
    # Layer 3: Processing & Engine - PySpark (x=6.8 to 9.8)
    # Layer 4: Orchestration & Fault-Tolerance - Airflow (x=10.3 to 12.8)
    # Layer 5: Serving & Presentation - Flask Dashboard (x=13.3 to 15.6)

    def draw_box(x, y, w, h, bg_color, border_color, title, subtitle="", items=None, icon=""):
        rect = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.12",
                                      facecolor=bg_color, edgecolor=border_color, linewidth=1.8)
        ax.add_patch(rect)
        if title:
            ax.text(x + w/2, y + h - 0.28, title, ha='center', va='center', 
                    color=border_color, fontsize=10.5, fontweight='bold')
        if subtitle:
            ax.text(x + w/2, y + h - 0.52, subtitle, ha='center', va='center', 
                    color='#CBD5E1', fontsize=8.5, style='italic')
        if items:
            start_y = y + h - 0.8
            line_spacing = (h - 0.9) / max(len(items), 1)
            for i, it in enumerate(items):
                ax.text(x + 0.18, start_y - i * line_spacing, f"• {it}", ha='left', va='center', 
                        color='#E2E8F0', fontsize=8.2)

    # 1. SOURCES
    draw_box(0.4, 4.3, 2.5, 3.2, "#1E293B", "#38BDF8", "1. DATA SOURCES", "Nguồn dữ liệu đa cấu trúc", [
        "IBM HR Analytics Dataset",
        "1,470 bản ghi, 35 thuộc tính",
        "Định dạng: Batch CSV (222 KB)",
        "Tần suất: Định kỳ hàng ngày",
        "Kafka Realtime Event Stream",
        "Nhịp đập nhân sự 100-250ms",
        "Producer: Faker HR Simulator",
        "JSON payload: 12 attributes"
    ])

    # 2. HDFS MEDALLION LAKEHOUSE
    draw_box(3.3, 0.6, 3.2, 6.9, "#0F172A", "#10B981", "2. HDFS MEDALLION LAKEHOUSE", "Lưu trữ phân tán cụm Hadoop", [
        "[BRONZE TIER - Dữ liệu thô]",
        "Path: .../raw/Dataset.csv",
        "Size: 227,976 bytes (Zero-loss)",
        "Streaming Sink: Parquet realtime",
        "------------------------------------",
        "[SILVER TIER - Đã làm sạch & Gộp]",
        "Path: .../processed/hr_consolidated.parquet",
        "Size: 78,000 bytes (76 KB Snappy)",
        "Compaction: Single 78KB Block",
        "Giải quyết triệt để Small File",
        "Lược đồ chuẩn hóa: 34 cột",
        "------------------------------------",
        "[GOLD TIER - Dữ liệu nghiệp vụ]",
        "Path: .../output/high_risk_employees.csv",
        "Phân loại rủi ro 3 cấp cảnh báo",
        "Audit Log đối chiếu 1,470 dòng"
    ])

    # 3. APACHE SPARK PROCESSING & ML
    draw_box(7.0, 0.6, 3.3, 6.9, "#1E1E38", "#F59E0B", "3. DISTRIBUTED SPARK & ML", "Xử lý song song & Học máy", [
        "[PySpark 3.5 In-Memory ETL]",
        "SparkSession Master local[*]",
        "Schema casting & Null audit",
        "Drop 4 zero-variance cols",
        "Feature Engineering:",
        "  + Income_Per_WorkingYear",
        "  + Promotion_Lag_Ratio",
        "  + Attrition_Label (0/1)",
        "------------------------------------",
        "[Spark SQL 6 Truy vấn Đa chiều]",
        "Q1: OverTime (30.5% vs 10.4%)",
        "Q2: Department (Sales 20.6%)",
        "Q3: JobRole (Sales Rep 39.8%)",
        "Q4: WorkLifeBalance (L1 31.3%)",
        "Q5: Tenancy Tenure (<2y 34.9%)",
        "Q6: Manager Tenure Correlation",
        "------------------------------------",
        "[Machine Learning Lakehouse]",
        "K-Means Clustering (K=4 groups)",
        "Random Forest Tuned (Balanced)",
        "Accuracy: 83.33% | Recall: 64.09%",
        "ROC-AUC: 0.7963 | Latency: 12ms",
        "Model Artifact: hr_rf_model.pkl"
    ])

    # 4. AIRFLOW ORCHESTRATION
    draw_box(10.7, 3.5, 2.3, 4.0, "#1F2937", "#EC4899", "4. AIRFLOW DAG", "Điều phối tự động", [
        "DAG: hr_attrition_pipeline",
        "Schedule: @daily | Retries: 3",
        "t1: 1_hdfs_prepare",
        "t2: 2_upload_ingest",
        "t3: 3_spark_read",
        "t4: 4_clean_parquet_snappy",
        "t4b: 4b_compact_parquet",
        "t5: 5_spark_sql_analytics",
        "t6: 6_ml_tune_and_train",
        "t7: 7_save_results_hdfs",
        "t8: 8_kafka_stream_sink",
        "Fault-tolerance: Auto-retry"
    ])

    # 5. SERVING & PRESENTATION
    draw_box(13.4, 0.6, 2.3, 6.9, "#182234", "#60A5FA", "5. WEB DASHBOARD", "Flask Serving & UI", [
        "[Flask REST Server :5000]",
        "Tab 1: Pipeline E2E Monitor",
        "  (9 Steps, Status, Runtime)",
        "Tab 2: Spark SQL Insights",
        "  (6 Interactive Charts)",
        "Tab 3: ML Clusters & Metrics",
        "  (K=4, Matrix, ROC Curve)",
        "Tab 4: Kafka Live Ticker",
        "  (Realtime Stream events)",
        "Tab 5: AI Simulator",
        "  (Interactive Form /api/predict)",
        "  (Realtime RF Inference)",
        "Tab 6: Airflow & HDFS Health",
        "  (Cluster Benchmarks)"
    ])

    # Draw Arrows
    def draw_arrow(x1, y1, x2, y2, color="#94A3B8"):
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(facecolor=color, edgecolor=color, width=2, headwidth=8, headlength=8, shrink=0.05))

    # Sources -> HDFS
    draw_arrow(2.9, 5.8, 3.3, 5.8, "#38BDF8")
    # HDFS -> Spark
    draw_arrow(6.5, 4.2, 7.0, 4.2, "#10B981")
    # Spark -> HDFS (Gold tier writeback)
    draw_arrow(7.0, 1.8, 6.5, 1.8, "#F59E0B")
    # Airflow -> All (control line from top)
    draw_arrow(11.8, 3.5, 11.8, 1.8, "#EC4899")
    draw_arrow(11.8, 1.8, 10.3, 1.8, "#EC4899")
    # Spark & Gold -> Web Dashboard
    draw_arrow(10.3, 5.2, 13.4, 5.2, "#60A5FA")

    # Bottom Footer
    footer_text = "Hệ thống tuân thủ nghiêm ngặt mô hình Medallion Lakehouse chuẩn doanh nghiệp: Bronze (Raw HDFS) -> Silver (Parquet Snappy Compacted) -> Gold (Analytical Mart & Model Serving)"
    ax.text(8.0, 0.22, footer_text, ha='center', va='center', color='#64748B', fontsize=9, family='sans-serif')

    out_path = r"D:\Doan_BigData\BaoCao_Word\images\architecture_bigdata_medallion_pipeline.png"
    plt.tight_layout()
    plt.savefig(out_path, dpi=300, facecolor=fig.get_facecolor(), edgecolor='none', bbox_inches='tight')
    plt.close()
    print(f"[OK] Đã xuất thành công sơ đồ kiến trúc tại: {out_path} ({os.path.getsize(out_path)/1024:.2f} KB)")

if __name__ == "__main__":
    draw_architecture_diagram()
