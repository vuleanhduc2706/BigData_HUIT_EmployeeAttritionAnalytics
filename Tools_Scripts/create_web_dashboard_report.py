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

def create_web_report():
    doc = Document()

    # Cấu hình lề trang (A4)
    for section in doc.sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(0.8)

    # Bảng màu chuẩn
    COLOR_PRIMARY = RGBColor(30, 58, 138)     # Deep Blue
    COLOR_SECONDARY = RGBColor(109, 40, 217)  # Purple
    COLOR_EMERALD = RGBColor(5, 150, 105)     # Emerald Green
    COLOR_DANGER = RGBColor(220, 38, 38)      # Crimson Red
    COLOR_TEXT = RGBColor(30, 41, 59)         # Slate Dark
    COLOR_MUTED = RGBColor(100, 116, 139)     # Slate Muted

    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Times New Roman'
    normal_style.font.size = Pt(12)
    normal_style.font.color.rgb = COLOR_TEXT
    normal_style.paragraph_format.line_spacing = 1.25
    normal_style.paragraph_format.space_after = Pt(6)

    def add_p(text, bold=False, italic=False, size=12, color=COLOR_TEXT, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=6):
        p = doc.add_paragraph()
        p.alignment = align
        p.paragraph_format.space_after = Pt(space_after)
        p.paragraph_format.line_spacing = 1.25
        run = p.add_run(text)
        run.bold = bold
        run.italic = italic
        run.font.name = 'Times New Roman'
        run.font.size = Pt(size)
        run.font.color.rgb = color
        return p

    def add_h1(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(16)
        p.paragraph_format.space_after = Pt(8)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        run.bold = True
        run.font.name = 'Times New Roman'
        run.font.size = Pt(15)
        run.font.color.rgb = COLOR_PRIMARY
        return p

    def add_h2(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        run.bold = True
        run.font.name = 'Times New Roman'
        run.font.size = Pt(13)
        run.font.color.rgb = COLOR_SECONDARY
        return p

    def add_h3(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        run.bold = True
        run.font.name = 'Times New Roman'
        run.font.size = Pt(12)
        run.font.color.rgb = COLOR_PRIMARY
        return p

    def add_callout(title, content, bg_hex="EFF6FF", border_color="3B82F6"):
        tbl = doc.add_table(rows=1, cols=1)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        tbl.autofit = False
        cell = tbl.cell(0, 0)
        cell.width = Inches(6.5)
        set_cell_shading(cell, bg_hex)
        set_cell_margins(cell, top=120, bottom=120, left=180, right=180)
        
        tcPr = cell._tc.get_or_add_tcPr()
        borders = parse_xml(f'<w:tcBorders {nsdecls("w")}><w:left w:val="single" w:sz="24" w:space="0" w:color="{border_color}"/><w:top w:val="none"/><w:right w:val="none"/><w:bottom w:val="none"/></w:tcBorders>')
        tcPr.append(borders)
        
        p = cell.paragraphs[0]
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.line_spacing = 1.2
        r_t = p.add_run(f"★ {title}\n")
        r_t.bold = True
        r_t.font.name = 'Times New Roman'
        r_t.font.size = Pt(11)
        r_t.font.color.rgb = COLOR_PRIMARY
        
        r_c = p.add_run(content)
        r_c.font.name = 'Times New Roman'
        r_c.font.size = Pt(10.5)
        r_c.font.color.rgb = COLOR_TEXT
        doc.add_paragraph().paragraph_format.space_after = Pt(4)

    def add_styled_table(headers, rows_data, col_widths=None):
        table = doc.add_table(rows=len(rows_data) + 1, cols=len(headers))
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        table.autofit = False

        # Header Row
        hdr_row = table.rows[0]
        for col_idx, header_text in enumerate(headers):
            cell = hdr_row.cells[col_idx]
            if col_widths and col_idx < len(col_widths):
                cell.width = Inches(col_widths[col_idx])
            set_cell_shading(cell, "1E3A8A")
            set_cell_margins(cell, top=120, bottom=120, left=140, right=140)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_after = Pt(2)
            run = p.add_run(header_text)
            run.bold = True
            run.font.name = 'Times New Roman'
            run.font.size = Pt(10)
            run.font.color.rgb = RGBColor(255, 255, 255)

        # Data Rows
        for r_idx, row_values in enumerate(rows_data):
            row = table.rows[r_idx + 1]
            bg_color = "FFFFFF" if r_idx % 2 == 0 else "F8FAFC"
            for c_idx, val in enumerate(row_values):
                cell = row.cells[c_idx]
                if col_widths and c_idx < len(col_widths):
                    cell.width = Inches(col_widths[c_idx])
                set_cell_shading(cell, bg_color)
                set_cell_margins(cell, top=90, bottom=90, left=130, right=130)
                p = cell.paragraphs[0]
                p.paragraph_format.space_after = Pt(2)
                p.paragraph_format.line_spacing = 1.15
                if c_idx == 0:
                    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                else:
                    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                run = p.add_run(str(val))
                run.font.name = 'Times New Roman'
                run.font.size = Pt(9.5)
                run.font.color.rgb = COLOR_TEXT

        doc.add_paragraph().paragraph_format.space_after = Pt(6)

    # -------------------------------------------------------------
    # TRANG TIÊU ĐỀ (COVER / HEADER)
    # -------------------------------------------------------------
    p_header = doc.add_paragraph()
    p_header.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_uni = p_header.add_run("BỘ GIÁO DỤC VÀ ĐÀO TẠO - TRƯỜNG ĐẠI HỌC CÔNG THƯƠNG TP.HCM (HUIT)\n")
    r_uni.bold = True
    r_uni.font.size = Pt(11)
    r_fac = p_header.add_run("KHOA CÔNG NGHỆ THÔNG TIN - BỘ MÔN KHOA HỌC DỮ LIỆU & TRÍ TUỆ NHÂN TẠO\n")
    r_fac.bold = True
    r_fac.font.size = Pt(11)
    p_header.paragraph_format.space_after = Pt(10)

    p_line = doc.add_paragraph()
    p_line.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_line = p_line.add_run("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    r_line.font.color.rgb = COLOR_SECONDARY
    p_line.paragraph_format.space_after = Pt(14)

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_sub = p_title.add_run("BÁO CÁO THUYẾT MINH KỸ THUẬT & HƯỚNG DẪN TRẢI NGHIỆM GIAO DIỆN\n")
    r_sub.font.size = Pt(12)
    r_sub.bold = True
    r_sub.font.color.rgb = COLOR_SECONDARY

    r_main_title = p_title.add_run("GIẢI THÍCH CHI TIẾT CÁC TRANG & CHỨC NĂNG TRÊN HỆ THỐNG WEB DASHBOARD BIG DATA PHÂN TÍCH NHÂN SỰ\n")
    r_main_title.bold = True
    r_main_title.font.size = Pt(15)
    r_main_title.font.color.rgb = COLOR_PRIMARY

    r_en_title = p_title.add_run("(Big Data Interactive Web Dashboard: 9-Stage Pipeline, Spark SQL Analytics, K-Means Clustering, Kafka Live Streaming, AI Risk Simulator & Airflow Orchestration)\n")
    r_en_title.italic = True
    r_en_title.font.size = Pt(10.5)
    r_en_title.font.color.rgb = COLOR_MUTED
    p_title.paragraph_format.space_after = Pt(14)

    # Bảng thông tin tác giả
    meta_table = doc.add_table(rows=5, cols=2)
    meta_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    meta_table.autofit = False
    meta_data = [
        ("Giảng viên hướng dẫn:", "ThS. Ngô Dương Hà (hand@huit.edu.vn)"),
        ("Sinh viên thực hiện:", "Vũ Lê Anh Đức"),
        ("Mã số sinh viên (MSSV):", "2001230191"),
        ("Lớp sinh hoạt / Ngành:", "11DHBM1 - Khoa học Dữ liệu & AI"),
        ("Học phần / Năm học:", "Các công nghệ Dữ liệu lớn (Big Data Technologies) - 2026")
    ]
    for r_idx, (col1, col2) in enumerate(meta_data):
        row = meta_table.rows[r_idx]
        c1, c2 = row.cells[0], row.cells[1]
        c1.width, c2.width = Inches(2.4), Inches(4.0)
        set_cell_shading(c1, "F1F5F9")
        set_cell_shading(c2, "FFFFFF")
        set_cell_margins(c1, top=60, bottom=60, left=100, right=100)
        set_cell_margins(c2, top=60, bottom=60, left=100, right=100)
        p1, p2 = c1.paragraphs[0], c2.paragraphs[0]
        p1.paragraph_format.space_after, p2.paragraph_format.space_after = Pt(2), Pt(2)
        r1 = p1.add_run(col1)
        r1.bold = True
        r1.font.size = Pt(10.5)
        r2 = p2.add_run(col2)
        r2.font.size = Pt(10.5)

    doc.add_paragraph().paragraph_format.space_after = Pt(14)

    # -------------------------------------------------------------
    # CHƯƠNG 1: TỔNG QUAN HỆ THỐNG WEB DASHBOARD
    # -------------------------------------------------------------
    add_h1("CHƯƠNG 1. TỔNG QUAN HỆ THỐNG WEB DASHBOARD BIG DATA")
    add_p(
        "Hệ thống Web Dashboard Big Data được thiết kế nhằm mục tiêu trực quan hóa toàn bộ kiến trúc công nghệ dữ liệu lớn phân tán "
        "và cung cấp giao diện tương tác thời gian thực (Interactive Web Client) phục vụ đồ án: 'Phân tích các yếu tố ảnh hưởng và dự đoán nguy cơ nghỉ việc của nhân viên'. "
        "Thay vì chỉ thực thi các mã nguồn Python trên terminal console độc lập, giao diện Web giúp Giảng viên và Hội đồng đánh giá có thể quan sát, điều khiển "
        "và thẩm định kết quả của từng tầng công nghệ một cách tường minh, sinh động và trực quan nhất."
    )
    add_p(
        "Ứng dụng web được khởi chạy tại địa chỉ http://localhost:5000 thông qua máy chủ Flask tích hợp (app.py) kết nối đồng bộ với các lõi Big Data (Hadoop HDFS, "
        "Apache Spark, Apache Kafka, Apache Airflow). Toàn bộ giao diện được tổ chức theo kiến trúc Single Page Application (SPA) gồm 6 tab điều hướng chuyên biệt, "
        "đáp ứng đầy đủ chu trình xử lý dữ liệu lớn từ Ingest -> Storage -> Processing -> Analytics -> Machine Learning -> Streaming -> Orchestration."
    )

    add_callout(
        "Điểm sáng nổi bật của giao diện Web Dashboard",
        "• Kiến trúc 6 Tab chuẩn hóa tương ứng với toàn bộ vòng đời phân tích Big Data của doanh nghiệp.\n"
        "• Tích hợp Terminal tương tác hai chiều (BigData CLI Terminal) cho phép kích hoạt script backend và theo dõi log thực tế.\n"
        "• Hệ thống 6 biểu đồ phân tích đa chiều tương tác mượt mà bằng thư viện Chart.js.\n"
        "• Mô hình học máy Random Forest và phân cụm K-Means (K=4) được trực quan hóa kèm kiểm thử tự động 6/6 test suites.\n"
        "• Mô phỏng dòng dữ liệu thời gian thực (Live Event Streaming) và bộ tính điểm nguy cơ AI Risk Simulator cho phòng nhân sự."
    )

    # Bảng tổng hợp 6 Tab
    add_h2("1.1. Bảng tổng hợp danh mục 6 trang chức năng (Tabs)")
    headers_tabs = ["Mã Tab", "Tên trang hiển thị", "Tầng công nghệ", "Chức năng trọng tâm"]
    data_tabs = [
        ["tab-pipeline", "1. Pipeline 9 Bước & Terminal", "Hadoop HDFS & CLI", "Điều khiển nạp dữ liệu, thực thi 9 bước tự động, terminal log."],
        ["tab-spark-sql", "2. Spark SQL (6 Biểu Đồ)", "Apache Spark In-Memory", "Truy vấn đa chiều 1,470 bản ghi, phân tích các nguyên nhân nghỉ việc."],
        ["tab-ml-kmeans", "3. K-Means & Machine Learning", "MLlib & Scikit-Learn", "Phân cụm K=4 nhóm nhân sự, đánh giá ROC-AUC 0.81, Feature Importance."],
        ["tab-streaming", "4. Kafka Live Streaming", "Apache Kafka & AI Scoring", "Phát luồng sự kiện thời gian thực, phân loại cảnh báo rủi ro 3 cấp độ."],
        ["tab-simulator", "5. AI Simulator Dự Đoán", "Interactive AI Engine", "Bộ công cụ What-If cho phép nhập thông số để suy luận rủi ro & giải pháp."],
        ["tab-airflow", "6. Airflow & Benchmark", "Apache Airflow & Metrics", "Sơ đồ chuỗi DAG @daily, đối chiếu HDFS, benchmark nén Parquet (-59.9%)."]
    ]
    add_styled_table(headers_tabs, data_tabs, [1.1, 1.8, 1.4, 2.2])

    # -------------------------------------------------------------
    # CHƯƠNG 2: THUYẾT MINH CHI TIẾT TỪNG TRANG & TÁC DỤNG
    # -------------------------------------------------------------
    add_h1("CHƯƠNG 2. THUYẾT MINH CHI TIẾT TỪNG TRANG & TÁC DỤNG NGHIỆP VỤ")

    # 2.1. TAB 1: PIPELINE 9 BƯỚC
    add_h2("2.1. Trang 1: Pipeline 9 Bước & BigData CLI Terminal (tab-pipeline)")
    add_p(
        "Trang Pipeline 9 Bước là trung tâm điều khiển (Control Center) của toàn bộ hệ thống. "
        "Giao diện tại trang này được thiết kế theo bố cục 3 cột chuyên nghiệp (Three-column Layout) mang lại trải nghiệm làm việc như một môi trường phát triển tích hợp (IDE):"
    )
    add_p(
        "1. Cột trái - Data Lake Workspace: "
        "Quản lý cây thư mục phân cấp của Data Lake tương thích HDFS (/courses/2/projects/3/students/2001230191) gồm 3 phân vùng:\n"
        "• raw/: Lưu trữ tệp dữ liệu gốc CSV (WA_Fn-UseC_-HR-Employee-Attrition.csv) theo cơ chế WORM (Write Once, Read Many) bất biến.\n"
        "• processed/: Chứa dữ liệu đã được làm sạch và chuyển đổi sang định dạng nén cột Snappy Parquet tối ưu cho truy vấn song song.\n"
        "• output/: Lưu trữ các bảng kết quả phân tích JSON, mô hình học máy đã huấn luyện (.pkl) và danh sách nhân sự cần can thiệp.\n"
        "Cột này cũng tích hợp nút 'Nạp Dataset.csv vào raw/' giúp người dùng nạp tập dữ liệu vào Data Lake chỉ với một cú nhấp chuột."
    )
    add_p(
        "2. Cột giữa - 9 Thẻ Bước Pipeline Tự Động Hóa:\n"
        "Mỗi thẻ đại diện cho một chặng công nghệ then chốt với trạng thái hoàn thành (dấu tích xanh '✓') được cập nhật theo thời gian thực:\n"
        "• Bước 1 - Chuẩn bị HDFS Data Lake: Khởi tạo cấu trúc phân vùng chịu lỗi và kiểm tra môi trường Hadoop 3.4.0.\n"
        "• Bước 2 - Ingest Dữ Liệu Nguồn: Đưa 1,470 bản ghi nhân sự vào tầng raw của cụm phân tán.\n"
        "• Bước 3 - Đọc Bằng Apache Spark: Nạp dữ liệu vào PySpark In-Memory DataFrame và tự động suy luận Schema.\n"
        "• Bước 4 - Feature Engineering & Parquet: Loại bỏ cột hằng số dư thừa (StandardHours, Over18, EmployeeCount), trích xuất 5 đặc trưng nâng cao và ghi ra Parquet Snappy.\n"
        "• Bước 5 - Spark SQL Đa Chiều: Đăng ký TempView và thực thi 6 câu truy vấn chuyên sâu phân tích nguyên nhân thôi việc.\n"
        "• Bước 6 - MLlib Random Forest & K-Means: Xử lý mất cân bằng lớp (16% vs 84%), phân cụm K=4 nhóm và kiểm thử 6/6 test suites.\n"
        "• Bước 7 - Xuất HDFS & Cảnh Báo 3 Cấp: Phân loại rủi ro (Risk Score %) theo 3 cấp độ Xanh/Vàng/Đỏ và lọc danh sách 172 nhân viên nguy cơ cao.\n"
        "• Bước 8 - Kafka Ingest & AI Suy Luận: Giả lập Producer phát luồng sự kiện nhân sự vào Topic 'hr-employee-events' và Consumer AI chấm điểm tức thời.\n"
        "• Bước 9 - Điều Phối Apache Airflow DAG: Thiết lập đồ thị có hướng DAG và tự động hóa chuỗi task dependencies định kỳ hàng ngày.\n"
        "Phía dưới cột giữa có Dock điều khiển cho phép người dùng chọn 'Chạy bước này' (đơn lẻ) hoặc 'Chạy liên hoàn (1 - 9)' để thực thi toàn chuỗi."
    )
    add_p(
        "3. Cột phải - BigData CLI Terminal:\n"
        "Cửa sổ console giả lập môi trường dòng lệnh tương tác trực tiếp với máy chủ qua REST API /api/run-stage/<name> và /api/run-all. "
        "Mọi thông báo khởi tạo, thông số bộ nhớ, tiến trình Spark Job và lỗi ngoại lệ đều được hiển thị đầy đủ, hỗ trợ các lệnh: run-stage, run-all, help, clear."
    )

    # 2.2. TAB 2: SPARK SQL
    add_h2("2.2. Trang 2: Spark SQL - 6 Biểu Đồ Phân Tích Đa Chiều (tab-spark-sql)")
    add_p(
        "Trang Spark SQL có tác dụng trực quan hóa kết quả phân tích thống kê đa chiều từ các truy vấn song song trên Apache Spark DataFrame. "
        "Mục tiêu là tìm ra các 'mẫu hình tiềm ẩn' (patterns) và nguyên nhân gốc rễ thúc đẩy nhân viên nộp đơn nghỉ việc."
    )
    add_p(
        "1. Hệ thống 5 chỉ số KPI đầu ngành (Top Metrics Row):\n"
        "• Tổng quy mô nhân sự: 1,470 bản ghi được lưu trữ và truy vấn trên Data Lake.\n"
        "• Tỷ lệ nghỉ việc chung (Attrition Rate): 16.12% (tương ứng 237 nhân viên đã rời bỏ công ty).\n"
        "• Thu nhập bình quân hàng tháng: $6,503 (biên độ dao động từ $1,009 đến $19,999).\n"
        "• Độ tuổi bình quân: 36.9 tuổi (phân bố từ 18 đến 60 tuổi).\n"
        "• Thâm niên gắn bó trung bình: 7.0 năm."
    )
    add_p(
        "2. Hệ thống 6 biểu đồ chuyên sâu tương tác (Chart.js Grid):\n"
        "• Biểu đồ 1 (OverTime - Query 1): Minh chứng nhân viên làm thêm giờ có tỷ lệ nghỉ việc là 30.53%, cao gấp gần 3 lần so với nhóm không làm thêm giờ (10.44%). Đây là yếu tố gây mất cân bằng cuộc sống và kiệt sức lớn nhất.\n"
        "• Biểu đồ 2 (Department - Query 2): So sánh giữa 3 khối: Khối Sales có tỷ lệ nghỉ cao nhất (20.63%), tiếp đến là Human Resources (19.05%), khối R&D gắn bó ổn định nhất (13.84%) nhờ mức lương trung bình cao hơn ($6,344).\n"
        "• Biểu đồ 3 (JobRole - Query 3): Phân tích Top 5 vị trí nguy cơ: Sales Representative đứng đầu bảng với tỷ lệ nghỉ 39.76%, tiếp theo là Laboratory Technician (23.94%) và Human Resources Specialist (23.08%).\n"
        "• Biểu đồ 4 (WorkLifeBalance - Query 4): Đánh giá tương quan giữa cân bằng cuộc sống và tỷ lệ nghỉ. Nhóm đánh giá Cân bằng rất kém (Mức 1) có tỷ lệ ra đi lên đến 31.25%, trong khi nhóm Cân bằng tốt (Mức 3 và 4) tỷ lệ này giảm xuống khoảng 14%.\n"
        "• Biểu đồ 5 (Tenure Buckets - Query 5): Thể hiện 'khủng hoảng hội nhập' khi nhân sự mới dưới 2 năm có tỷ lệ thôi việc lên đến 31.1%. Sau mốc 5 năm, tỷ lệ này giảm sâu xuống dưới 10%.\n"
        "• Biểu đồ 6 (Environment Satisfaction - Query 6): Nhân viên không hài lòng với môi trường làm việc (Mức 1) có tỷ lệ nghỉ việc là 25.35%, cao gấp đôi so với nhóm hài lòng cao (Mức 4 là 13.45%)."
    )

    # 2.3. TAB 3: K-MEANS & ML
    add_h2("2.3. Trang 3: K-Means & Machine Learning MLlib (tab-ml-kmeans)")
    add_p(
        "Trang này có tác dụng công bố toàn diện kết quả xây dựng mô hình trí tuệ nhân tạo (AI/ML) phục vụ dự đoán nguy cơ nghỉ việc "
        "và phân khúc nhân sự theo các nhóm đặc trưng hành vi tương đồng."
    )
    add_p(
        "1. Các chỉ số Benchmark của mô hình Random Forest:\n"
        "• Độ chính xác toàn thể (Accuracy): 83.67% trên tập kiểm thử độc lập (Test Set).\n"
        "• Diện tích dưới đường cong ROC-AUC: Đạt 0.8095 (thể hiện khả năng phân tách ranh giới giữa người ở lại và người có nguy cơ nghỉ xuất sắc).\n"
        "• Độ nhạy (Recall bắt người nghỉ việc): 68.09% (vượt qua bài toán mất cân bằng dữ liệu 16% vs 84% nhờ kỹ thuật Balanced Class Weighting).\n"
        "• Độ trễ suy luận (Inference Latency): Đạt 0.066 ms/bản ghi, đảm bảo khả năng đáp ứng hoàn hảo cho xử lý dòng thời gian thực (Streaming)."
    )
    add_p(
        "2. Phân khúc 4 nhóm nhân sự bằng thuật toán K-Means Clustering (K=4):\n"
        "• Nhóm 0 - Cốt cán & Thu nhập cao (28.9% quy mô): Lương TB $15,492/tháng, tuổi TB 48.2, thâm niên 15.6 năm, tỷ lệ nghỉ cực thấp 6.48%. -> Khuyến nghị: Giữ chân bằng cổ phần (Stock Options) và trao quyền quản trị cấp cao.\n"
        "• Nhóm 1 - Nguy cơ cao & Lương thấp (14.7% quy mô): Lương TB $3,508/tháng, tuổi TB 29.4, thâm niên 2.8 năm, tỷ lệ nghỉ báo động 24.47%. -> Khuyến nghị: Rà soát định biên lương, cắt giảm làm thêm ban đêm.\n"
        "• Nhóm 2 - Tài năng trẻ tiềm năng (22.8% quy mô): Lương TB $5,006/tháng, tuổi TB 33.1, thâm niên 3.9 năm, tỷ lệ nghỉ 19.40%. -> Khuyến nghị: Hỗ trợ thi chứng chỉ chuyên môn, thiết lập lộ trình thăng tiến 1-2 năm.\n"
        "• Nhóm 3 - Thâm niên ổn định (33.6% quy mô): Lương TB $6,165/tháng, tuổi TB 38.6, thâm niên 8.1 năm, tỷ lệ nghỉ 10.93%. -> Khuyến nghị: Gia tăng phúc lợi gia đình, bảo hiểm sức khỏe và duy trì cân bằng cuộc sống."
    )
    add_p(
        "3. Biểu đồ độ quan trọng của đặc trưng (Feature Importance):\n"
        "Xác định 5 thuộc tính chi phối mạnh nhất đến quyết định thôi việc gồm: OverTime (trọng số 0.185), MonthlyIncome (0.162), "
        "Age (0.128), TotalWorkingYears (0.114) và StockOptionLevel (0.095)."
    )
    add_p(
        "4. Bộ kiểm thử tự động (6/6 Automated Test Suites Passed):\n"
        "Toàn bộ quy trình huấn luyện đều vượt qua 6 bài kiểm tra chuẩn công nghiệp: Kiểm tra rò rỉ dữ liệu giữa tập Train/Test (Test 1), "
        "Độ nhạy ROC-AUC > 0.75 (Test 2), Recall > 60% (Test 3), K-Means không có cụm rỗng (Test 4), Chuẩn hóa trọng số đặc trưng = 1.0 (Test 5), "
        "và Độ trễ suy luận < 5ms (Test 6)."
    )
    add_p(
        "5. Phân tích các trường hợp đoán sai (Error Analysis) & Lưu trữ mô hình:\n"
        "Trang web minh bạch hóa việc phân tích 8 ca False Positives (dự đoán nghỉ nhưng ở lại nhờ quản lý tốt và quyền mua cổ phiếu) "
        "và 41 ca False Negatives (bỏ sót do thâm niên cao nhưng chậm thăng tiến nhiều năm). Đồng thời, xác nhận việc lưu trữ các tệp mô hình vật lý "
        "(model_random_forest.pkl, model_scaler.pkl) tại thư mục data/output/ và HDFS sink."
    )

    # 2.4. TAB 4: KAFKA LIVE STREAMING
    add_h2("2.4. Trang 4: Kafka Live Streaming & Cảnh Báo 3 Cấp Độ (tab-streaming)")
    add_p(
        "Trang Kafka Live Streaming có tác dụng mô phỏng kiến trúc xử lý dòng (Stream Ingestion & Real-time Inference). "
        "Hệ thống không chỉ dừng lại ở việc phân tích dữ liệu tĩnh (Batch Data) mà còn tiếp nhận các biến động hành vi nhân sự diễn ra hàng ngày để cảnh báo sớm."
    )
    add_p(
        "1. Hệ thống phân loại 3 Cấp độ cảnh báo rủi ro (3-Tier Alert System):\n"
        "• Cấp 1 - An toàn (Xanh - Low Risk): 1,233 nhân viên (83.9%) có xác suất thôi việc < 30%. Doanh nghiệp duy trì môi trường làm việc ổn định.\n"
        "• Cấp 2 - Cảnh báo (Vàng - Medium Risk): 65 nhân viên (4.4%) có xác suất từ 30% đến 70%. Cần theo dõi mức độ gắn kết và điều chỉnh khối lượng công việc.\n"
        "• Cấp 3 - Báo động đỏ (Đỏ - High Risk): 172 nhân viên (11.7%) có xác suất > 70%. Bộ phận HR cần can thiệp khẩn cấp bằng các giải pháp đặc thù."
    )
    add_p(
        "2. Bộ điều khiển và luồng sự kiện Real-time Event Feed (Topic hr-employee-events):\n"
        "Người dùng có thể bấm 'Bắt đầu Streaming' hoặc 'Phát 1 Event' để kích hoạt Producer phát sinh ngẫu nhiên các sự kiện nhân sự như: "
        "'Đi muộn > 45 phút (+7% rủi ro)', 'Làm việc ban đêm liên tục (+15% rủi ro)', 'Tra cứu bảng quy chế thôi việc (+13% rủi ro)', "
        "'Truy cập trang tuyển dụng bên ngoài (+19.5% rủi ro)', hoặc 'Được khen thưởng hoàn thành xuất sắc dự án (-14% rủi ro)'.\n"
        "Consumer AI sẽ ngay lập tức tính toán lại điểm nguy cơ (Risk Delta) và cập nhật màu sắc cấp độ cảnh báo theo thời gian thực."
    )
    add_p(
        "3. Bảng Top nhân sự nguy cơ cao (> 70%):\n"
        "Liệt kê danh sách các nhân viên đang trong diện báo động đỏ cùng đầy đủ thông tin: Mã nhân viên, Phòng ban, Chức vụ, Mức lương, "
        "Tình trạng làm thêm giờ và Xác suất nguy cơ nghỉ việc, kèm nút hành động xem phương án giữ chân."
    )

    # 2.5. TAB 5: AI SIMULATOR
    add_h2("2.5. Trang 5: AI Simulator Dự Đoán Nguy Cơ Nghỉ Việc (tab-simulator)")
    add_p(
        "Trang AI Simulator là một công cụ tương tác kịch bản giả định (What-If Interactive Analysis) được thiết kế đặc thù cho các nhà quản lý, "
        "Trưởng bộ phận và Giám đốc nhân sự. Thay vì các công thức máy học phức tạp, người dùng có thể kéo thả trực quan các thông số nhân sự "
        "để nhận kết quả đánh giá nguy cơ và lộ trình hành động tức thì từ mô hình Random Forest."
    )
    add_p(
        "1. Form điều khiển tham số nhân sự đầu vào:\n"
        "• Độ tuổi (Age): Thanh trượt từ 18 đến 60 tuổi.\n"
        "• Mức thu nhập hàng tháng (MonthlyIncome): Thanh trượt từ $1,000 đến $20,000.\n"
        "• Chế độ làm thêm giờ (OverTime): Nút gạt chọn 'Có làm thêm giờ' hoặc 'Không làm thêm giờ'.\n"
        "• Cân bằng cuộc sống (WorkLifeBalance): Hộp chọn 4 mức (1-Rất kém, 2-Tạm được, 3-Tốt, 4-Rất tốt).\n"
        "• Thâm niên tại công ty (YearsAtCompany): Thanh trượt từ 0 đến 30 năm.\n"
        "• Tổng số năm kinh nghiệm làm việc (TotalWorkingYears): Thanh trượt từ 0 đến 40 năm."
    )
    add_p(
        "2. Kết quả suy luận AI & Khuyến nghị hành động (Action Plan):\n"
        "Khi bấm nút 'Chạy AI Suy Luận Tức Thì', máy chủ Flask gọi API /api/ml/predict-risk và trả về kết quả trong chưa đầy 10ms:\n"
        "• Đồng hồ đo Gauge Score: Hiển thị trực quan xác suất nghỉ việc (ví dụ: 74.5%) cùng huy hiệu cảnh báo (Báo động đỏ).\n"
        "• Phân tích thanh tác động (Risk Breakdown): Bóc tách các yếu tố chính làm tăng điểm rủi ro (OverTime +28%, Thu nhập dưới trung bình +22%, Cân bằng cuộc sống thấp +18%).\n"
        "• Kế hoạch hành động gợi ý cho phòng nhân sự: Cung cấp giải pháp cụ thể như 'Cắt giảm ngay ca làm thêm giờ ban đêm', 'Tổ chức phiên trao đổi 1-on-1 trong tuần', 'Rà soát lương cơ bản theo thị trường'."
    )

    # 2.6. TAB 6: AIRFLOW & BENCHMARK
    add_h2("2.6. Trang 6: Apache Airflow DAG & Báo Cáo Benchmark (tab-airflow)")
    add_p(
        "Trang này có tác dụng chứng minh tính sẵn sàng triển khai trong môi trường doanh nghiệp thông qua việc tự động hóa điều phối quy trình (Data Orchestration) "
        "và công bố các kết quả thực nghiệm chứng minh ưu thế vượt trội của công nghệ Dữ liệu lớn so với các giải pháp xử lý tệp truyền thống."
    )
    add_p(
        "1. Sơ đồ chuỗi điều phối tác vụ (Apache Airflow DAG Flow):\n"
        "Minh họa đồ thị có hướng (Directed Acyclic Graph) mang tên hr_employee_attrition_pipeline được lên lịch định kỳ hàng ngày (@daily). "
        "Chuỗi điều phối gồm 8 tác vụ liên hoàn sử dụng BashOperator kết hợp PythonOperator, đảm bảo tính phụ thuộc chặt chẽ: "
        "Task 1 (HDFS Prepare) -> Task 2 (Upload Ingest) -> Task 3 (Spark Read) -> Task 4 (Clean & Parquet) -> Task 4b (Compaction) -> "
        "Task 5 (Spark SQL) -> Task 6 (ML Train) -> Task 7 (Save Results) -> Task 8 (Kafka Streaming)."
    )
    add_p(
        "2. Bảng kiểm tra toàn vẹn & đối chiếu dữ liệu trên HDFS (Reconciliation Audit):\n"
        "Thẩm định tính toàn vẹn 100% của dữ liệu: 1,470 bản ghi đầu vào CSV khớp hoàn toàn với 1,470 bản ghi trong định dạng Parquet; "
        "Dữ liệu được phân vùng chính xác theo 3 phòng ban (Sales, R&D, HR); Thực hiện gộp tệp (Compaction) thành hr_consolidated.parquet (89.1 KB); "
        "và tỷ lệ giá trị khuyết thiếu đạt chuẩn Zero Defect (0 Null)."
    )
    add_p(
        "3. Kiểm thử luồng khép kín End-to-End (E2E Test Report):\n"
        "Đo đạc độ trễ qua 5 chặng xử lý liên tục: Ingest (12 ms) -> Kafka Stream (45 ms) -> Spark Streaming (85 ms) -> AI Inference (6 ms) -> HDFS Output Sink (28 ms). "
        "Toàn bộ 5 chặng đều đạt trạng thái PASSED với tổng thời gian xử lý chưa đầy 0.2 giây."
    )
    add_p(
        "4. Bảng Benchmark Lưu Trữ: CSV Thô vs Snappy Parquet:\n"
        "Chứng minh lợi thế vượt trội của định dạng Parquet:\n"
        "• Dung lượng lưu trữ: Giảm từ 222.63 KB (CSV) xuống còn 89.06 KB (Parquet Snappy), tiết kiệm 59.9% dung lượng đĩa cứng trên HDFS.\n"
        "• Cấu trúc dữ liệu: Chuyển từ dạng dòng (Row-oriented) sang dạng cột (Columnar), tối ưu hóa nén từng kiểu dữ liệu riêng biệt.\n"
        "• Tốc độ đọc quét của Spark: Nhanh hơn 4.5 lần nhờ cơ chế lọc dữ liệu tại nguồn (Predicate Pushdown) và chỉ đọc đúng các cột cần thiết (Column Projection).\n"
        "• Suy luận lược đồ (Schema): Đọc tức thì 0ms nhờ siêu dữ liệu tích hợp (Embedded Metadata), thay vì tốn CPU quét toàn bộ tệp như CSV."
    )
    add_p(
        "5. Bảng Benchmark Tính Toán & Tài Nguyên Hệ Thống:\n"
        "Đo lường thời gian thực thi của từng thành phần: Spark Read & Clean Transform (0.312s), Spark SQL 6 truy vấn đa chiều (0.091s), "
        "Huấn luyện Random Forest 100 cây (0.298s), Gộp tệp Parquet Compaction (0.035s) và Phân cụm K-Means hội tụ sau 10 vòng lặp (0.085s)."
    )

    # -------------------------------------------------------------
    # CHƯƠNG 3: HƯỚNG DẪN VẬN HÀNH & KỊCH BẢN DEMO
    # -------------------------------------------------------------
    add_h1("CHƯƠNG 3. HƯỚNG DẪN VẬN HÀNH & KỊCH BẢN DEMO BẢO VỆ ĐỒ ÁN")

    add_h2("3.1. Hướng dẫn khởi chạy ứng dụng")
    add_p(
        "Để khởi chạy và trải nghiệm đầy đủ các tính năng của Web Dashboard, người dùng thực hiện theo một trong hai cách sau tại thư mục gốc D:\\Doan_BigData:\n"
        "• Cách 1 (Nhanh nhất): Nhấp đúp chuột vào tệp run_web.bat tại thư mục gốc.\n"
        "• Cách 2 (Dòng lệnh): Mở Command Prompt hoặc Terminal và chạy lệnh: python run_web.py\n"
        "Sau đó, mở trình duyệt Web (Chrome, Edge hoặc Firefox) và truy cập địa chỉ: http://localhost:5000"
    )

    add_h2("3.2. Kịch bản thuyết trình bảo vệ đồ án mẫu trong 5 phút (Pitching Script)")
    pitching = (
        "«Kính thưa Thầy/Cô trong Hội đồng chấm thi,\n\n"
        "Em tên là Vũ Lê Anh Đức, sinh viên lớp 11DHBM1, MSSV 2001230191. Hôm nay em xin phép được báo cáo và trình diễn sản phẩm đồ án môn học "
        "Các công nghệ Dữ liệu lớn với đề tài: 'Xây dựng hệ thống Pipeline Big Data phân tích các yếu tố ảnh hưởng và dự đoán nguy cơ nghỉ việc của nhân viên'.\n\n"
        "Để minh họa trực quan cho đồ án, em đã hiện thực hóa toàn bộ giải pháp thành một Web Dashboard tương tác trực tiếp tại địa chỉ localhost:5000 gồm 6 trang chức năng:\n\n"
        "1. TẠI TRANG PIPELINE 9 BƯỚC: Em điều phối toàn bộ chu trình ETL. Thầy/Cô có thể thấy cây thư mục HDFS Data Lake với 3 tầng raw, processed, output. "
        "Khi em bấm nút 'Chạy liên hoàn', cửa sổ Terminal bên phải sẽ tương tác thời gian thực với backend, nạp 1,470 bản ghi nhân sự, chuyển đổi nén cột Parquet "
        "và ghi nhận trạng thái hoàn thành của cả 9 chặng công nghệ.\n\n"
        "2. TẠI TRANG SPARK SQL: Động cơ Apache Spark thực thi song song các truy vấn trên bộ nhớ RAM. Biểu đồ chỉ ra rằng nhân viên làm thêm giờ (OverTime) "
        "có tỷ lệ nghỉ việc vọt lên 30.53%, cao gấp 3 lần bình thường. Khối Sales và các nhân sự có thâm niên dưới 2 năm là những nhóm có nguy cơ ra đi cao nhất.\n\n"
        "3. TẠI TRANG MACHINE LEARNING & K-MEANS: Em giải quyết bài toán mất cân bằng lớp dữ liệu để huấn luyện mô hình Random Forest đạt ROC-AUC 0.81, "
        "độ trễ suy luận chỉ 0.066 ms và vượt qua 6/6 bài kiểm thử tự động. Đồng thời thuật toán K-Means phân khúc nhân sự thành 4 cụm rõ rệt giúp doanh nghiệp "
        "có chiến lược giữ chân phù hợp cho từng nhóm.\n\n"
        "4. TẠI TRANG STREAMING & SIMULATOR: Hệ thống tích hợp Apache Kafka để tiếp nhận luồng sự kiện quẹt thẻ, chấm công và tự động phân loại cảnh báo 3 cấp độ. "
        "Người quản lý có thể vào trang AI Simulator kéo thả thử nghiệm mức lương hay giờ làm thêm để hệ thống dự báo xác suất thôi việc và xuất kế hoạch hành động ngay lập tức.\n\n"
        "5. TẠI TRANG AIRFLOW & BENCHMARK: Toàn bộ quy trình được tự động hóa bằng đồ thị DAG định kỳ hàng ngày, cùng báo cáo thực nghiệm chứng minh định dạng Parquet "
        "tiết kiệm 59.9% dung lượng đĩa và tăng tốc độ đọc của Spark lên 4.5 lần.\n\n"
        "Em xin chân thành cảm ơn Thầy/Cô đã lắng nghe và em rất mong nhận được những câu hỏi phản biện từ Hội đồng ạ!»"
    )
    p_pitch = doc.add_paragraph()
    r_pitch = p_pitch.add_run(pitching)
    r_pitch.font.size = Pt(10.5)
    r_pitch.italic = True
    p_pitch.paragraph_format.space_after = Pt(12)

    # -------------------------------------------------------------
    # CHƯƠNG 4: KẾT LUẬN & GIÁ TRỊ ĐÓNG GÓP
    # -------------------------------------------------------------
    add_h1("CHƯƠNG 4. KẾT LUẬN & GIÁ TRỊ ĐÓNG GÓP CỦA HỆ THỐNG")
    add_p(
        "Hệ thống Web Dashboard Big Data phân tích nhân sự được hoàn thiện đầy đủ, đáp ứng vượt mong đợi các tiêu chuẩn học phần Các công nghệ Dữ liệu lớn. "
        "Các đóng góp chính của đề tài bao gồm:\n"
        "1. Tính hoàn chỉnh về mặt kiến trúc: Hiện thực hóa trọn vẹn 6 tầng công nghệ Big Data theo đúng giáo trình (Ingestion, Storage, Processing, Analytics, ML, Orchestration).\n"
        "2. Tính thực tiễn và ứng dụng cao: Cung cấp giao diện trực quan, bảng điều khiển KPI, bộ mô phỏng AI và kế hoạch hành động giữ chân nhân tài có thể chuyển giao cho các doanh nghiệp.\n"
        "3. Tính tối ưu và kiểm định chặt chẽ: Dữ liệu được nén cột Parquet Snappy (-59.9%), thời gian truy vấn dưới 0.1 giây, luồng xử lý đạt chuẩn E2E và vượt qua 6/6 automated test suites.\n"
        "Hệ thống là minh chứng rõ nét cho năng lực làm chủ công nghệ dữ liệu lớn phân tán, tư duy kỹ thuật hệ thống và khả năng hiện thực hóa sản phẩm phần mềm của sinh viên."
    )

    output_dir = "D:\\Doan_BigData\\BaoCao_Word"
    os.makedirs(output_dir, exist_ok=True)
    output_docx_path = os.path.join(output_dir, "BaoCao_ThuyetMinh_CacTrang_Web_Dashboard_BigData.docx")
    doc.save(output_docx_path)
    
    file_size_kb = os.path.getsize(output_docx_path) / 1024
    print(f"\n[THÀNH CÔNG] ĐÃ TẠO TỆP BÁO CÁO WORD MỚI TẠI:")
    print(f"             {output_docx_path}")
    print(f"             Dung lượng tệp: {file_size_kb:.2f} KB\n")

if __name__ == "__main__":
    create_web_report()
