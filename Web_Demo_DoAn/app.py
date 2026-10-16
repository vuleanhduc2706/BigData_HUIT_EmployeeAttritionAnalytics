import os
import sys
import subprocess
import json
import time
import random
from flask import Flask, render_template, jsonify, request

sys.stdout.reconfigure(encoding='utf-8')

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
SRC_DIR = os.path.join(BASE_DIR, "src")
OUTPUT_DIR = os.path.join(DATA_DIR, "output")

# Danh sách 9 bước Pipeline
STAGE_SCRIPTS = {
    "hdfs_prepare": ("step1_hdfs_prepare.py", "1. Chuẩn bị HDFS"),
    "upload_data": ("step2_upload_ingest.py", "2. Upload dữ liệu"),
    "spark_read": ("step3_spark_read.py", "3. Đọc bằng Spark"),
    "spark_clean": ("step4_clean_transform.py", "4. Làm sạch dữ liệu"),
    "spark_sql": ("step5_spark_sql.py", "5. Spark SQL"),
    "ml_predict": ("step6_ml_predict.py", "6. MLlib Dự đoán"),
    "save_results": ("step7_save_results.py", "7. Lưu kết quả"),
    "kafka_stream": ("step8_kafka_simulation.py", "8. Kafka Ingest"),
    "airflow_dag": ("step9_airflow_dag.py", "9. Airflow DAG")
}

# Lưu trạng thái hoàn thành của từng bước
step_status = {stage: True for stage in STAGE_SCRIPTS}

def read_json_file(filename, default=None):
    if default is None:
        default = {}
    filepath = os.path.join(OUTPUT_DIR, filename)
    if os.path.exists(filepath):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return default
    return default

def get_folder_info():
    info = {}
    for sub in ["raw", "processed", "output"]:
        p = os.path.join(DATA_DIR, sub)
        if os.path.exists(p):
            files = os.listdir(p)
            size_kb = sum(os.path.getsize(os.path.join(p, f)) for f in files if os.path.isfile(os.path.join(p, f))) / 1024
            info[sub] = {"files": files, "count": len(files), "size_kb": round(size_kb, 1)}
        else:
            info[sub] = {"files": [], "count": 0, "size_kb": 0}
    return info

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/status", methods=["GET"])
def api_status():
    return jsonify({
        "student": {
            "name": "Vũ Lê Anh Đức",
            "role": "Học viên",
            "id": "2001230191",
            "workspace": "/courses/2/projects/3/students/2001230191"
        },
        "hadoop": {
            "version": "Hadoop 3.4.0 (Windows Native with WinUtils)",
            "status": "BigData Core sẵn sàng",
            "cluster": "5 DataNodes (7 blocks WORM, Replication=2)",
            "home": os.environ.get("HADOOP_HOME", "D:\\hadoop")
        },
        "steps": step_status,
        "folders": get_folder_info(),
        "storageBenchmark": read_json_file("storage_benchmark.json")
    })

@app.route("/api/run-stage/<stage_name>", methods=["POST"])
def api_run_stage(stage_name):
    stage_key = stage_name.strip().lower()
    
    aliases = {
        "1": "hdfs_prepare", "hdfs": "hdfs_prepare",
        "2": "upload_data", "upload": "upload_data",
        "3": "spark_read", "read": "spark_read",
        "4": "spark_clean", "clean": "spark_clean",
        "5": "spark_sql", "sql": "spark_sql",
        "6": "ml_predict", "rfm_kmeans": "ml_predict", "ml": "ml_predict",
        "7": "save_results", "save": "save_results",
        "8": "kafka_stream", "kafka": "kafka_stream",
        "9": "airflow_dag", "airflow": "airflow_dag"
    }
    stage_key = aliases.get(stage_key, stage_key)
    
    if stage_key not in STAGE_SCRIPTS:
        return jsonify({
            "success": False,
            "stage": stage_name,
            "output": f"[ERROR] Không tìm thấy stage '{stage_name}'.\nGõ 'help' để xem danh sách các stage hỗ trợ."
        }), 400
        
    script_file, display_name = STAGE_SCRIPTS[stage_key]
    script_path = os.path.join(SRC_DIR, script_file)
    
    if not os.path.exists(script_path):
        return jsonify({
            "success": False,
            "stage": stage_key,
            "output": f"[ERROR] Không tìm thấy file script: {script_path}"
        }), 404
        
    try:
        res = subprocess.run(
            [sys.executable, script_path],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=60
        )
        output = res.stdout + ("\n[STDERR]:\n" + res.stderr if res.stderr else "")
        step_status[stage_key] = (res.returncode == 0)
        
        return jsonify({
            "success": res.returncode == 0,
            "stage": stage_key,
            "display_name": display_name,
            "output": output,
            "steps": step_status,
            "folders": get_folder_info()
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "stage": stage_key,
            "output": f"[EXCEPTION]: {str(e)}"
        }), 500

@app.route("/api/run-all", methods=["POST"])
def api_run_all():
    full_output = []
    has_error = False
    
    for stage_key, (script_file, display_name) in STAGE_SCRIPTS.items():
        script_path = os.path.join(SRC_DIR, script_file)
        try:
            res = subprocess.run(
                [sys.executable, script_path],
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                timeout=60
            )
            step_status[stage_key] = (res.returncode == 0)
            full_output.append(f"$ run-stage {stage_key}\n" + res.stdout)
            if res.returncode != 0:
                has_error = True
                if res.stderr:
                    full_output.append(f"[STDERR]: {res.stderr}\n")
                break
        except Exception as e:
            has_error = True
            full_output.append(f"[ERROR]: {str(e)}\n")
            break
            
    return jsonify({
        "success": not has_error,
        "output": "\n".join(full_output),
        "steps": step_status,
        "folders": get_folder_info()
    })

# REST Endpoints đồng bộ chuẩn NestJS
@app.route("/api/spark-sql/overview", methods=["GET"])
def api_spark_sql_overview():
    data = read_json_file("spark_sql_analytics.json")
    return jsonify(data)

@app.route("/api/spark-sql/query/<qid>", methods=["GET"])
def api_spark_sql_query(qid):
    overview = read_json_file("spark_sql_analytics.json")
    query_key = f"query_{qid}"
    if "queries" in overview and query_key in overview["queries"]:
        return jsonify(overview["queries"][query_key])
    return jsonify({"error": f"Không tìm thấy query id: {qid}"}), 404

@app.route("/api/ml/metrics", methods=["GET"])
def api_ml_metrics():
    return jsonify(read_json_file("ml_results.json"))

@app.route("/api/ml/kmeans", methods=["GET"])
def api_ml_kmeans():
    return jsonify(read_json_file("kmeans_summary.json", []))

@app.route("/api/ml/risk-distribution", methods=["GET"])
def api_ml_risk_distribution():
    return jsonify(read_json_file("risk_distribution.json"))

@app.route("/api/ml/high-risk-employees", methods=["GET"])
def api_ml_high_risk_employees():
    return jsonify(read_json_file("top_high_risk_employees.json", []))

@app.route("/api/ml/predict-risk", methods=["POST"])
def api_ml_predict_risk():
    req = request.get_json(silent=True) or {}
    age = float(req.get("age", 35))
    monthly_income = float(req.get("monthlyIncome", 5000))
    over_time = str(req.get("overTime", "No")).strip().lower() in ["yes", "true", "1"]
    work_life_balance = float(req.get("workLifeBalance", 3))
    years_at_company = float(req.get("yearsAtCompany", 5))
    total_working_years = float(req.get("totalWorkingYears", 8))
    
    # Baseline
    score = 20.0
    if over_time:
        score += 28.0
    if monthly_income < 3000:
        score += 22.0
    elif monthly_income < 5000:
        score += 10.0
    elif monthly_income > 12000:
        score -= 15.0
        
    if work_life_balance == 1:
        score += 24.0
    elif work_life_balance == 2:
        score += 10.0
    elif work_life_balance == 4:
        score -= 8.0
        
    if years_at_company < 2:
        score += 14.0
    elif years_at_company > 8:
        score -= 10.0
        
    if age < 28:
        score += 10.0
    elif age > 45:
        score -= 8.0
        
    score = max(5.0, min(98.0, round(score, 1)))
    
    if score >= 70.0:
        alert_tier = "CẤP ĐỘ 3: BÁO ĐỘNG ĐỎ (HIGH RISK)"
        tier_code = "HIGH"
        badge_color = "#ef4444"
        recommendations = [
            "Cắt giảm ngay chế độ làm thêm giờ liên tục (OverTime)",
            "Rà soát mức thu nhập theo định biên thị trường ngay trong tháng",
            "Trưởng bộ phận tổ chức phiên 1-on-1 lắng nghe tâm tư",
            "Thiết lập lộ trình phát triển thăng tiến rõ ràng trong 6 tháng"
        ]
    elif score >= 30.0:
        alert_tier = "CẤP ĐỘ 2: CẢNH BÁO (MEDIUM RISK)"
        tier_code = "MEDIUM"
        badge_color = "#f59e0b"
        recommendations = [
            "Theo dõi mức độ gắn kết và hài lòng công việc",
            "Khuyến khích cân bằng cuộc sống và giờ nghỉ ngơi",
            "Cân nhắc đề cử tham gia các dự án đổi mới công nghệ"
        ]
    else:
        alert_tier = "CẤP ĐỘ 1: AN TOÀN (LOW RISK)"
        tier_code = "LOW"
        badge_color = "#10b981"
        recommendations = [
            "Duy trì môi trường và động lực làm việc tích cực",
            "Ghi nhận và khen thưởng định kỳ các đóng góp chuyên môn",
            "Bồi dưỡng đưa vào nhóm nhân sự nòng cốt kế cận"
        ]
        
    return jsonify({
        "success": True,
        "riskScorePercent": score,
        "alertTier": alert_tier,
        "tierCode": tier_code,
        "badgeColor": badge_color,
        "recommendations": recommendations,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    })

@app.route("/api/streaming/latest", methods=["GET"])
def api_streaming_latest():
    events = read_json_file("kafka_stream_events.json", [])
    return jsonify(events)

@app.route("/api/streaming/simulate", methods=["POST"])
def api_streaming_simulate():
    templates = [
        ("CHECK_IN_LATE", "Nhân viên đi muộn > 45 phút không báo trước", 7.0),
        ("OVERTIME_NIGHT", "Làm thêm giờ ca đêm > 4 tiếng liên tục", 15.0),
        ("WEEKEND_ACCESS", "Đăng nhập hệ thống nội bộ vào ngày nghỉ", 5.5),
        ("COMPENSATION_LOOKUP", "Tra cứu bảng lương & quy chế thôi việc", 13.0),
        ("JOB_PORTAL_DETECTED", "Truy cập các trang tuyển dụng bên ngoài", 19.5),
        ("NEGATIVE_FEEDBACK", "Gửi khảo sát không hài lòng về quản lý", 23.0),
        ("COMMENDATION_AWARD", "Được khen thưởng hoàn thành xuất sắc dự án", -14.0),
        ("ON_TIME_CHECKIN", "Check-in đúng giờ và hoàn thành tốt ca làm", -3.0)
    ]
    roles = ["Sales Executive", "Research Scientist", "Laboratory Technician", "Developer", "HR Specialist"]
    departments = ["Research & Development", "Sales", "Human Resources"]
    
    emp_id = f"EMP_{random.randint(1001, 1470)}"
    tpl = random.choice(templates)
    prior_risk = random.uniform(20.0, 75.0)
    new_risk = max(5.0, min(99.0, round(prior_risk + tpl[2] + random.uniform(-2.0, 2.0), 1)))
    
    if new_risk >= 70.0:
        alert_level = "CẤP 3: BÁO ĐỘNG ĐỎ (HIGH RISK)"
        badge_color = "#ef4444"
    elif new_risk >= 30.0:
        alert_level = "CẤP 2: CẢNH BÁO (MEDIUM RISK)"
        badge_color = "#f59e0b"
    else:
        alert_level = "CẤP 1: AN TOÀN (LOW RISK)"
        badge_color = "#10b981"
        
    new_event = {
        "event_id": f"EVT-{int(time.time()*1000)}",
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "employee_id": emp_id,
        "department": random.choice(departments),
        "role": random.choice(roles),
        "event_type": tpl[0],
        "description": tpl[1],
        "risk_delta": f"{'+' if tpl[2] > 0 else ''}{tpl[2]}%",
        "current_risk_score": new_risk,
        "alert_level": alert_level,
        "badge_color": badge_color
    }
    
    events = read_json_file("kafka_stream_events.json", [])
    events.insert(0, new_event)
    events = events[:50]
    
    stream_file = os.path.join(OUTPUT_DIR, "kafka_stream_events.json")
    try:
        with open(stream_file, "w", encoding="utf-8") as f:
            json.dump(events, f, ensure_ascii=False, indent=2)
    except Exception:
        pass
        
    return jsonify(new_event)

@app.route("/api/ml/experiments", methods=["GET"])
def api_ml_experiments():
    return jsonify(read_json_file("model_experiments_comparison.json", []))

@app.route("/api/ml/misclassified-cases", methods=["GET"])
def api_ml_misclassified_cases():
    return jsonify(read_json_file("misclassified_cases_analysis.json"))

@app.route("/api/pipeline/reconciliation", methods=["GET"])
def api_pipeline_reconciliation():
    return jsonify(read_json_file("hdfs_reconciliation_audit.json"))

@app.route("/api/pipeline/e2e-test", methods=["GET"])
def api_pipeline_e2e_test():
    return jsonify(read_json_file("kafka_e2e_test_report.json"))

@app.route("/api/pipeline/compaction", methods=["GET"])
def api_pipeline_compaction():
    return jsonify(read_json_file("parquet_compaction_log.json"))

@app.route("/api/pipeline/benchmark", methods=["GET"])
def api_pipeline_benchmark():
    return jsonify(read_json_file("storage_benchmark.json"))

@app.route("/api/pipeline/airflow-dag", methods=["GET"])
def api_pipeline_airflow_dag():
    return jsonify(read_json_file("airflow_dag_status.json"))

@app.route("/api/upload", methods=["POST"])
def api_upload():
    raw_dir = os.path.join(DATA_DIR, "raw")
    os.makedirs(raw_dir, exist_ok=True)
    target_csv = os.path.join(raw_dir, "Dataset.csv")
    
    if "file" not in request.files:
        source_csv = os.path.join(BASE_DIR, "WA_Fn-UseC_-HR-Employee-Attrition.csv")
        if os.path.exists(source_csv):
            import shutil
            shutil.copy2(source_csv, target_csv)
            step_status["upload_data"] = True
            return jsonify({
                "success": True,
                "message": "Đã tự động nạp dataset WA_Fn-UseC_-HR-Employee-Attrition.csv vào raw/Dataset.csv",
                "steps": step_status,
                "folders": get_folder_info()
            })
        return jsonify({"success": False, "message": "Không tìm thấy file để upload"}), 400
        
    f = request.files["file"]
    if f.filename == "":
        return jsonify({"success": False, "message": "Tên file rỗng"}), 400
        
    f.save(target_csv)
    step_status["upload_data"] = True
    
    return jsonify({
        "success": True,
        "message": f"Đã upload thành công {f.filename} thành raw/Dataset.csv!",
        "steps": step_status,
        "folders": get_folder_info()
    })

if __name__ == "__main__":
    print("=" * 70)
    print(" BigData Lab Server - HR Employee Attrition Full Stack")
    print(" Sinh viên: Vũ Lê Anh Đức - MSSV: 2001230191")
    print(" Địa chỉ truy cập Web: http://localhost:5000")
    print("=" * 70)
    app.run(host="0.0.0.0", port=5000, debug=False)
