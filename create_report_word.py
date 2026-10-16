import os
import sys
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

sys.stdout.reconfigure(encoding='utf-8')

def set_cell_shading(cell, color_hex):
    shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
    cell._tc.get_or_add_tcPr().append(shading_elm)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def create_document():
    doc = Document()

    # Cấu hình lề trang (A4)
    for section in doc.sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(0.8)

    # Palette màu học thuật & công nghệ cao
    COLOR_PRIMARY = RGBColor(30, 58, 138)     # Deep Blue
    COLOR_SECONDARY = RGBColor(109, 40, 217)  # Purple
    COLOR_TEXT = RGBColor(30, 41, 59)         # Slate Dark
    COLOR_MUTED = RGBColor(100, 116, 139)     # Slate Muted

    # Style chuẩn
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Times New Roman'
    normal_style.font.size = Pt(12)
    normal_style.font.color.rgb = COLOR_TEXT
    normal_style.paragraph_format.line_spacing = 1.25
    normal_style.paragraph_format.space_after = Pt(6)

    # -------------------------------------------------------------
    # TRANG TIÊU ĐỀ (HEADER BÁO CÁO)
    # -------------------------------------------------------------
    p_header = doc.add_paragraph()
    p_header.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_uni = p_header.add_run("BỘ GIÁO DỤC VÀ ĐÀO TẠO - TRƯỜNG ĐẠI HỌC CÔNG THƯƠNG TP.HCM\n")
    r_uni.bold = True
    r_uni.font.size = Pt(11)
    r_fac = p_header.add_run("KHOA CÔNG NGHỆ THÔNG TIN - BỘ MÔN KHOA HỌC DỮ LIỆU & TTNT\n")
    r_fac.bold = True
    r_fac.font.size = Pt(11)
    p_header.paragraph_format.space_after = Pt(12)

    p_line = doc.add_paragraph()
    p_line.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_line = p_line.add_run("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    r_line.font.color.rgb = COLOR_SECONDARY
    p_line.paragraph_format.space_after = Pt(14)

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_sub = p_title.add_run("BÁO CÁO THUYẾT MINH & CẨM NANG VẤN ĐÁP ĐỒ ÁN MÔN HỌC\nNHẬP MÔN DỮ LIỆU LỚN (BIG DATA)\n\n")
    r_sub.font.size = Pt(13)
    r_sub.bold = True
    r_sub.font.color.rgb = COLOR_SECONDARY

    r_main_title = p_title.add_run("XÂY DỰNG HỆ THỐNG PIPELINE DỮ LIỆU LỚN PHÂN TÍCH CÁC YẾU TỐ ẢNH HƯỞNG VÀ DỰ ĐOÁN NGUY CƠ NGHỈ VIỆC CỦA NHÂN VIÊN\n")
    r_main_title.bold = True
    r_main_title.font.size = Pt(16)
    r_main_title.font.color.rgb = COLOR_PRIMARY

    r_en_title = p_title.add_run("(Employee Attrition Analysis & Prediction with Hadoop, PySpark, Kafka & Airflow)\n")
    r_en_title.italic = True
    r_en_title.font.size = Pt(11.5)
    r_en_title.font.color.rgb = COLOR_MUTED
    p_title.paragraph_format.space_after = Pt(18)

    # Bảng thông tin sinh viên & giảng viên
    meta_table = doc.add_table(rows=4, cols=2)
    meta_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    meta_table.autofit = False

    meta_data = [
        ("Giảng viên hướng dẫn:", "ThS. Ngô Dương Hà (hand@huit.edu.vn)"),
        ("Sinh viên thực hiện:", "Vũ Lê Anh Đức"),
        ("Mã số sinh viên (MSSV):", "2001230191"),
        ("Học phần / Học kỳ:", "Nhập môn Dữ liệu lớn (Big Data) - 2026")
    ]

    for row_idx, (col1, col2) in enumerate(meta_data):
        row = meta_table.rows[row_idx]
        cell_1 = row.cells[0]
        cell_2 = row.cells[1]
        cell_1.width = Inches(2.5)
        cell_2.width = Inches(3.8)
        
        p1 = cell_1.paragraphs[0]
        p1.paragraph_format.space_after = Pt(2)
        r1 = p1.add_run(col1)
        r1.bold = True
        r1.font.size = Pt(11)
        
        p2 = cell_2.paragraphs[0]
        p2.paragraph_format.space_after = Pt(2)
        r2 = p2.add_run(col2)
        r2.font.size = Pt(11)
        
        set_cell_shading(cell_1, "F8FAFC")
        set_cell_shading(cell_2, "F8FAFC")
        set_cell_margins(cell_1, top=60, bottom=60, left=90, right=90)
        set_cell_margins(cell_2, top=60, bottom=60, left=90, right=90)

    doc.add_paragraph().paragraph_format.space_after = Pt(12)

    def add_chapter_heading(title_text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(16)
        p.paragraph_format.space_after = Pt(8)
        run = p.add_run(title_text)
        run.bold = True
        run.font.size = Pt(13.5)
        run.font.color.rgb = COLOR_PRIMARY
        return p

    def add_section_heading(title_text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(6)
        run = p.add_run(title_text)
        run.bold = True
        run.font.size = Pt(12)
        run.font.color.rgb = COLOR_SECONDARY
        return p

    def add_callout(text, prefix="📌 LƯU Ý / NGUYÊN LÝ CỐT LÕI:"):
        tbl = doc.add_table(rows=1, cols=1)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        cell = tbl.cell(0, 0)
        cell.width = Inches(6.3)
        set_cell_shading(cell, "F5F3FF")
        set_cell_margins(cell, top=80, bottom=80, left=120, right=120)
        p = cell.paragraphs[0]
        p.paragraph_format.space_after = Pt(2)
        r_pre = p.add_run(f"{prefix}\n")
        r_pre.bold = True
        r_pre.font.size = Pt(10.5)
        r_pre.font.color.rgb = COLOR_SECONDARY
        r_txt = p.add_run(text)
        r_txt.font.size = Pt(10)
        doc.add_paragraph().paragraph_format.space_after = Pt(4)

    # -------------------------------------------------------------
    # CHƯƠNG 1: TỔNG QUAN ĐỀ TÀI & TẬP DỮ LIỆU
    # -------------------------------------------------------------
    add_chapter_heading("CHƯƠNG 1: TỔNG QUAN ĐỀ TÀI & TẬP DỮ LIỆU NGHIÊN CỨU")

    p = doc.add_paragraph()
    p.add_run(
        "Trong bối cảnh chuyển đổi số và quản trị doanh nghiệp hiện đại, nguồn nhân lực (Human Resources) "
        "được xem là tài sản chiến lược quý giá nhất. Biến động nhân sự, đặc biệt là tình trạng nhân viên nghỉ việc "
        "(Employee Attrition) đột ngột, gây ra những tổn thất tài chính nặng nề: chi phí tuyển dụng thay thế, "
        "thời gian đào tạo nhân sự mới, sụt giảm năng suất và rò rỉ bí mật kinh doanh. Đề tài "
    )
    r_bold = p.add_run("«Phân tích các yếu tố ảnh hưởng và dự đoán nguy cơ nghỉ việc của nhân viên»")
    r_bold.bold = True
    p.add_run(
        " hướng đến việc ứng dụng hệ sinh thái Dữ liệu lớn (Big Data Ecosystem) để xây dựng một quy trình khép kín từ "
        "thu thập dữ liệu (Ingestion), lưu trữ phân tán (Storage), xử lý song song (Processing) đến phân tích kinh doanh "
        "và dự báo rủi ro bằng học máy (BI / Machine Learning)."
    )

    add_section_heading("1.1. Giới thiệu bộ dữ liệu IBM HR Analytics")
    p = doc.add_paragraph()
    p.add_run(
        "Đồ án sử dụng bộ dữ liệu chuẩn mực thế giới do tập đoàn IBM phát hành: "
        "WA_Fn-UseC_-HR-Employee-Attrition.csv gồm 1,470 bản ghi nhân viên với 35 trường thông tin chi tiết:"
    )

    data_attr_table = doc.add_table(rows=6, cols=3)
    data_attr_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    headers = ["Nhóm thuộc tính", "Các trường thông tin đại diện", "Ý nghĩa phân tích"]
    for i, h in enumerate(headers):
        cell = data_attr_table.cell(0, i)
        set_cell_shading(cell, "1E3A8A")
        set_cell_margins(cell, top=70, bottom=70, left=90, right=90)
        p = cell.paragraphs[0]
        r = p.add_run(h)
        r.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)
        r.font.size = Pt(10.5)

    attr_rows = [
        ("Biến mục tiêu (Target)", "Attrition (Yes / No)", "16.12% nhân viên nghỉ việc (237 người) vs 83.88% ở lại (1,233 người). Thách thức mất cân bằng lớp cực đoan (Class Imbalance: tỷ lệ 1 : 5.2)."),
        ("Nhân khẩu học & Cá nhân", "Age, Gender, MaritalStatus, Education, DistanceFromHome", "Khảo sát ảnh hưởng của độ tuổi, tình trạng hôn nhân và khoảng cách đi lại đến quyết định gắn bó."),
        ("Công việc & Chức danh", "Department, JobRole, TotalWorkingYears, YearsAtCompany, YearsSinceLastPromotion", "Đánh giá thâm niên, số năm làm việc với quản lý trực tiếp và thời gian chưa được thăng tiến."),
        ("Thu nhập & Đãi ngộ", "MonthlyIncome, PercentSalaryHike, StockOptionLevel, HourlyRate", "Khảo sát mức độ thỏa mãn về tài chính, cổ phiếu thưởng và chế độ tăng lương định kỳ."),
        ("Tâm lý & Môi trường", "JobSatisfaction, EnvironmentSatisfaction, WorkLifeBalance, OverTime", "Thang đo 1 - 4 đánh giá mức độ hài lòng, áp lực công việc và chế độ làm thêm giờ (OT).")
    ]

    for row_idx, rdata in enumerate(attr_rows, 1):
        for col_idx, text in enumerate(rdata):
            cell = data_attr_table.cell(row_idx, col_idx)
            set_cell_shading(cell, "FFFFFF" if row_idx % 2 == 1 else "F8FAFC")
            set_cell_margins(cell, top=60, bottom=60, left=80, right=80)
            p = cell.paragraphs[0]
            p.paragraph_format.space_after = Pt(2)
            r = p.add_run(text)
            r.font.size = Pt(9.5)

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    # -------------------------------------------------------------
    # CHƯƠNG 2: KIẾN TRÚC HỆ THỐNG THEO SLIDE BÀI GIẢNG
    # -------------------------------------------------------------
    add_chapter_heading("CHƯƠNG 2: BẢN ĐỒ CÔNG NGHỆ VÀ KIẾN TRÚC THEO SLIDE BÀI GIẢNG")

    p = doc.add_paragraph()
    p.add_run(
        "Theo đúng chuẩn kiến trúc được trình bày trong bài giảng môn học (Chương 4: Data Ingestion & Orchestration), "
        "hệ thống Big Data được cấu thành từ 6 lớp chức năng rõ ràng, giải quyết 3 câu hỏi cốt lõi:"
    )

    add_callout(
        "1. INGESTION: «Làm sao đưa dữ liệu vào?» (Batch Ingestion cho file tĩnh & Streaming Ingestion cho log sự kiện).\n"
        "2. PROCESSING: «Làm gì với dữ liệu?» (Apache Spark tính toán song song In-Memory, làm sạch và nén Parquet).\n"
        "3. ORCHESTRATION: «Khi nào và theo thứ tự nào?» (Apache Airflow DAG điều phối thứ tự, lịch chạy và giám sát lỗi).",
        "💡 BA CÂU HỎI CỐT LÕI CỦA MỘT BIG DATA PIPELINE:"
    )

    arch_table = doc.add_table(rows=8, cols=4)
    arch_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    arch_headers = ["Lớp kiến trúc", "Công nghệ slide", "Vai trò nghiệp vụ", "Hiện thực trong Đồ án"]
    for i, h in enumerate(arch_headers):
        cell = arch_table.cell(0, i)
        set_cell_shading(cell, "6D28D9")
        set_cell_margins(cell, top=70, bottom=70, left=80, right=80)
        p = cell.paragraphs[0]
        r = p.add_run(h)
        r.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)
        r.font.size = Pt(10.5)

    arch_rows = [
        ("Storage", "HDFS, Object Storage", "Lưu trữ phân tán, nhân bản chịu lỗi", "Bước 1 & Bước 7: Cấu trúc Data Lake raw, processed, output trên HDFS/Local."),
        ("Ingestion (Batch)", "File Upload, Sqoop", "Nạp tập dữ liệu thô ban đầu", "Bước 2: Nạp Dataset.csv (1,470 bản ghi) vào tầng raw/."),
        ("Processing", "Apache Spark, Flink", "Biến đổi In-Memory, ETL, Feature", "Bước 3 & Bước 4: PySpark đọc CSV, lọc cột vô nghĩa, ghi Parquet."),
        ("Query / Serving", "Spark SQL, Hive", "Truy vấn dữ liệu kinh doanh", "Bước 5: Spark SQL bóc tách các nguyên nhân nghỉ việc (OverTime, Lương)."),
        ("BI / ML", "Spark MLlib, Python ML", "Dự báo, mô hình học máy", "Bước 6: Random Forest & Logistic Regression dự đoán nguy cơ nghỉ việc."),
        ("Ingestion (Streaming)", "Apache Kafka, Flume", "Thu thập sự kiện liên tục", "Bước 8: Kafka Producer mô phỏng event chấm công, OT ca đêm thời gian thực."),
        ("Orchestration", "Apache Airflow", "Lên lịch, retry, dependency", "Bước 9: Airflow DAG tự động hóa chu trình khép kín @daily.")
    ]

    for row_idx, rdata in enumerate(arch_rows, 1):
        for col_idx, text in enumerate(rdata):
            cell = arch_table.cell(row_idx, col_idx)
            set_cell_shading(cell, "FFFFFF" if row_idx % 2 == 1 else "F5F3FF")
            set_cell_margins(cell, top=50, bottom=50, left=70, right=70)
            p = cell.paragraphs[0]
            p.paragraph_format.space_after = Pt(2)
            r = p.add_run(text)
            r.font.size = Pt(9.5)

    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    # -------------------------------------------------------------
    # CHƯƠNG 3: QUY TRÌNH THỰC HIỆN CHI TIẾT 9 BƯỚC
    # -------------------------------------------------------------
    add_chapter_heading("CHƯƠNG 3: QUY TRÌNH THỰC HIỆN CHI TIẾT 9 BƯỚC PIPELINE")

    steps_detail = [
        {
            "num": "Bước 1: Chuẩn bị HDFS (Storage Workspace)",
            "layer": "Tầng STORAGE",
            "file": "src/step1_hdfs_prepare.py",
            "what": "Khởi tạo cấu trúc phân cấp Data Lake theo chuẩn Medallion Architecture gồm 3 thư mục: raw/ (chứa dữ liệu thô), processed/ (dữ liệu Parquet đã làm sạch), output/ (kết quả mô hình & báo cáo).",
            "how": "Mã nguồn gọi lệnh Hadoop Client hdfs dfs -mkdir -p. Máy chủ NameNode của HDFS tiếp nhận yêu cầu, cập nhật siêu dữ liệu (Metadata) phân tán vào RAM và đồng bộ hóa sang DataNode. Hệ thống đồng thời khởi tạo cấu trúc thư mục cục bộ song song.",
            "where": "HDFS: /courses/2/projects/3/students/2001230191/{raw, processed, output}\nLocal: D:\\Doan_BigData\\data\\{raw, processed, output}",
            "output": "3 phân vùng thư mục sẵn sàng đón nhận dữ liệu, trạng thái hiển thị HDFS_PREPARE_OK."
        },
        {
            "num": "Bước 2: Upload dữ liệu (Batch Ingestion)",
            "layer": "Tầng INGESTION (Batch Ingestion)",
            "file": "src/step2_upload_ingest.py",
            "what": "Nạp tập dữ liệu nguồn WA_Fn-UseC_-HR-Employee-Attrition.csv vào phân vùng lưu trữ raw/ và kiểm tra tính toàn vẹn.",
            "how": "Cơ chế Batch Ingestion nạp tệp theo đợt từ nguồn bên ngoài. HDFS tự động phân mảnh tệp thành các khối Block 128MB (Sharding) và nhân bản sang 3 DataNode khác nhau (Replication Factor = 3) để đảm bảo an toàn tuyệt đối khi có máy chủ vật lý gặp sự cố.",
            "where": "Local: D:\\Doan_BigData\\data\\raw\\Dataset.csv\nHDFS: /courses/.../raw/Dataset.csv",
            "output": "Tệp CSV nguyên bản (Bronze Layer) gồm 1,470 dòng và 35 thuộc tính được xác thực toàn vẹn (dung lượng 222.63 KB)."
        },
        {
            "num": "Bước 3: Đọc bằng Spark (Processing Layer)",
            "layer": "Tầng PROCESSING",
            "file": "src/step3_spark_read.py",
            "what": "Khởi tạo SparkSession kết nối HDFS, đọc dữ liệu phân tán và tự động phân tích Schema.",
            "how": "Khác với MapReduce truyền thống phải liên tục ghi/đọc đĩa từ gây nghẽn I/O, Apache Spark nạp dữ liệu trực tiếp vào bộ nhớ RAM (In-Memory Computing). Tùy chọn inferSchema=True giúp Spark tự động quét và xác định kiểu dữ liệu của 35 cột; dữ liệu được phân chia thành các Partitions chạy song song.",
            "where": "Bộ nhớ RAM dưới dạng cấu trúc bảng phân tán PySpark DataFrame (df).",
            "output": "Trạng thái SPARK_READ_OK, in cây Schema phân cấp và hiển thị bảng 10 dòng đầu tiên của tập dữ liệu nhân sự."
        },
        {
            "num": "Bước 4: Làm sạch dữ liệu & Ghi Parquet",
            "layer": "Tầng PROCESSING (ETL & Transformation)",
            "file": "src/step4_clean_transform.py",
            "what": "Loại bỏ nhiễu, mã hóa biến mục tiêu, sinh đặc trưng mới (Feature Engineering) và nén tối ưu hóa dạng cột Parquet.",
            "how": "1) Loại bỏ 4 cột vô nghĩa/hằng số: EmployeeCount, Over18, StandardHours, EmployeeNumber.\n2) Mã hóa Attrition_Label (Yes=1, No=0).\n3) Tạo biến mới: Income_Per_WorkingYear (Thu nhập trên số năm làm việc), Promotion_Lag_Ratio (Tỷ lệ chậm thăng tiến).\n4) Ghi dữ liệu ra định dạng Apache Parquet (Snappy Compression), cấu trúc lưu trữ theo cột giúp giảm 60% dung lượng và tăng tốc độ đọc cột gấp nhiều lần.",
            "where": "D:\\Doan_BigData\\data\\processed\\hr_cleaned.parquet",
            "output": "Tệp Parquet đã làm sạch chuẩn (Silver Layer) gồm 1,470 dòng x 34 thuộc tính, không còn bất kỳ giá trị null nào."
        },
        {
            "num": "Bước 5: Spark SQL phân tích nhân sự",
            "layer": "Tầng QUERY / SERVING",
            "file": "src/step5_spark_sql.py",
            "what": "Đăng ký bảng tạm SQL (TempView), thực thi các câu truy vấn nghiệp vụ phức tạp để phân tích các yếu tố gây nghỉ việc.",
            "how": "Trình tối ưu hóa Catalyst Optimizer của Spark phân tích câu lệnh SQL, tối ưu hóa các phép lọc (WHERE) và gom nhóm (GROUP BY), tính toán song song trên RAM và in kết quả bảng ASCII đẹp mắt.",
            "where": "Bảng tổng hợp trên RAM và in trực tiếp ra cửa sổ Terminal.",
            "output": "4 phát hiện định lượng then chốt:\n• Làm thêm giờ (OverTime): Nhóm làm thêm có tỷ lệ nghỉ việc là 30.53%, gấp gần 3 lần nhóm không làm thêm (10.44%).\n• Phòng ban: Sales có tỷ lệ nghỉ cao nhất (20.63%), HR (19.05%), R&D (13.84%).\n• Chức vụ: Sales Representative có tỷ lệ nghỉ việc cao đột biến (39.76%).\n• Cân bằng cuộc sống: Nhóm WorkLifeBalance mức 1 (Kém) có tỷ lệ nghỉ việc lên đến 31.25%."
        },
        {
            "num": "Bước 6: MLlib Huấn luyện mô hình dự đoán",
            "layer": "Tầng BI / ML",
            "file": "src/step6_ml_predict.py",
            "what": "Xử lý lệch lớp cực đoan, huấn luyện thuật toán Random Forest Classifier và Logistic Regression dự đoán nguy cơ nhân viên nghỉ việc.",
            "how": "1) Giải quyết mất cân bằng lớp (1:5.2): Áp dụng kỹ thuật Balanced Class Weighting phạt nặng mô hình khi bỏ lọt ca nghỉ việc.\n2) Chuẩn hóa đặc trưng bằng StandardScaler.\n3) Chia tập dữ liệu 80/20 có phân tầng (Stratified Split).\n4) Huấn luyện 100 cây quyết định Random Forest và trích xuất độ quan trọng của đặc trưng (Feature Importance).",
            "where": "D:\\Doan_BigData\\data\\output\\metrics_summary.json",
            "output": "Mô hình đạt ROC-AUC ~0.80, Accuracy 83.67%. Top yếu tố chi phối lớn nhất: Thu nhập hàng tháng (7.52%), Độ tuổi (6.81%), Tổng số năm kinh nghiệm (5.39%)."
        },
        {
            "num": "Bước 7: Lưu kết quả & Chấm điểm rủi ro",
            "layer": "Tầng STORAGE & SERVING",
            "file": "src/step7_save_results.py",
            "what": "Chấm điểm xác suất nguy cơ nghỉ việc (Risk Score %) từ 0% đến 100% cho từng nhân viên, xuất danh sách nhân viên nguy cơ cao để HR giữ chân.",
            "how": "Mô hình tính hàm xác suất predict_proba, phân loại nhân viên theo 3 cấp độ: Thấp (<30%), Trung bình (30-70%), Nguy cơ cao (>=70%). Lọc nhóm nguy cơ cao và đồng bộ vào HDFS Output.",
            "where": "Local: D:\\Doan_BigData\\data\\output\\high_risk_employees.csv\nHDFS: /courses/.../output/high_risk_employees.csv",
            "output": "Danh sách nhân viên có nguy cơ nghỉ việc cao nhất kèm điểm số rủi ro cụ thể để ban giám đốc và phòng HR có biện pháp can thiệp kịp thời."
        },
        {
            "num": "Bước 8: Kafka Streaming Ingestion",
            "layer": "Tầng INGESTION (Streaming)",
            "file": "src/step8_kafka_simulation.py",
            "what": "Mô phỏng cơ chế thu nhận dữ liệu dòng sự kiện liên tục thời gian thực (Event Stream) từ log quẹt thẻ, chấm công, làm đêm.",
            "how": "Cơ chế Kafka Producer liên tục sinh event dạng JSON (CHECK_IN_LATE, OVERTIME_LOG, WEEKEND_ACCESS...) gửi vào Kafka Topic 'hr-employee-events'. Spark Streaming đóng vai trò Consumer đọc liên tục để cập nhật điểm rủi ro nhân viên theo thời gian thực.",
            "where": "Lưu đệm trong bộ đệm phân vùng (Topic Partitions) của Kafka Broker.",
            "output": "Luồng sự kiện thời gian thực nhảy liên tục trên Terminal với mức độ rủi ro cộng dồn (+5% đến +15% rủi ro/sự kiện)."
        },
        {
            "num": "Bước 9: Airflow DAG điều phối tự động hóa",
            "layer": "Tầng ORCHESTRATION",
            "file": "src/step9_airflow_dag.py",
            "what": "Thiết lập đồ thị có hướng không chu trình (DAG) để điều phối toàn bộ chu trình 8 bước trên thành hệ thống tự động hoàn toàn.",
            "how": "Airflow đóng vai trò 'nhạc trưởng' (không chứa dữ liệu thô), thiết lập chuỗi phụ thuộc nghiêm ngặt: hdfs_prep >> upload_data >> spark_read >> clean_parquet >> spark_sql >> train_ml >> save_output. Lên lịch chạy @daily (00:00 hàng ngày), tự động retry 3 lần khi xảy ra sự cố mạng.",
            "where": "D:\\Doan_BigData\\src\\step9_airflow_dag.py",
            "output": "Sơ đồ luồng DAG hoàn chỉnh, tự động hóa 100% chu trình Big Data mà không cần con người can thiệp thủ công."
        }
    ]

    for s in steps_detail:
        add_section_heading(s["num"])
        step_tbl = doc.add_table(rows=5, cols=2)
        step_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        step_tbl.autofit = False
        
        info_pairs = [
            ("Lớp kiến trúc trong Slide:", s["layer"]),
            ("Mục đích (Làm gì?):", s["what"]),
            ("Cách thức hoạt động kỹ thuật:", s["how"]),
            ("Lưu ở đâu (Vị trí lưu trữ)?:", s["where"]),
            ("Kết quả đầu ra (Outputs):", s["output"])
        ]
        
        for r_idx, (label, val) in enumerate(info_pairs):
            row = step_tbl.rows[r_idx]
            c1, c2 = row.cells[0], row.cells[1]
            c1.width = Inches(2.2)
            c2.width = Inches(4.1)
            
            p1 = c1.paragraphs[0]
            p1.paragraph_format.space_after = Pt(2)
            run1 = p1.add_run(label)
            run1.bold = True
            run1.font.size = Pt(10)
            
            p2 = c2.paragraphs[0]
            p2.paragraph_format.space_after = Pt(2)
            run2 = p2.add_run(val)
            run2.font.size = Pt(10)
            
            set_cell_shading(c1, "F1F5F9")
            set_cell_shading(c2, "FFFFFF" if r_idx % 2 == 0 else "F8FAFC")
            set_cell_margins(c1, top=50, bottom=50, left=70, right=70)
            set_cell_margins(c2, top=50, bottom=50, left=70, right=70)
            
        doc.add_paragraph().paragraph_format.space_after = Pt(4)

    # -------------------------------------------------------------
    # CHƯƠNG 4: THIẾT KẾ WEB BIG DATA LAB DASHBOARD
    # -------------------------------------------------------------
    add_chapter_heading("CHƯƠNG 4: THIẾT KẾ ỨNG DỤNG WEB LAB DASHBOARD TƯƠNG TÁC")

    p = doc.add_paragraph()
    p.add_run(
        "Nhằm trực quan hóa đồ án và giúp giảng viên/người dùng có thể tương tác trực tiếp, một ứng dụng Web Full-stack "
        "đã được phát triển riêng biệt tại địa chỉ "
    )
    p.add_run("http://localhost:5000").bold = True
    p.add_run(" với bố cục 3 cột chuẩn phòng Lab Big Data:")

    p_c1 = doc.add_paragraph(style='List Bullet')
    p_c1.add_run("Cột 1 (Workspace HDFS): ").bold = True
    p_c1.add_run("Hiển thị đường dẫn không gian HDFS của sinh viên (/courses/2/projects/3/students/2001230191), trạng thái BigData Core sẵn sàng, nút Upload tập dữ liệu và cây thư mục phân cấp raw/, processed/, output/ cập nhật dung lượng thời gian thực.")

    p_c2 = doc.add_paragraph(style='List Bullet')
    p_c2.add_run("Cột 2 (9 Bước Pipeline): ").bold = True
    p_c2.add_run("Bố trí 9 thẻ bước thông minh có đánh dấu tick xanh (check icon) khi hoàn tất. Cho phép người dùng click vào từng bước để xem giải thích chi tiết, bấm 'Chạy bước này' hoặc kích hoạt 'Chạy toàn bộ Pipeline (1 - 9)'.")

    p_c3 = doc.add_paragraph(style='List Bullet')
    p_c3.add_run("Cột 3 (Terminal Thực hành cố định): ").bold = True
    p_c3.add_run("Cửa sổ Terminal phong cách Linux màu đen tuyền cố định, tự động cuộn nội bộ mượt mà, hỗ trợ nhập lệnh ($ run-stage ..., $ run-all, $ help, $ clear) và hiển thị trực tiếp các bảng dữ liệu ASCII chuẩn Spark SQL và Machine Learning.")

    # -------------------------------------------------------------
    # CHƯƠNG 5: KẾT LUẬN & ĐÁNH GIÁ NGHIỆP VỤ
    # -------------------------------------------------------------
    add_chapter_heading("CHƯƠNG 5: KẾT LUẬN VÀ GIÁ TRỊ THỰC TIỄN CỦA ĐỒ ÁN")

    p_concl = doc.add_paragraph()
    p_concl.add_run(
        "1. Về mặt kỹ thuật: Đồ án đã hiện thực hóa trọn vẹn 6 tầng công nghệ Big Data theo đúng giáo trình: "
        "từ Ingestion (Batch/Streaming), Storage (HDFS Data Lake), Processing (PySpark, Parquet), Query (Spark SQL), "
        "BI/ML (Random Forest phân loại) đến Orchestration (Airflow DAG điều phối tự động).\n\n"
        "2. Về mặt nghiệp vụ: Đã phát hiện chính xác các nguyên nhân cốt lõi khiến nhân viên nghỉ việc: "
        "chế độ làm thêm giờ (OverTime) khiến rủi ro nghỉ việc tăng gấp 3 lần; nhóm nhân viên kinh doanh (Sales Rep) "
        "và kỹ thuật viên phòng lab có tỷ lệ nghỉ cao nhất do áp lực KPI và chênh lệch thu nhập; mức độ cân bằng cuộc sống "
        "kém là chỉ báo sớm nguy hiểm nhất.\n\n"
        "3. Ứng dụng thực tiễn: Hệ thống đã xuất thành công danh sách các nhân viên có rủi ro cao (>70%) kèm điểm số cụ thể "
        "để doanh nghiệp chủ động điều chỉnh chính sách đãi ngộ, phân bổ lại khối lượng công việc trước khi nhân sự rời đi."
    )

    # -------------------------------------------------------------
    # CHƯƠNG 6: CẨM NANG VẤN ĐÁP BẢO VỆ ĐỒ ÁN TOÀN DIỆN (VIVA DEFENSE HANDBOOK)
    # -------------------------------------------------------------
    add_chapter_heading("CHƯƠNG 6: CẨM NANG VẤN ĐÁP BẢO VỆ ĐỒ ÁN TOÀN DIỆN")

    p_intro6 = doc.add_paragraph()
    p_intro6.add_run(
        "Chương này được biên soạn đặc biệt để phục vụ cho buổi thi vấn đáp và bảo vệ đồ án trước Hội đồng Giảng viên. "
        "Nội dung cung cấp bức tranh toàn cảnh về luồng đi của dữ liệu (Data Lineage), giải thích cặn kẽ từng quyết định kỹ thuật, "
        "bộ 12 câu hỏi sát hạch kinh điển của Giảng viên kèm câu trả lời chuẩn xác, bảng thuật ngữ Big Data và kịch bản thuyết trình 5 phút."
    )

    add_section_heading("6.1. Dòng chảy dữ liệu chi tiết (Data Lineage & Lifecycle)")
    p_lin = doc.add_paragraph()
    p_lin.add_run(
        "Dữ liệu trong hệ thống chuyển dịch và tiến hóa qua 4 trạng thái theo chuẩn kiến trúc Medallion Data Lake:\n\n"
        "1. Bronze Layer (Dữ liệu thô - Raw Storage):\n"
        "   • Nguồn: Tệp Dataset.csv từ bên ngoài được nạp qua cổng Batch Ingestion (Bước 2).\n"
        "   • Nơi lưu: HDFS /courses/2/projects/3/students/2001230191/raw/Dataset.csv (và data/raw/).\n"
        "   • Đặc điểm: 1,470 dòng, 35 thuộc tính, định dạng văn bản thuần CSV chưa lọc, được HDFS chia thành các block 128MB và nhân bản 3 lần (Replication = 3).\n\n"
        "2. In-Memory Layer (Dữ liệu trên RAM - Processing Engine):\n"
        "   • Đọc bởi: Apache SparkSession (Bước 3).\n"
        "   • Nơi lưu: Bộ nhớ RAM phân tán dưới dạng PySpark DataFrame (df).\n"
        "   • Đặc điểm: Spark áp dụng kỹ thuật Lazy Evaluation, xây dựng đồ thị thực thi DAG (Directed Acyclic Graph) và chỉ thực thi tính toán khi có hành động (Action) như count(), show().\n\n"
        "3. Silver Layer (Dữ liệu sạch - Optimized Storage):\n"
        "   • Xử lý bởi: Spark Transformation & Feature Engineering (Bước 4).\n"
        "   • Nơi lưu: data/processed/hr_cleaned.parquet.\n"
        "   • Đặc điểm: Loại bỏ 4 cột vô nghĩa, mã hóa nhãn Attrition (0/1), bổ sung 2 đặc trưng kinh doanh (Income_Per_WorkingYear, Promotion_Lag_Ratio). Dữ liệu được nén theo cột bằng Snappy Parquet, tối ưu tốc độ đọc và tiết kiệm hơn 60% bộ nhớ.\n\n"
        "4. Gold Layer (Dữ liệu phục vụ nghiệp vụ & Báo cáo - Serving / Output):\n"
        "   • Phục vụ cho: Spark SQL phân tích nhân sự (Bước 5), Machine Learning dự đoán (Bước 6) và Chấm điểm rủi ro (Bước 7).\n"
        "   • Nơi lưu: data/output/metrics_summary.json và data/output/high_risk_employees.csv (đồng bộ lên HDFS output/).\n"
        "   • Đặc điểm: Chứa danh sách nhân viên có xác suất nghỉ việc >= 70% kèm các chỉ số phân tích trực tiếp cho lãnh đạo doanh nghiệp."
    )

    add_section_heading("6.2. Bộ 12 câu hỏi vấn đáp cốt lõi của Giảng viên & Đáp án kỹ thuật chuẩn")

    qa_list = [
        (
            "Câu 1: Tại sao bài toán này cần dùng công nghệ Big Data (Hadoop/Spark) mà không chỉ dùng Excel hoặc Python Pandas thông thường?",
            "Đáp án: Trong phạm vi đồ án môn học, tập dữ liệu mẫu gồm 1,470 bản ghi được sử dụng để kiểm thử giải thuật và minh họa quy trình. Tuy nhiên, trong môi trường doanh nghiệp thực tế (như FPT, Viettel, Samsung, Shopee), dữ liệu nhân sự không dừng lại ở tệp CSV mà là một hệ thống dữ liệu lớn bao gồm:\n"
            "• Log quẹt thẻ ra vào và chấm công vân tay hàng ngày (hàng triệu lượt log/tháng).\n"
            "• Dữ liệu camera AI nhận diện khuôn mặt và cảm xúc tại văn phòng.\n"
            "• Lịch sử tương tác email, công cụ chat nội bộ (Slack, Teams), log commit Git và VPN của nhân viên.\n"
            "Tổng dung lượng có thể lên đến hàng chục Terabytes. Lúc này:\n"
            "1) Excel lập tức treo và báo lỗi vì giới hạn tối đa chỉ 1,048,576 dòng.\n"
            "2) Pandas xử lý trên một luồng duy nhất của CPU (Single-threaded) và bắt buộc phải nạp toàn bộ tệp vào thanh RAM cục bộ của máy tính; khi dữ liệu lớn hơn RAM, máy sẽ bị lỗi sập bộ nhớ Out-Of-Memory (OOM).\n"
            "3) Hadoop HDFS cho phép lưu trữ không giới hạn nhờ ghép nối hàng trăm ổ cứng của các máy chủ thành một hệ thống tệp dùng chung, và Apache Spark chia nhỏ dữ liệu thành hàng ngàn phân vùng (Partitions) để xử lý song song trên nhiều CPU Core cùng lúc."
        ),
        (
            "Câu 2: Trong Hadoop HDFS, NameNode và DataNode hoạt động như thế nào? Nếu một DataNode bị hỏng ổ cứng thì dữ liệu có bị mất không?",
            "Đáp án: Kiến trúc HDFS tuân theo mô hình Master - Worker:\n"
            "• NameNode (Master Node): Đóng vai trò là 'bộ não', quản lý toàn bộ Metadata (siêu dữ liệu) của hệ thống: cây thư mục, quyền truy cập tệp và bảng phân giải ánh xạ xem mỗi Block dữ liệu đang được lưu trữ ở DataNode nào trên mạng. Toàn bộ Metadata này được giữ trong RAM của NameNode để phản hồi nhanh chóng.\n"
            "• DataNode (Worker Node): Là các máy chủ lưu trữ dữ liệu thực tế. Tệp tin khi nạp vào HDFS được xẻ nhỏ thành các khối Block cố định (mặc định 128MB trong Hadoop 2.x/3.x).\n"
            "Dữ liệu TUYỆT ĐỐI KHÔNG BỊ MẤT khi một DataNode bị cháy ổ cứng nhờ cơ chế Data Replication:\n"
            "HDFS tự động nhân bản mỗi Block thành 3 bản sao (Replication Factor = 3) nằm trên các DataNode và Rack (tủ máy chủ) khác nhau. Định kỳ mỗi 3 giây, DataNode phải gửi tín hiệu nhịp tim (Heartbeat) về cho NameNode. Nếu sau 10 phút NameNode không nhận được tín hiệu từ một DataNode, nó sẽ coi node đó đã chết và ngay lập tức ra lệnh cho các DataNode còn lại tự động nhân bản thêm bản sao mới từ các bản sao còn nguyên vẹn, đảm bảo hệ thống luôn duy trì đúng 3 bản sao chịu lỗi (Fault Tolerance)."
        ),
        (
            "Câu 3: Apache Spark khác gì so với Hadoop MapReduce cũ? Tại sao Spark lại chạy nhanh hơn từ 10 đến 100 lần?",
            "Đáp án: Sự khác biệt bản chất nằm ở cơ chế lưu trữ dữ liệu trung gian giữa các bước tính toán:\n"
            "• Hadoop MapReduce: Hoạt động theo chu trình cứng nhắc: Đọc đĩa -> Map -> Ghi đĩa trung gian -> Shuffle qua mạng -> Reduce -> Ghi đĩa kết quả HDFS. Mỗi vòng lặp tính toán đều phải đọc và ghi xuống ổ đĩa cứng (Disk I/O Bottleneck), khiến tốc độ xử lý rất chậm, đặc biệt là với các thuật toán lặp của Machine Learning.\n"
            "• Apache Spark: Áp dụng kiến trúc Tính toán trong bộ nhớ (In-Memory Computing). Dữ liệu sau khi nạp được giữ lại trong RAM dưới dạng cấu trúc RDD (Resilient Distributed Datasets) hoặc DataFrame. Spark chỉ ghi xuống ổ đĩa khi thực sự cần thiết hoặc khi bộ nhớ RAM bị đầy. Nhờ hạn chế tối đa việc đọc/ghi đĩa từ, Spark xử lý nhanh gấp 100 lần trong RAM và gấp 10 lần trên đĩa so với MapReduce."
        ),
        (
            "Câu 4: Tại sao ở Bước 4 em lại chuyển đổi định dạng từ CSV sang Apache Parquet? Định dạng Parquet có ưu điểm gì trong Big Data?",
            "Đáp án: Việc chuyển đổi sang Apache Parquet ở Bước 4 là bước chuẩn hóa tối quan trọng vì:\n"
            "1) Lưu trữ theo cột (Columnar Storage) thay vì theo dòng (Row-based) của CSV: Trong phân tích Big Data, người dùng thường chỉ chọn (SELECT) từ 3 đến 5 cột trên tổng số 35 cột. Với Parquet, Spark chỉ đọc đúng những cột cần thiết trên ổ cứng, bỏ qua hoàn toàn các cột còn lại. Ngược lại, với CSV, Spark bắt buộc phải đọc qua toàn bộ 35 cột của từng dòng, gây lãng phí băng thông đĩa.\n"
            "2) Tỷ lệ nén cực cao (Snappy Compression): Parquet gom nhóm các dữ liệu cùng kiểu trên cùng một cột lại với nhau, giúp thuật toán nén Snappy đạt hiệu quả tối đa, giảm dung lượng tệp từ 50% đến 75% so với CSV nguyên bản.\n"
            "3) Tối ưu hóa truy vấn thông minh: Parquet lưu sẵn thông tin Min, Max, Null Count cho từng khối dữ liệu trong Header/Footer. Nhờ đó, Spark thực hiện được cơ chế Predicate Pushdown: nếu câu lệnh SQL có điều kiện WHERE Age > 50, Spark sẽ kiểm tra Max của khối, nếu Max < 50 thì Spark bỏ qua hoàn toàn khối đó mà không cần đọc dữ liệu."
        ),
        (
            "Câu 5: Em giải quyết bài toán mất cân bằng dữ liệu (Imbalanced Data) như thế nào? Tại sao trong bài toán này không thể dùng Độ chính xác (Accuracy) làm thước đo duy nhất?",
            "Đáp án: Trong tập dữ liệu HR Analytics, tỷ lệ nhân viên nghỉ việc (Attrition = Yes) chỉ chiếm 16.12% (237 người), trong khi nhân viên ở lại (No) chiếm tới 83.88% (1,233 người), tức tỷ lệ chênh lệch là 1 : 5.2.\n"
            "• Cạm bẫy của Accuracy: Nếu một mô hình 'ngây thơ' chỉ cần dự đoán tất cả 1,470 nhân viên đều 'Không nghỉ việc', thì độ chính xác của mô hình vẫn đạt tới 83.88%! Nhưng mô hình này hoàn toàn vô dụng đối với doanh nghiệp vì nó đã bỏ lọt 100% nhân viên có ý định nghỉ việc thật sự (Độ nhạy Recall = 0%).\n"
            "• Giải pháp kỹ thuật của em: Em sử dụng kỹ thuật Balanced Class Weighting (Trọng số nghịch đảo tần suất lớp). Thuật toán tự động tính trọng số của lớp thiểu số cao gấp 5.2 lần lớp đa số. Khi mô hình dự đoán sai một ca nghỉ việc (False Negative), hàm mất mát (Loss Function) sẽ bị phạt nặng gấp 5.2 lần, ép thuật toán phải chú trọng nhận diện các nhân viên sắp rời đi.\n"
            "• Thước đo đánh giá: Em sử dụng chỉ số ROC-AUC (Area Under the ROC Curve) đạt ~0.80 và chỉ số Recall để đánh giá khả năng phân tách thực chất của mô hình thay vì phụ thuộc vào Accuracy."
        ),
        (
            "Câu 6: Vai trò của Apache Kafka ở Bước 8 và Apache Airflow ở Bước 9 là gì trong một kiến trúc Big Data toàn diện?",
            "Đáp án: \n"
            "• Apache Kafka (Tầng Streaming Ingestion - Cửa ngõ thu nhận dữ liệu dòng): Đóng vai trò là hệ thống môi giới thông điệp phân tán (Distributed Event Streaming Platform). Trong thực tế, các sự kiện nhân sự phát sinh liên tục: nhân viên quẹt thẻ trễ, nộp đơn xin nghỉ phép, ghi nhận làm thêm giờ (OT) lúc 22h đêm. Kafka Producer bắn các sự kiện này dạng JSON vào Topic 'hr-employee-events' với thông lượng hàng chục nghìn event/giây mà không làm nghẽn hệ thống. Spark Streaming sau đó đọc dòng sự kiện này để cập nhật điểm rủi ro ngay tức thì.\n"
            "• Apache Airflow (Tầng Orchestration - Nhạc trưởng điều phối): Airflow không trực tiếp lưu trữ hay tính toán dữ liệu thô, mà chịu trách nhiệm điều phối thứ tự thực thi của toàn bộ quy trình thông qua đồ thị có hướng không chu trình DAG. Airflow đảm bảo: Bước 2 chỉ chạy khi Bước 1 đã hoàn tất; nếu Bước 3 bị lỗi mạng, Airflow tự động thử lại (Retry) 3 lần, ghi log chi tiết và gửi thông báo qua Slack/Email; tự động lên lịch chạy định kỳ vào 00:00 hàng ngày (@daily)."
        ),
        (
            "Câu 7: Trình bày chi tiết công thức và ý nghĩa của các đặc trưng mới mà em tự tạo (Feature Engineering) ở Bước 4?",
            "Đáp án: Nhằm nâng cao năng lực dự đoán cho mô hình Machine Learning, em đã trích xuất thêm 2 đặc trưng nghiệp vụ quan trọng:\n"
            "1) Income_Per_WorkingYear (Thu nhập trung bình trên mỗi năm kinh nghiệm):\n"
            "   • Công thức: MonthlyIncome / (TotalWorkingYears + 1) (cộng 1 để tránh lỗi chia cho 0 với nhân viên mới vào nghề).\n"
            "   • Ý nghĩa nghiệp vụ: Thước đo đánh giá sự tương xứng giữa mức đãi ngộ tài chính so với bề dày kinh nghiệm và thâm niên cống hiến. Một nhân viên có 10 năm kinh nghiệm nhưng thu nhập chỉ tương đương nhân viên 2 năm kinh nghiệm sẽ có chỉ số này rất thấp, sinh ra tâm lý bất mãn và có nguy cơ nhảy việc cao nhất.\n"
            "2) Promotion_Lag_Ratio (Tỷ lệ chậm thăng tiến):\n"
            "   • Công thức: YearsSinceLastPromotion / (YearsAtCompany + 1).\n"
            "   • Ý nghĩa nghiệp vụ: Đo lường mức độ 'dậm chân tại chỗ' của nhân viên trong tổ chức. Nếu nhân viên làm việc 8 năm ở công ty mà 7 năm qua chưa từng được thăng chức (tỷ lệ gần 1.0), họ cảm thấy tương lai nghề nghiệp bị bế tắc và sẽ chủ động tìm kiếm cơ hội thăng tiến ở công ty đối thủ."
        ),
        (
            "Câu 8: Tại sao ở Bước 4 em lại loại bỏ 4 cột EmployeeCount, Over18, StandardHours và EmployeeNumber? Nếu giữ lại thì có tác hại gì?",
            "Đáp án: Việc loại bỏ 4 cột này dựa trên 2 nguyên lý tiền xử lý dữ liệu chuẩn:\n"
            "1) Cột không có tính phân biến (Zero-Variance Features): Các cột EmployeeCount (luôn luôn bằng 1), Over18 (luôn luôn bằng 'Y'), StandardHours (luôn luôn bằng 80) mang cùng một giá trị duy nhất trên toàn bộ 1,470 bản ghi. Về mặt toán học và lý thuyết thông tin, phương sai của chúng bằng 0 và lượng tin (Information Entropy) bằng 0. Nếu đưa vào mô hình, chúng chỉ làm tăng số chiều tính toán một cách vô ích mà không đóng góp bất kỳ giá trị phân loại nào.\n"
            "2) Cột định danh ngẫu nhiên (Identifier Feature - Data Leakage/Overfitting): Cột EmployeeNumber là mã số định danh tăng dần ngẫu nhiên của nhân viên. Cột này không mang tính quy luật hành vi nhân sự. Nếu để lại, các cây quyết định có thể vô tình tách nhánh theo ID cá nhân, dẫn đến hiện tượng học vẹt (Overfitting) khiến mô hình chạy rất tốt trên dữ liệu cũ nhưng dự đoán sai hoàn toàn trên dữ liệu nhân viên mới."
        ),
        (
            "Câu 9: Thuật toán Random Forest hoạt động như thế nào trong đồ án? Phân tích độ quan trọng của đặc trưng (Feature Importance)?",
            "Đáp án: \n"
            "• Nguyên lý hoạt động: Random Forest là thuật toán học kết hợp (Ensemble Learning) dựa trên kỹ thuật Bagging (Bootstrap Aggregating). Hệ thống khởi tạo một 'rừng' gồm 100 cây quyết định (n_estimators = 100). Mỗi cây được huấn luyện trên một tập mẫu con ngẫu nhiên được rút trích có hoàn lại từ tập dữ liệu gốc, và tại mỗi nút phân nhánh, thuật toán chỉ chọn ngẫu nhiên một tập con các đặc trưng. Kết quả dự đoán cuối cùng là sự biểu quyết đa số (Majority Voting) của tất cả 100 cây, giúp triệt tiêu hiện tượng Overfitting của một cây quyết định đơn lẻ.\n"
            "• Kết quả độ quan trọng đặc trưng (Feature Importance): Thuật toán đo lường mức độ giảm độ tinh khiết (Gini Impurity Reduction) và chỉ ra Top 3 yếu tố chi phối mạnh mẽ nhất đến quyết định nghỉ việc:\n"
            "   1. MonthlyIncome (7.52%): Mức thu nhập hàng tháng là động lực kinh tế trực tiếp nhất.\n"
            "   2. Age (6.81%): Độ tuổi trẻ (dưới 30 tuổi) có tính biến động công việc cao gấp 2.5 lần so với nhóm trung niên.\n"
            "   3. TotalWorkingYears (5.39%): Số năm kinh nghiệm phản ánh giai đoạn phát triển sự nghiệp của người lao động."
        ),
        (
            "Câu 10: Chấm điểm rủi ro (Risk Scoring) ở Bước 7 được tính như thế nào? Ngưỡng 70% có ý nghĩa gì và bộ phận HR sẽ làm gì với kết quả này?",
            "Đáp án: \n"
            "• Cơ chế tính toán: Thay vì chỉ đưa ra nhãn nhị phân (Yes/No), mô hình tính toán hàm xác suất predict_proba trên phân phối dự đoán của 100 cây quyết định, cho ra điểm số liên tục từ 0% đến 100% (ví dụ: nhân viên A có nguy cơ nghỉ việc là 84.5%).\n"
            "• Phân loại nhóm rủi ro:\n"
            "   - Nhóm an toàn (< 30%): Nhân sự ổn định, gắn bó.\n"
            "   - Nhóm cảnh báo (30% - 69%): Bắt đầu xuất hiện dấu hiệu quá tải công việc hoặc bất mãn.\n"
            "   - Nhóm nguy cơ cao (>= 70%): Nhóm có nguy cơ nộp đơn nghỉ việc trong vòng 3 đến 6 tháng tới.\n"
            "• Hành động can thiệp của HR (Actionable Insights): Danh sách high_risk_employees.csv được tự động gửi đến Giám đốc Nhân sự (CHRO). HR sẽ ngay lập tức triển khai chính sách giữ chân nhân tài (Retention Strategy) trước khi nhân viên nộp đơn: xem xét điều chỉnh lương thưởng, cắt giảm giờ làm thêm OverTime, luân chuyển sang dự án mới hoặc tổ chức buổi trò chuyện 1-1 thấu hiểu tâm tư."
        ),
        (
            "Câu 11: Cơ chế chịu lỗi (Fault Tolerance) của Apache Spark diễn ra như thế nào nếu trong quá trình xử lý có một máy chủ bị sập?",
            "Đáp án: Cơ chế chịu lỗi của Spark dựa trên khái niệm Đồ thị dòng dõi RDD (RDD Lineage Graph):\n"
            "Khi Spark thực hiện các phép biến đổi (Transformations như map, filter, select), nó không sao chép lại toàn bộ dữ liệu ra nhiều nơi như HDFS, mà chỉ ghi nhớ chuỗi các thao tác logic đã biến đổi dữ liệu dưới dạng đồ thị có hướng (DAG Lineage).\n"
            "Nếu một máy chủ Worker Node đang chạy Bước 4 hoặc Bước 6 bị sập nguồn hoặc mất kết nối mạng, các phân vùng (Partitions) dữ liệu trên thanh RAM của máy đó sẽ bị mất. Trình lập lịch của Spark (DAG Scheduler) lập tức phát hiện sự cố, tìm đến một Worker Node khỏe mạnh khác trong cụm và yêu cầu tính toán lại CHỈ RIÊNG các phân vùng bị mất bằng cách thực thi lại đồ thị Lineage từ dữ liệu nguồn HDFS ban đầu mà không cần phải chạy lại toàn bộ Job từ đầu."
        ),
        (
            "Câu 12: Giả sử quy mô công ty tăng từ 1,470 nhân viên lên 10 triệu nhân viên, hệ thống của em sẽ mở rộng (Scale-out) như thế nào?",
            "Đáp án: Kiến trúc Big Data của đồ án được thiết kế theo nguyên lý Mở rộng theo chiều ngang (Horizontal Scalability), cho phép nâng cấp hệ thống mà không cần sửa đổi mã nguồn:\n"
            "1) Tầng Storage (HDFS): Khi dữ liệu tăng từ Megabytes lên hàng chục Terabytes, ta chỉ cần gắn thêm các máy chủ DataNode vật lý giá rẻ vào cụm Hadoop. HDFS sẽ tự động tái cân bằng (HDFS Balancer) và phân bổ các Block 128MB sang các node mới.\n"
            "2) Tầng Processing (Spark): Tăng số lượng Spark Worker Nodes và số Executor Cores. Điều chỉnh thông số spark.sql.shuffle.partitions (mặc định 200) tăng lên 1,000 hoặc 2,000 partitions tương ứng với khối lượng dữ liệu để đảm bảo mỗi Partition có dung lượng lý tưởng từ 100MB đến 200MB trong RAM.\n"
            "3) Tầng Ingestion (Kafka): Tạo thêm các Partitions cho Topic 'hr-employee-events' và tăng số lượng Kafka Consumer trong Consumer Group để đọc song song dòng sự kiện chấm công của 10 triệu nhân viên."
        )
    ]

    for q, a in qa_list:
        p_q = doc.add_paragraph()
        p_q.paragraph_format.space_before = Pt(8)
        p_q.paragraph_format.space_after = Pt(2)
        r_q = p_q.add_run(q)
        r_q.bold = True
        r_q.font.size = Pt(11)
        r_q.font.color.rgb = COLOR_SECONDARY
        
        p_a = doc.add_paragraph()
        p_a.paragraph_format.space_after = Pt(8)
        r_a = p_a.add_run(a)
        r_a.font.size = Pt(10.5)

    add_section_heading("6.3. Bảng tra cứu thuật ngữ Big Data cốt lõi (Cheat Sheet)")

    term_table = doc.add_table(rows=10, cols=2)
    term_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    term_table.autofit = False

    terms_data = [
        ("Thuật ngữ Big Data", "Định nghĩa và ý nghĩa kỹ thuật ngắn gọn"),
        ("HDFS (Hadoop Distributed File System)", "Hệ thống tệp phân tán chia nhỏ tệp thành các khối Block 128MB lưu trữ trên nhiều máy chủ, tự động nhân bản chịu lỗi."),
        ("NameNode & DataNode", "NameNode quản lý Metadata trong RAM; DataNode lưu trữ các khối dữ liệu thực tế và gửi tín hiệu Heartbeat định kỳ 3 giây."),
        ("Replication Factor = 3", "Mỗi khối dữ liệu luôn được nhân bản thành 3 bản sao nằm trên các máy chủ và tủ rack khác nhau để bảo vệ an toàn dữ liệu."),
        ("In-Memory Computing", "Kỹ thuật tính toán giữ dữ liệu trung gian trong bộ nhớ RAM của Apache Spark, loại bỏ độ trễ đọc/ghi đĩa từ so với MapReduce."),
        ("RDD (Resilient Distributed Dataset)", "Cấu trúc dữ liệu phân tán cơ bản của Spark, bất biến (immutable), có khả năng tự phục hồi lỗi nhờ đồ thị dòng dõi (Lineage Graph)."),
        ("Columnar Storage (Parquet)", "Lưu trữ dữ liệu theo cột, hỗ trợ nén Snappy tiết kiệm 60% đĩa, tối ưu đọc riêng lẻ các cột thông qua Projection Pushdown."),
        ("Balanced Class Weighting", "Kỹ thuật gán trọng số nghịch đảo tần suất lớp để khắc phục mất cân bằng dữ liệu, phạt nặng mô hình khi bỏ sót lớp thiểu số."),
        ("ROC-AUC Score", "Diện tích dưới đường cong ROC, đánh giá năng lực phân loại tổng thể của mô hình bất chấp sự mất cân bằng giữa hai lớp."),
        ("Airflow DAG (Directed Acyclic Graph)", "Đồ thị có hướng không chu trình quản lý chuỗi phụ thuộc của các tác vụ, lên lịch tự động và xử lý thử lại (Retry) khi có lỗi.")
    ]

    for row_idx, (col1, col2) in enumerate(terms_data):
        row = term_table.rows[row_idx]
        c1, c2 = row.cells[0], row.cells[1]
        c1.width = Inches(2.2)
        c2.width = Inches(4.1)
        
        p1 = c1.paragraphs[0]
        p1.paragraph_format.space_after = Pt(2)
        r1 = p1.add_run(col1)
        r1.bold = True
        r1.font.size = Pt(10)
        
        p2 = c2.paragraphs[0]
        p2.paragraph_format.space_after = Pt(2)
        r2 = p2.add_run(col2)
        r2.font.size = Pt(9.5)
        
        if row_idx == 0:
            set_cell_shading(c1, "1E3A8A")
            set_cell_shading(c2, "1E3A8A")
            r1.font.color.rgb = RGBColor(255, 255, 255)
            r2.font.color.rgb = RGBColor(255, 255, 255)
        else:
            set_cell_shading(c1, "F1F5F9")
            set_cell_shading(c2, "FFFFFF" if row_idx % 2 == 1 else "F8FAFC")
            
        set_cell_margins(c1, top=50, bottom=50, left=70, right=70)
        set_cell_margins(c2, top=50, bottom=50, left=70, right=70)

    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    add_section_heading("6.4. Kịch bản thuyết trình bảo vệ đồ án mẫu trong 5 phút (Pitching Script)")

    pitching_content = (
        "«Kính thưa Thầy/Cô trong Hội đồng chấm thi,\n\n"
        "Em tên là Vũ Lê Anh Đức, MSSV 2001230191. Hôm nay em xin phép được báo cáo đồ án môn học Nhập môn Dữ liệu lớn với đề tài: "
        "'Xây dựng hệ thống Pipeline Big Data phân tích các yếu tố ảnh hưởng và dự đoán nguy cơ nghỉ việc của nhân viên'.\n\n"
        "1. VỀ BỐI CẢNH & MỤC TIÊU: Tình trạng nhân sự nhảy việc đột ngột gây tổn thất chi phí tuyển dụng và gián đoạn vận hành của doanh nghiệp. "
        "Mục tiêu của em là hiện thực hóa một hệ sinh thái Big Data 6 tầng công nghệ hoàn chỉnh theo đúng giáo trình: Ingestion, Storage, Processing, Query, ML và Orchestration.\n\n"
        "2. VỀ QUY TRÌNH PIPELINE 9 BƯỚC: \n"
        "• Tại tầng Lưu trữ (Storage), em thiết lập kiến trúc Medallion Data Lake trên HDFS với 3 phân vùng raw/, processed/, output/.\n"
        "• Tại tầng Thu thập (Ingestion), dữ liệu 1,470 nhân viên được đưa vào HDFS chia block 128MB chịu lỗi 3 bản sao. Đồng thời, ở Bước 8 em tích hợp Apache Kafka để mô phỏng thu nhận dữ liệu dòng sự kiện quẹt thẻ, chấm công thời gian thực.\n"
        "• Tại tầng Xử lý (Processing), Apache Spark nạp dữ liệu vào bộ nhớ RAM, lọc 4 cột phương sai bằng 0, tạo thêm 2 đặc trưng quan trọng là 'Thu nhập trên năm kinh nghiệm' và 'Tỷ lệ chậm thăng tiến', sau đó nén dạng cột Parquet Snappy giúp tiết kiệm hơn 60% bộ nhớ.\n"
        "• Tại tầng Phân tích & Học máy (Serving & ML), Spark SQL chỉ ra rằng nhân viên làm thêm giờ (OverTime) có tỷ lệ nghỉ việc gấp 3 lần bình thường (30.5% so với 10.4%). Em giải quyết vấn đề mất cân bằng dữ liệu (1 : 5.2) bằng kỹ thuật Balanced Class Weighting, huấn luyện mô hình Random Forest đạt ROC-AUC ~0.80 và xuất danh sách các nhân viên có rủi ro cao >= 70% để doanh nghiệp chủ động giữ chân nhân tài.\n"
        "• Cuối cùng tại tầng Điều phối (Orchestration), toàn bộ chu trình được tự động hóa 100% bằng Apache Airflow DAG theo lịch định kỳ hàng ngày.\n\n"
        "3. VỀ DEMO ỨNG DỤNG: Em đã xây dựng một giao diện Web Dashboard 3 cột trực quan tại localhost:5000 gồm: Workspace HDFS, 9 Thẻ tiến trình và Terminal thực thi theo thời gian thực.\n\n"
        "Em xin chân thành cảm ơn Thầy/Cô đã lắng nghe và rất mong nhận được những góp ý, câu hỏi phản biện từ Hội đồng ạ!»"
    )

    p_pitch = doc.add_paragraph()
    r_pitch = p_pitch.add_run(pitching_content)
    r_pitch.font.size = Pt(10.5)
    r_pitch.italic = True
    p_pitch.paragraph_format.space_after = Pt(12)

    output_docx_path = "D:\\Doan_BigData\\BaoCao_HeThong_BigData_PhanTich_NhanSu.docx"
    doc.save(output_docx_path)
    print(f"\n[OK] ĐÃ CẬP NHẬT TOÀN DIỆN TÀI LIỆU WORD TẠI: {output_docx_path}")
    print(f"     Dung lượng tệp: {os.path.getsize(output_docx_path) / 1024:.2f} KB\n")

if __name__ == "__main__":
    create_document()
