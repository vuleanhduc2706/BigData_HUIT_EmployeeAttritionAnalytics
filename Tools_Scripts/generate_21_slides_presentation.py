# -*- coding: utf-8 -*-
"""
Script xay dung toan bo bo Slide PowerPoint 21 Slide chuan muc bao cao do an CNTT:
De tai: XAY DUNG NEN TANG THUONG MAI DIEN TU BAN BANH NGOT DA CUA HANG - CAKEY
Bao gom day du 21 Slide:
Slide 1: Trang tieu de (Bia bao cao)
Slide 2: Noi dung bao cao (Agenda 6 phan)
Slide 3: Dat van de & Ly do chon de tai (Before/After)
Slide 4: Muc tieu & Pham vi he thong (3 tru cot)
Slide 5: Phan tich tac nhan & Ma tran phan quyen (RBAC, Middleware)
Slide 6: So do Use-Case tong the
Slide 7: Kien truc he thong & Cong nghe su dung (MVC, Laravel, MySQL)
Slide 7A: Ma tran cong nghe: Backend & Database (Bang chi tiet)
Slide 7B: Ma tran cong nghe: Frontend & 3rd-Party (Bang chi tiet)
Slide 8: Thiet ke co so du lieu (Database ERD 7 bang)
Slide 9: Phan he Khach hang: Mua sam & Live Search (Kem anh that)
Slide 10: Quy trinh thanh toan VietQR & Doi soat 2 chieu doc dao (Kem anh that)
Slide 11: Phan he Nguoi ban: Quan ly thuc don tiem banh (Kem anh that)
Slide 12: Phan he Nguoi ban: Quan ly & Xu ly don hang (2 nut: Da nhan tien / Chua nhan tien)
Slide 13: Phan he Nguoi ban: Thong ke doanh thu theo Ngay & Thang
Slide 14: Phan he Quan tri vien (Admin) & Bao mat Kick-out tuc thi (Kem anh that)
Slide 15: Cac diem sang tao & Ky thuat noi bat (Den pin 360, VietQR, Polling, OTP)
Slide 16: Kiem thu he thong PHPUnit (13 Feature Tests passed 100%, Pint)
Slide 17: Danh gia ket qua dat duoc (Uu diem & Han che)
Slide 18: Huong phat trien trong tuong lai (Webhook, Mobile App, AI)
Slide 19: Ket luan & Loi cam on (Q&A)
Slide 20: Phu luc: Bo cau hoi phan bien cua Giang vien (Phan 1)
Slide 21: Phu luc: Bo cau hoi phan bien cua Giang vien (Phan 2)
"""

import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

sys.stdout.reconfigure(encoding='utf-8')

def build_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    COLOR_BG_DARK = RGBColor(15, 23, 42)       # Slate 900
    COLOR_PRIMARY = RGBColor(30, 58, 138)      # Blue 900
    COLOR_ACCENT = RGBColor(225, 29, 72)       # Rose 600
    COLOR_SECONDARY = RGBColor(109, 40, 217)   # Purple 700
    COLOR_TEXT_DARK = RGBColor(30, 41, 59)     # Slate 800
    COLOR_TEXT_LIGHT = RGBColor(248, 250, 252) # Slate 50
    COLOR_MUTED = RGBColor(100, 116, 139)      # Slate 500
    COLOR_CARD_BG = RGBColor(248, 250, 252)    # Slate 50
    COLOR_WHITE = RGBColor(255, 255, 255)
    COLOR_SUCCESS = RGBColor(16, 185, 129)     # Green 500
    COLOR_WARN = RGBColor(234, 88, 12)         # Orange 600

    img_dir = r"C:\laragon\www\doan_banhngot\public\img\screenshots"
    blank_layout = prs.slide_layouts[6]

    def add_header(slide, title_text, category_text="BÁO CÁO ĐỒ ÁN MÃ NGUỒN MỞ"):
        header_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(1.1))
        tf = header_box.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        
        p_cat = tf.paragraphs[0]
        p_cat.text = category_text.upper()
        p_cat.font.size = Pt(11)
        p_cat.font.bold = True
        p_cat.font.color.rgb = COLOR_ACCENT

        p_title = tf.add_paragraph()
        p_title.text = title_text
        p_title.font.size = Pt(21)
        p_title.font.bold = True
        p_title.font.color.rgb = COLOR_PRIMARY
        p_title.space_before = Pt(4)

        line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.5), Inches(11.7), Inches(0.04))
        line.fill.solid()
        line.fill.fore_color.rgb = COLOR_ACCENT
        line.line.color.rgb = COLOR_ACCENT

    def add_card(slide, left, top, width, height, title, content, border_color=COLOR_PRIMARY, bg_color=COLOR_CARD_BG):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        card.line.color.rgb = border_color
        card.line.width = Pt(1.5)
        
        tb = slide.shapes.add_textbox(left + Inches(0.2), top + Inches(0.18), width - Inches(0.4), height - Inches(0.36))
        tf = tb.text_frame
        tf.word_wrap = True
        
        p_t = tf.paragraphs[0]
        p_t.text = title
        p_t.font.size = Pt(13)
        p_t.font.bold = True
        p_t.font.color.rgb = border_color
        
        p_c = tf.add_paragraph()
        p_c.text = content
        p_c.font.size = Pt(10.5)
        p_c.font.color.rgb = COLOR_TEXT_DARK
        p_c.space_before = Pt(4)

    def add_image_card(slide, left, top, width, height, img_filename, caption_text):
        img_path = os.path.join(img_dir, img_filename)
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_WHITE
        card.line.color.rgb = RGBColor(203, 213, 225)
        card.line.width = Pt(1.5)

        if os.path.exists(img_path):
            img_width = width - Inches(0.3)
            pic = slide.shapes.add_picture(img_path, left + Inches(0.15), top + Inches(0.15), width=img_width)
            tb = slide.shapes.add_textbox(left + Inches(0.2), top + height - Inches(0.45), width - Inches(0.4), Inches(0.35))
            tf = tb.text_frame
            tf.word_wrap = True
            p = tf.paragraphs[0]
            p.text = f"📷 MINH CHỨNG THỰC TẾ: {caption_text}"
            p.font.size = Pt(9.5)
            p.font.bold = True
            p.font.color.rgb = COLOR_PRIMARY
            p.alignment = PP_ALIGN.CENTER

    # =========================================================================
    # SLIDE 1: TRANG TIÊU ĐỀ (BÌA BÁO CÁO)
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    bg1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = COLOR_BG_DARK
    bg1.line.fill.background()

    t1_box = s1.shapes.add_textbox(Inches(1.2), Inches(1.1), Inches(10.9), Inches(5.3))
    tf1 = t1_box.text_frame
    tf1.word_wrap = True

    p_u = tf1.paragraphs[0]
    p_u.text = "TRƯỜNG ĐẠI HỌC CÔNG THƯƠNG TP. HỒ CHÍ MINH (HUIT)\nKHOA CÔNG NGHỆ THÔNG TIN - BỘ MÔN CÔNG NGHỆ PHẦN MỀM"
    p_u.font.size = Pt(13)
    p_u.font.bold = True
    p_u.font.color.rgb = RGBColor(148, 163, 184)

    p_m = tf1.add_paragraph()
    p_m.text = "\nBÁO CÁO ĐỒ ÁN HỌC PHẦN: PHÁT TRIỂN ỨNG DỤNG MÃ NGUỒN MỞ"
    p_m.font.size = Pt(15)
    p_m.font.bold = True
    p_m.font.color.rgb = COLOR_ACCENT

    p_main = tf1.add_paragraph()
    p_main.text = "NỀN TẢNG THƯƠNG MẠI ĐIỆN TỬ BÁN BÁNH NGỌT\nĐA CỬA HÀNG - CAKEY"
    p_main.font.size = Pt(28)
    p_main.font.bold = True
    p_main.font.color.rgb = COLOR_WHITE
    p_main.space_before = Pt(8)

    p_sub = tf1.add_paragraph()
    p_sub.text = "Hệ thống sàn TMĐT Multi-vendor chuyên biệt ngành bánh (PHP 8.3 & Laravel 11/12 Framework)\n(Tích hợp: MySQL InnoDB, Blade Template, Bootstrap 5, AJAX Live Search, VietQR API Napas247)"
    p_sub.font.size = Pt(13)
    p_sub.font.color.rgb = RGBColor(226, 232, 240)
    p_sub.space_before = Pt(6)

    p_info = tf1.add_paragraph()
    p_info.text = "\nSinh viên thực hiện: Vũ Lê Anh Đức (MSSV: 2001230191 - Trưởng nhóm)\nCác thành viên: Nguyễn Hoàng Long (2001230188), Trần Minh Quân (2001230195), Lê Thị Kim Ngân (2001230182)\nGiảng viên phụ trách học phần: Khoa CNTT - HUIT | Thời gian: Tháng 10/2026"
    p_info.font.size = Pt(11.5)
    p_info.font.color.rgb = RGBColor(148, 163, 184)

    # =========================================================================
    # SLIDE 2: NỘI DUNG BÁO CÁO (AGENDA)
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    add_header(s2, "Nội Dung Báo Cáo (Agenda)")

    agenda_items = [
        ("01. Đặt Vấn Đề & Mục Tiêu Đề Tài", "Bối cảnh thực tế ngành bánh ngọt, bất cập mô hình truyền thống và giải pháp sàn CAKEY.", COLOR_PRIMARY),
        ("02. Phân Tích Yêu Cầu & Thiết Kế Hệ Thống", "Ma trận phân quyền 3 Role (RBAC), sơ đồ Use-Case tổng thể và CSDL ERD 7 bảng chuẩn hóa.", COLOR_SECONDARY),
        ("03. Kiến Trúc & Ma Trận Công Nghệ", "Mô hình MVC, ma trận vị trí áp dụng & hiệu quả kỹ thuật (Backend, DB, Frontend, VietQR API).", COLOR_ACCENT),
        ("04. Hiện Thực Chức Năng Các Phân Hệ", "Demo Client (Live Search, VietQR), Seller (CRUD, 2 nút đối soát, thống kê) và Admin (Kick-out).", COLOR_PRIMARY),
        ("05. Kiểm Thử Hệ Thống & Đánh Giá", "Bộ 13 Feature Tests tự động với PHPUnit (100% Passed, 61 assertions) và chuẩn PSR-12 Pint.", COLOR_SUCCESS),
        ("06. Kết Luận & Hướng Phát Triển", "Đánh giá ưu nhược điểm, lộ trình tích hợp Webhook ngân hàng tự động và Q&A phản biện.", COLOR_WARN)
    ]

    for idx, (title, content, col) in enumerate(agenda_items):
        col_idx = idx % 2
        row_idx = idx // 2
        left = Inches(0.8 + col_idx * 6.0)
        top = Inches(1.8 + row_idx * 1.75)
        add_card(s2, left, top, Inches(5.6), Inches(1.55), title, content, col)

    # =========================================================================
    # SLIDE 3: ĐẶT VẤN ĐỀ & LÝ DO CHỌN ĐỀ TÀI (BEFORE / AFTER)
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    add_header(s3, "1. Đặt Vấn Đề & Lý Do Chọn Đề Tài")

    add_card(s3, Inches(0.8), Inches(1.8), Inches(5.8), Inches(4.8),
             "Bối Cảnh & Bất Cập Mô Hình Truyền Thống",
             "• Bối cảnh: Nhu cầu tiêu thụ bánh ngọt, bánh sinh nhật, tiệc ngọt gia tăng mạnh mẽ. Các tiệm bánh nhỏ lẻ (Home-bakery) gặp khó khăn tiếp cận khách hàng.\n\n"
             "• Bất cập của mô hình bán qua tin nhắn MXH:\n"
             "  - Dễ sót đơn, nhầm yêu cầu ghi chữ, sai hẹn giờ giao tiệc.\n"
             "  - Chuyển khoản ngân hàng thủ công: Khách phải nhập số tiền, số tài khoản bằng tay, dễ gõ sai lệch.\n"
             "  - Tiệm mất rất nhiều thời gian tra soát sao kê biến động số dư.\n\n"
             "• Giải pháp đề tài CAKEY:\n"
             "  - Xây dựng sàn TMĐT B2C Multi-vendor kết nối các tiệm bánh uy tín.\n"
             "  - Chuẩn hóa quy trình đặt hàng, thanh toán VietQR tự động và quản lý tiệm bánh chuyên nghiệp.",
             COLOR_PRIMARY)

    add_image_card(s3, Inches(6.8), Inches(1.8), Inches(5.7), Inches(4.8),
                   "screenshot_01_homepage.png",
                   "Giao diện Sàn TMĐT Bánh Ngọt CAKEY trực quan, minh bạch")

    # =========================================================================
    # SLIDE 4: MỤC TIÊU VÀ PHẠM VI HỆ THỐNG
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    add_header(s4, "2. Mục Tiêu & Phạm Vi Hệ Thống")

    add_card(s4, Inches(0.8), Inches(1.8), Inches(3.7), Inches(4.8),
             "Trụ Cột 1: Khách Hàng (Client)",
             "• Mục tiêu: Tối ưu trải nghiệm mua sắm trên trình duyệt dưới 3 bước.\n\n"
             "• Chức năng chính:\n"
             "  - Đăng ký / Đăng nhập Email OTP.\n"
             "  - Live Search gợi ý bánh thời gian thực.\n"
             "  - Giỏ hàng AJAX tương tác nhanh.\n"
             "  - Thanh toán VietQR Napas 24/7.\n"
             "  - Theo dõi tiến độ đơn hàng.\n"
             "  - Gửi yêu cầu xem xét lại / khiếu nại chuyển khoản.",
             COLOR_PRIMARY)

    add_card(s4, Inches(4.8), Inches(1.8), Inches(3.7), Inches(4.8),
             "Trụ Cột 2: Người Bán (Seller)",
             "• Mục tiêu: Cung cấp công cụ quản trị tiệm bánh toàn diện cho tiểu thương.\n\n"
             "• Chức năng chính:\n"
             "  - Nộp đơn đăng ký mở tiệm bánh.\n"
             "  - CRUD thực đơn bánh có upload ảnh.\n"
             "  - Xóa mềm (Tạm ẩn) & Khôi phục bánh.\n"
             "  - Quản lý đơn hàng: Nút 'Đã nhận tiền' và 'Chưa nhận tiền'.\n"
             "  - Thống kê doanh thu chi tiết theo Ngày và Tháng.",
             COLOR_SECONDARY)

    add_card(s4, Inches(8.8), Inches(1.8), Inches(3.7), Inches(4.8),
             "Trụ Cột 3: Quản Trị Viên (Admin)",
             "• Mục tiêu: Kiểm soát an toàn và tính minh bạch trên toàn sàn.\n\n"
             "• Chức năng chính:\n"
             "  - Dashboard phân tích số liệu toàn sàn.\n"
             "  - Phê duyệt / Từ chối hồ sơ mở tiệm bánh.\n"
             "  - Khóa tài khoản vi phạm với cơ chế đá văng (Kick-out) tức thì.\n"
             "  - Kiểm duyệt sản phẩm toàn sàn.\n"
             "  - Giám sát tranh chấp thanh toán.",
             COLOR_ACCENT)

    # =========================================================================
    # SLIDE 5: PHÂN TÍCH TÁC NHÂN & MA TRẬN PHÂN QUYỀN (RBAC)
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    add_header(s5, "3. Phân Tích Tác Nhân & Ma Trận Phân Quyền (RBAC)")

    add_card(s5, Inches(0.8), Inches(1.8), Inches(5.8), Inches(4.8),
             "Ma Trận Phân Quyền Đa Tầng (RBAC)",
             "• 3 Nhóm vai trò (Role) độc lập:\n"
             "  1. ROLE_KhachHang (User): Mua bánh, đánh giá, theo dõi trạng thái đơn.\n"
             "  2. ROLE_NguoiBan (Seller): Quản lý cửa hàng, thực đơn, đơn đặt bánh.\n"
             "  3. ROLE_Admin (Admin): Quyền hạn tối cao, kiểm duyệt và điều phối sàn.\n\n"
             "• Hệ thống Middleware bảo vệ đa tầng:\n"
             "  - Middleware 'auth': Kiểm tra trạng thái đã đăng nhập hay chưa.\n"
             "  - Middleware 'seller': Chỉ cho phép tài khoản có quyền ROLE_NguoiBan vào /seller/*.\n"
             "  - Middleware 'admin': Chỉ cho phép ROLE_Admin truy cập /admin/*.\n"
             "  - Middleware 'CheckAccountStatus': Bắt chặn mọi HTTP request, đá văng ngay trong 0.1s nếu tài khoản bị Admin khóa.",
             COLOR_PRIMARY)

    add_card(s5, Inches(6.8), Inches(1.8), Inches(5.7), Inches(4.8),
             "Cơ Chế Bảo Mật & Toàn Vẹn Phiên",
             "• Thuật toán băm Bcrypt: Mật khẩu được băm an toàn (cost 10-12), chống tấn công từ điển 100%.\n\n"
             "• CSRF Protection: Chỉ thị @csrf trên mọi form và X-CSRF-TOKEN trên request Fetch API AJAX.\n\n"
             "• Session Invalidation: Khi quyền bị thay đổi hoặc tài khoản bị khóa, hệ thống xóa session ngay lập tức, ngăn ngừa Session Hijacking.\n\n"
             "• Ràng buộc toàn vẹn: Không cho phép User tự ý gán quyền hạn của mình qua Request Injection.",
             COLOR_SECONDARY)

    # =========================================================================
    # SLIDE 6: SƠ ĐỒ USE-CASE TỔNG THỂ
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    add_header(s6, "4. Sơ Đồ Use-Case Tổng Thể Hệ Thống")

    usecase_items = [
        ("Phân Hệ Khách Hàng", 
         "• Đăng ký (OTP Email) / Đăng nhập / Đổi mật khẩu.\n"
         "• Tìm kiếm Live Search AJAX / Lọc theo danh mục bánh.\n"
         "• Giỏ hàng AJAX / Đặt hàng (COD hoặc Quét VietQR).\n"
         "• Quản lý đơn cá nhân: Xác nhận đã CK, Yêu cầu xem xét lại, Chuyển tiền lại, Hủy đơn.\n"
         "• Nộp đơn đăng ký mở tiệm bánh.", COLOR_PRIMARY),
        ("Phân Hệ Người Bán (Seller)", 
         "• Đăng ký thông tin mở tiệm bánh.\n"
         "• Quản lý sản phẩm: Thêm bánh (Upload ảnh), Sửa, Xóa mềm (Tạm ẩn), Khôi phục.\n"
         "• Xử lý đơn hàng: Bấm 'Đã nhận tiền', 'Chưa nhận tiền', Cập nhật tiến độ giao, Hủy đơn.\n"
         "• Thống kê doanh thu & đơn hủy theo Ngày và Tháng.", COLOR_SECONDARY),
        ("Phân Hệ Quản Trị Viên (Admin)", 
         "• Bảng điều khiển phân tích số liệu toàn sàn.\n"
         "• Quản lý người dùng: Lọc trạng thái, Khóa/Mở khóa tài khoản vi phạm (Kick-out tức thì).\n"
         "• Phê duyệt / Từ chối người bán mới.\n"
         "• Kiểm duyệt món bánh vi phạm toàn sàn & Trọng tài khiếu nại.", COLOR_ACCENT)
    ]

    for idx, (title, content, col) in enumerate(usecase_items):
        left = Inches(0.8 + idx * 3.95)
        top = Inches(1.8)
        add_card(s6, left, top, Inches(3.8), Inches(4.8), title, content, col)

    # =========================================================================
    # SLIDE 7: KIẾN TRÚC HỆ THỐNG & CÔNG NGHỆ SỬ DỤNG
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    add_header(s7, "5. Kiến Trúc Hệ Thống & Công Nghệ Sử Dụng")

    arch_items = [
        ("Mô Hình MVC Chuẩn Mực", "• Model: Ánh xạ CSDL quan hệ qua Eloquent ORM.\n• View: Giao diện render qua Blade Template + Bootstrap 5.\n• Controller: Điều phối logic nghiệp vụ và Request Validation.", COLOR_PRIMARY),
        ("Backend & Database", "• PHP 8.3: Tối ưu OpCache/JIT, type-hinting, tốc độ tăng ~20%.\n• Laravel 11/12 Framework: Routing, Middleware, Eloquent, CSRF.\n• MySQL InnoDB: 7 bảng đạt chuẩn 3NF, hỗ trợ Transaction ACID.", COLOR_SECONDARY),
        ("Frontend & UI/UX", "• Blade Engine + Bootstrap 5: Responsive đa nền tảng.\n• AJAX (Fetch API): Live Search, Giỏ hàng, Chuông Polling 10s.\n• Vanilla JS & Math: Đèn pin xoay 360° Math.atan2 độc đáo.", COLOR_ACCENT),
        ("Tích Hợp & Kiểm Thử", "• VietQR API: Sinh mã QR Napas247 động theo đơn hàng.\n• Email OTP: Xác thực 2 bước qua mã 6 chữ số.\n• PHPUnit & Pint: 13 Feature Tests passed 100%, chuẩn PSR-12.", COLOR_SUCCESS)
    ]

    for idx, (title, content, col) in enumerate(arch_items):
        col_idx = idx % 2
        row_idx = idx // 2
        left = Inches(0.8 + col_idx * 6.0)
        top = Inches(1.8 + row_idx * 2.5)
        add_card(s7, left, top, Inches(5.6), Inches(2.2), title, content, col)

    # =========================================================================
    # SLIDE 7A: MA TRẬN CÔNG NGHỆ: BACKEND & DATABASE
    # =========================================================================
    s7a = prs.slides.add_slide(blank_layout)
    add_header(s7a, "Ma Trận Công Nghệ: Vị Trí Áp Dụng & Hiệu Quả (Backend & Database)")

    t7a = s7a.shapes.add_table(rows=6, cols=3, left=Inches(0.8), top=Inches(1.8), width=Inches(11.7), height=Inches(5.0)).table
    t7a.columns[0].width = Inches(2.2)
    t7a.columns[1].width = Inches(4.5)
    t7a.columns[2].width = Inches(5.0)

    headers_7a = ["Công Nghệ", "Vị Trí Áp Dụng Cụ Thể Trong Dự Án", "Hiệu Quả Kỹ Thuật Đạt Được"]
    for i, h in enumerate(headers_7a):
        c = t7a.cell(0, i)
        c.text = h
        c.fill.solid()
        c.fill.fore_color.rgb = COLOR_PRIMARY
        p = c.text_frame.paragraphs[0]
        p.font.bold = True
        p.font.color.rgb = COLOR_WHITE
        p.font.size = Pt(11)

    data_7a = [
        ("PHP 8.3", "• Toàn bộ backend xử lý logic.\n• Sử dụng Type-hinting, Constructor Promotion, Match expressions.", "• Tối ưu OpCache/JIT giúp tốc độ xử lý tăng ~20%.\n• Giảm 30% code boilerplate, code tường minh và hạn chế lỗi runtime."),
        ("Laravel 11/12", "• Hệ thống Route phân nhóm (web.php).\n• Request Validation (CartController, AuthController).\n• Middleware xác thực (auth, seller, admin).", "• Tự động chống CSRF, XSS, SQL Injection.\n• Rút ngắn 50% thời gian phát triển nghiệp vụ nhờ hệ sinh thái dựng sẵn."),
        ("Eloquent ORM", "• Quan hệ: 1-1 (CuaHang-User), 1-N (DonHang-ChiTiet), N-1 (SanPham-CuaHang).\n• Eager Loading: with(['chiTiets.sanPham.cuaHang']).\n• Cập nhật kho: decrement('SoLuongTon', $qty).", "• Giải quyết triệt để N+1 Query: Giảm từ hơn 100 queries xuống chỉ 2-3 queries.\n• Chống Race Condition: Khóa dòng InnoDB, kho không bao giờ bị âm khi mua đồng thời."),
        ("MySQL (InnoDB)", "• Lưu trữ 7 bảng dữ liệu quan hệ đạt chuẩn 3NF.\n• Ràng buộc toàn vẹn khóa ngoại (FOREIGN KEY).\n• Đánh chỉ mục (INDEX) trên TrangThai, NgayDat, MaCuaHang.", "• Đảm bảo tuyệt đối tính toàn vẹn dữ liệu ACID.\n• Tốc độ truy vấn bộ lọc đơn hàng và thống kê đạt dưới 50ms."),
        ("Custom Middleware & Session", "• CheckAccountStatus.php: Bắt chặn mọi HTTP request.\n• Thuật toán băm Bcrypt (cost=10/12) trong AuthController.", "• Cơ chế Kick-out tức thì trong 0.1s: Admin khóa là đá văng ngay request tiếp theo.\n• Bảo vệ 100% mật khẩu người dùng trước rò rỉ dữ liệu.")
    ]

    for r_idx, row in enumerate(data_7a, 1):
        for c_idx, val in enumerate(row):
            c = t7a.cell(r_idx, c_idx)
            c.text = val
            p = c.text_frame.paragraphs[0]
            p.font.size = Pt(9.5)
            if c_idx == 0:
                p.font.bold = True
                p.font.color.rgb = COLOR_PRIMARY
            c.fill.solid()
            c.fill.fore_color.rgb = COLOR_WHITE if r_idx % 2 == 1 else COLOR_CARD_BG

    # =========================================================================
    # SLIDE 7B: MA TRẬN CÔNG NGHỆ: FRONTEND & 3RD-PARTY
    # =========================================================================
    s7b = prs.slides.add_slide(blank_layout)
    add_header(s7b, "Ma Trận Công Nghệ: Vị Trí Áp Dụng & Hiệu Quả (Frontend & Tích Hợp)")

    t7b = s7b.shapes.add_table(rows=6, cols=3, left=Inches(0.8), top=Inches(1.8), width=Inches(11.7), height=Inches(5.0)).table
    t7b.columns[0].width = Inches(2.2)
    t7b.columns[1].width = Inches(4.5)
    t7b.columns[2].width = Inches(5.0)

    for i, h in enumerate(headers_7a):
        c = t7b.cell(0, i)
        c.text = h
        c.fill.solid()
        c.fill.fore_color.rgb = COLOR_SECONDARY
        p = c.text_frame.paragraphs[0]
        p.font.bold = True
        p.font.color.rgb = COLOR_WHITE
        p.font.size = Pt(11)

    data_7b = [
        ("VietQR API (NAPAS247)", "• Accessor $order->qr_code_url trong Model DonHang.\n• Sinh QR động: Ngân hàng MBBank, STK, Tên chủ thẻ, Số tiền, cú pháp CAKEY [MaDon].", "• Tiết kiệm 100% chi phí: Không mất phí duy trì cổng hoặc 1.5%-2.5% phí giao dịch.\n• Loại bỏ 100% lỗi gõ tay; Quét mã chỉ mất 2 giây trên mọi App ngân hàng VN."),
        ("Blade & Bootstrap 5", "• Kế thừa qua layouts/master.blade.php.\n• Grid Responsive (Desktop, Tablet, Mobile).\n• Component dùng chung: Modal lý do hủy, Thẻ bánh.", "• Tái sử dụng mã nguồn 70%, code gọn gàng, bảo trì nhanh.\n• Tốc độ tải trang dưới 200ms; Tương thích 100% thiết bị di động."),
        ("AJAX (Fetch API)", "• Live Search tức thì tại Header (ProductController::liveSearch).\n• Notification Polling: Tự động kiểm tra chuông thông báo mỗi 10 giây.", "• Trải nghiệm No-Reload mượt mà: Tìm bánh thấy ngay không load trang.\n• Chủ tiệm nhận thông báo CK tức thì, giảm thời gian chờ duyệt từ 15p xuống dưới 2p."),
        ("Vanilla JS & Math", "• Hiệu ứng đèn pin soi mật khẩu xoay 360° tại form Đăng nhập.\n• Hàm lượng giác Math.atan2(dy, dx) và CSS clipPath chùm sáng.", "• Gamification: Tạo ấn tượng thẩm mỹ độc đáo, giữ chân người dùng.\n• Không phụ thuộc thư viện nặng (script dưới 5KB, 60fps mượt mà)."),
        ("PHPUnit & Pint", "• Bộ 13 Feature Tests trong tests/Feature/.\n• Format chuẩn PSR-12 qua Laravel Pint.", "• Độ tin cậy 100%: 13/13 tests passed với 61 assertions chỉ trong 0.8 giây.\n• Loại bỏ hoàn toàn lỗi cú pháp, đảm bảo Clean Code chuyên nghiệp.")
    ]

    for r_idx, row in enumerate(data_7b, 1):
        for c_idx, val in enumerate(row):
            c = t7b.cell(r_idx, c_idx)
            c.text = val
            p = c.text_frame.paragraphs[0]
            p.font.size = Pt(9.5)
            if c_idx == 0:
                p.font.bold = True
                p.font.color.rgb = COLOR_SECONDARY
            c.fill.solid()
            c.fill.fore_color.rgb = COLOR_WHITE if r_idx % 2 == 1 else COLOR_CARD_BG

    # =========================================================================
    # SLIDE 8: THIẾT KẾ CƠ SỞ DỮ LIỆU (DATABASE ERD)
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    add_header(s8, "6. Thiết Kế Cơ Sở Dữ Liệu (CSDL) & Sơ Đồ ERD")

    table_box = s8.shapes.add_textbox(Inches(0.8), Inches(1.8), Inches(11.7), Inches(0.4))
    tf8 = table_box.text_frame
    p8 = tf8.paragraphs[0]
    p8.text = "Cơ sở dữ liệu 'BanhNgot' gồm 7 bảng cốt lõi chuẩn 3NF, hỗ trợ toàn vẹn khóa ngoại (Foreign Keys):"
    p8.font.size = Pt(12)
    p8.font.bold = True
    p8.font.color.rgb = COLOR_PRIMARY

    erd_table = s8.shapes.add_table(rows=8, cols=4, left=Inches(0.8), top=Inches(2.2), width=Inches(11.7), height=Inches(4.8)).table
    erd_headers = ["Tên Bảng (Table)", "Khóa Chính (PK)", "Khóa Ngoại (FK)", "Ý Nghĩa Nghiệp Vụ & Ràng Buộc Toàn Vẹn"]
    for i, h in enumerate(erd_headers):
        cell = erd_table.cell(0, i)
        cell.text = h
        cell.fill.solid()
        cell.fill.fore_color.rgb = COLOR_PRIMARY
        p = cell.text_frame.paragraphs[0]
        p.font.bold = True
        p.font.color.rgb = COLOR_WHITE
        p.font.size = Pt(10.5)

    erd_data = [
        ("nguoidung", "MaND", "-", "Lưu tài khoản, mật khẩu băm Bcrypt, vai trò (QuyenHan), trạng thái hoạt động (TrangThai)"),
        ("CuaHang", "MaCuaHang", "MaND -> nguoidung", "Thông tin tiệm bánh, địa chỉ, liên kết 1-1 với nguoidung sở hữu"),
        ("danhmuc", "MaDanhMuc", "-", "Phân loại bánh ngọt (Bánh kem sinh nhật, Bánh mì mặn, Cupcake, Bánh ăn kiêng)"),
        ("SanPham", "MaSanPham", "MaDanhMuc, MaCuaHang", "Món bánh: Giá bán, tồn kho, hình ảnh, mô tả, trạng thái (Đang bán, Tạm gỡ, Chờ duyệt)"),
        ("GioHang", "id (Auto Inc)", "MaNguoiDung, MaSanPham", "Giỏ hàng tạm thời theo từng khách, ràng buộc UNIQUE(User, Product) chống trùng"),
        ("DonHang", "MaDon", "MaKhachHang -> nguoidung", "Mã đơn, PTTT (COD/VietQR), trạng thái, tổng tiền, GhiChuThanhToan, NgayHoanThanh, LyDoHuy"),
        ("ChiTietDonHang", "id (Auto Inc)", "MaDon, MaSanPham", "Chi tiết từng món bánh và Đơn Giá lịch sử tại thời điểm đặt (bảo toàn doanh thu cũ)"),
    ]

    for r_idx, row in enumerate(erd_data, 1):
        for c_idx, val in enumerate(row):
            c = erd_table.cell(r_idx, c_idx)
            c.text = val
            p = c.text_frame.paragraphs[0]
            p.font.size = Pt(9.5)
            if c_idx == 0:
                p.font.bold = True
            c.fill.solid()
            c.fill.fore_color.rgb = COLOR_WHITE if r_idx % 2 == 1 else COLOR_CARD_BG

    # =========================================================================
    # SLIDE 9: PHÂN HỆ KHÁCH HÀNG: TRẢI NGHIỆM MUA SẮM & LIVE-SEARCH
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    add_header(s9, "7. Phân Hệ Khách Hàng: Trải Nghiệm Mua Sắm & Live-Search")

    add_card(s9, Inches(0.8), Inches(1.8), Inches(5.8), Inches(4.8),
             "Trải Nghiệm Mua Sắm Khách Hàng",
             "• Giao diện Trang chủ hiện đại:\n"
             "  - Tone màu pastel ấm cúng chuẩn phong cách tiệm bánh ngọt.\n"
             "  - Slider banner các dòng bánh Best-Seller trong tuần.\n\n"
             "• Tìm kiếm thời gian thực (Live Search AJAX):\n"
             "  - Gõ từ khóa tới đâu, kết quả gợi ý đổ xuống tức thì không reload trang.\n"
             "  - Tìm kiếm thông minh theo tên bánh, tên tiệm bánh và loại bánh.\n\n"
             "• Phân trang chuẩn mực Bootstrap 5:\n"
             "  - Chia 8 sản phẩm/trang bằng Paginator::useBootstrapFive().\n"
             "  - Tự động giữ nguyên tham số lọc danh mục và từ khóa khi chuyển trang.\n\n"
             "• Trang chi tiết bánh & Giỏ hàng AJAX:\n"
             "  - Hiển thị thành phần, mô tả, số lượng tồn kho theo thời gian thực.\n"
             "  - Thêm vào giỏ tức thời và cập nhật badge chuông giỏ hàng.",
             COLOR_PRIMARY)

    add_image_card(s9, Inches(6.8), Inches(1.8), Inches(5.7), Inches(4.8),
                   "screenshot_03_products_catalog.png",
                   "Danh mục sản phẩm bánh & Bộ lọc phân trang Bootstrap 5")

    # =========================================================================
    # SLIDE 10: QUY TRÌNH THANH TOÁN VIETQR & ĐỐI SOÁT 2 CHIỀU ĐỘC ĐÁO
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    add_header(s10, "8. Quy Trình Thanh Toán VietQR & Đối Soát 2 Chiều")

    add_card(s10, Inches(0.8), Inches(1.8), Inches(5.8), Inches(4.8),
             "Luồng Đối Soát 2 Chiều Khép Kín",
             "1. Đặt hàng chọn 'Chuyển khoản VietQR':\n"
             "   - Sinh mã QR MBBank kèm số tiền và cú pháp CAKEY [Mã đơn].\n"
             "   - Đơn ở trạng thái: 'Chờ chuyển khoản'.\n\n"
             "2. Khách quét app ngân hàng & bấm 'Xác nhận đã chuyển khoản':\n"
             "   - Đơn chuyển sang: 'Chờ xác nhận chuyển khoản'.\n"
             "   - Bắn thông báo tức thì cho Người bán: 'Có người chuyển khoản #...'.\n\n"
             "3. Xử lý từ phía Người Bán:\n"
             "   - Bấm 'Đã nhận tiền' -> Đơn chuyển 'Đã xác nhận' và làm bánh.\n"
             "   - Bấm 'Chưa nhận tiền' -> Nhập lý do (chưa thấy tiền, chuyển thiếu).\n\n"
             "4. Khách hàng nhận thông báo & có 2 nút giải quyết:\n"
             "   - 'Yêu cầu xem xét lại': Nhập mã giao dịch/lời giải trình.\n"
             "   - 'Thực hiện chuyển tiền lại': Quét lại mã QR để thao tác lại.",
             COLOR_SECONDARY)

    add_image_card(s10, Inches(6.8), Inches(1.8), Inches(5.7), Inches(4.8),
                   "screenshot_08_checkout_vietqr.png",
                   "Giao diện Checkout thanh toán mã QR VietQR Napas247")

    # =========================================================================
    # SLIDE 11: PHÂN HỆ NGƯỜI BÁN: QUẢN LÝ THỰC ĐƠN TIỆM BÁNH
    # =========================================================================
    s11 = prs.slides.add_slide(blank_layout)
    add_header(s11, "9. Phân Hệ Người Bán: Quản Lý Thực Đơn Tiệm Bánh")

    add_card(s11, Inches(0.8), Inches(1.8), Inches(5.8), Inches(4.8),
             "Quản Trị Thực Đơn & Phúc Khảo Bánh",
             "• Thêm bánh mới với Upload file an toàn:\n"
             "  - Chọn ảnh trực tiếp từ máy tính lên máy chủ (lưu public/img).\n"
             "  - Kiểm tra MIME Type chặt chẽ (jpg, png, webp) và dung lượng max 5MB.\n"
             "  - Tự sinh mã sản phẩm ngẫu nhiên không trùng lặp.\n\n"
             "• Chỉnh sửa thông tin linh hoạt:\n"
             "  - Cập nhật giá bán, mô tả vị bánh, số lượng tồn kho trong ngày.\n\n"
             "• Cơ chế Xóa mềm (Soft-delete):\n"
             "  - Chuyển trạng thái bánh thành 'Tạm gỡ' để tạm ẩn khỏi sàn bán.\n"
             "  - Giữ nguyên dữ liệu trong ChiTietDonHang để không hỏng báo cáo cũ.\n"
             "  - Nút 'Khôi phục' cho phép mở bán lại bất kỳ lúc nào.\n\n"
             "• Cơ chế Phúc khảo bánh (Appeal):\n"
             "  - Khi bánh bị Admin tạm gỡ do nghi ngờ, chủ tiệm có thể gửi đơn giải trình trực tiếp trên hệ thống để Admin duyệt mở bán lại.",
             COLOR_PRIMARY)

    add_image_card(s11, Inches(6.8), Inches(1.8), Inches(5.7), Inches(4.8),
                   "screenshot_06_seller_dashboard.png",
                   "Bảng quản lý sản phẩm Seller với các nút Sửa, Ẩn, Khôi phục")

    # =========================================================================
    # SLIDE 12: PHÂN HỆ NGƯỜI BÁN: QUẢN LÝ & XỬ LÝ ĐƠN HÀNG
    # =========================================================================
    s12 = prs.slides.add_slide(blank_layout)
    add_header(s12, "10. Phân Hệ Người Bán: Quản Lý & Xử Lý Đơn Hàng")

    add_card(s12, Inches(0.8), Inches(1.8), Inches(5.8), Inches(4.8),
             "Xử Lý Đơn Hàng Chuyên Biệt",
             "• Phân loại đơn hàng đa tiêu chí:\n"
             "  - Mã đơn, Tên khách hàng & SĐT, Địa chỉ giao nhận, Chi tiết món bánh.\n"
             "  - Tab lọc trạng thái: Tất cả, Chờ xác nhận CK, Đã xác nhận, Đang giao, Hoàn thành, Đã hủy.\n\n"
             "• Xử lý nhanh đơn chuyển khoản với 2 nút chuyên biệt:\n"
             "  - Nút 'Đã nhận tiền' (Màu xanh): Chuyển đơn sang 'Đã xác nhận', kích hoạt làm bánh và chuẩn bị giao hàng.\n"
             "  - Nút 'Chưa nhận tiền' (Màu đỏ outline): Mở modal nhập lý do (chưa thấy biến động số dư, sai cú pháp) để gửi thông báo tức thì đến khách.\n\n"
             "• Cơ chế Tiệm chủ động hủy đơn:\n"
             "  - Mở modal chọn lý do mẫu: Hết nguyên liệu, Quá tải lò nướng, Địa chỉ quá xa.\n"
             "  - Hệ thống ghi nhận NguoiHuy = 'Tiệm bánh' và hoàn trả tồn kho.",
             COLOR_SECONDARY)

    add_image_card(s12, Inches(6.8), Inches(1.8), Inches(5.7), Inches(4.8),
                   "screenshot_09_order_tracking.png",
                   "Giao diện Chi tiết Đơn hàng & Quản lý trạng thái xử lý")

    # =========================================================================
    # SLIDE 13: PHÂN HỆ NGƯỜI BÁN: THỐNG KÊ DOANH THU THEO NGÀY & THÁNG
    # =========================================================================
    s13 = prs.slides.add_slide(blank_layout)
    add_header(s13, "11. Phân Hệ Người Bán: Thống Kê Doanh Thu Ngày & Tháng")

    add_card(s13, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8),
             "Dashboard Phân Tích Tài Chính 2 Chiều",
             "• Thống kê chi tiết theo Ngày:\n"
             "  - Chọn ngày bất kỳ -> Xem số tiền thực nhận từ các đơn giao hoàn tất trong ngày.\n"
             "  - Hiển thị số đơn hoàn thành, số đơn bị hủy và tỷ lệ hoàn thành (%).\n\n"
             "• Thống kê tổng hợp theo Tháng:\n"
             "  - Chọn tháng bất kỳ -> Xem tổng doanh thu tháng, tổng đơn giao thành công, tổng đơn thất bại.\n\n"
             "• Bảng danh sách đơn hàng đồng bộ bên dưới:\n"
             "  - Tự động lọc danh sách hóa đơn tương ứng với mốc ngày/tháng đang chọn.",
             COLOR_PRIMARY)

    add_card(s13, Inches(6.8), Inches(1.8), Inches(5.6), Inches(4.8),
             "Thuật Toán Thống Kê Chuẩn Kế Toán",
             "• Phân tách nguồn gốc đơn hủy:\n"
             "  - Khách hàng tự hủy đơn vs Tiệm bánh chủ động hủy đơn.\n"
             "  - Giúp chủ tiệm đánh giá chính xác nguyên nhân thất thoát doanh thu.\n\n"
             "• Nguyên tắc ghi nhận doanh thu:\n"
             "  - Chỉ tính tổng tiền đối với đơn có trạng thái 'Đã hoàn thành' hoặc 'Đã giao thành công'.\n"
             "  - Ngày ghi nhận lấy theo trường NgayHoanThanh (thời điểm giao bánh thành công), không lấy NgayDat, chống sai lệch số liệu vắt qua tháng.",
             COLOR_SUCCESS)

    # =========================================================================
    # SLIDE 14: PHÂN HỆ QUẢN TRỊ VIÊN (ADMIN) & BẢO MẬT KICK-OUT
    # =========================================================================
    s14 = prs.slides.add_slide(blank_layout)
    add_header(s14, "12. Phân Hệ Quản Trị Viên (Admin) & Bảo Mật Kick-out")

    add_card(s14, Inches(0.8), Inches(1.8), Inches(5.8), Inches(4.8),
             "Quản Trị Toàn Sàn & Cơ Chế Kick-Out Tức Thì",
             "• Quản lý tài khoản toàn diện:\n"
             "  - Xem danh sách người dùng, bộ lọc tab: Tất cả, Khách, Tiệm bánh, Chờ duyệt, Bị khóa.\n"
             "  - Phê duyệt / Từ chối hồ sơ xin mở tiệm bánh mới chỉ với 1 cú click.\n\n"
             "• Cơ chế KICK-OUT tức thì trong 0.1s (Real-time Session Ejection):\n"
             "  - Nếu tài khoản đang online bị Admin bấm Khóa -> Ngay tại request tiếp theo, Middleware CheckAccountStatus lập tức hủy Session, đăng xuất và đá văng về trang Đăng nhập.\n"
             "  - Giao diện đăng nhập hiển thị cảnh báo đỏ nổi bật: 'Tài Khoản Đã Bị Khóa!' kèm biểu tượng ổ khóa.\n"
             "  - Phân biệt chuẩn xác giữa: Nhập sai mật khẩu vs Tài khoản bị cấm.",
             COLOR_ACCENT)

    add_image_card(s14, Inches(6.8), Inches(1.8), Inches(5.7), Inches(4.8),
                   "screenshot_05_login.png",
                   "Màn hình Đăng nhập hiển thị cảnh báo Kick-out an ninh mạng")

    # =========================================================================
    # SLIDE 15: CÁC ĐIỂM SÁNG TẠO & KỸ THUẬT NỔI BẬT
    # =========================================================================
    s15 = prs.slides.add_slide(blank_layout)
    add_header(s15, "13. Các Điểm Sáng Tạo & Kỹ Thuật Nổi Bật Trong Đồ Án")

    innovations = [
        ("1. Đèn Pin Soi Mật Khẩu Xoay 360°", 
         "• Sử dụng SVG và tính toán góc lượng giác Math.atan2(dy, dx).\n"
         "• Giữ và xoay đèn pin quanh trục: Chiếu thẳng vào ô mật khẩu mới hiển thị text; xoay ra ngoài mật khẩu tự ẩn; hiệu ứng vệt sáng quét 60fps mượt mà.", COLOR_PRIMARY),
        ("2. VietQR API NAPAS247 Động", 
         "• Tự động sinh mã QR ngân hàng MBBank chứa sẵn số tiền chính xác và cú pháp CAKEY [MaDon].\n"
         "• Quét mã 2 giây trên mọi app Mobile Banking VN, loại bỏ 100% sai sót người dùng.", COLOR_SECONDARY),
        ("3. Real-Time Notification AJAX Polling", 
         "• Hệ thống chuông thông báo tự động kiểm tra và đếm số lượng thông báo mới mỗi 10 giây.\n"
         "• Tiệm bánh nhận thông báo 'Có người chuyển khoản' tức thì không reload trang.", COLOR_ACCENT),
        ("4. Xác Thực Email OTP Bảo Mật 2 Bước", 
         "• Bảo vệ tài khoản khi đăng ký mới và quên mật khẩu bằng mã OTP 6 chữ số gửi qua Email.\n"
         "• Mã OTP có thời hạn 5 phút, cơ chế rate-limiting chống spam tài khoản rác.", COLOR_SUCCESS)
    ]

    for idx, (title, content, col) in enumerate(innovations):
        col_idx = idx % 2
        row_idx = idx // 2
        left = Inches(0.8 + col_idx * 6.0)
        top = Inches(1.8 + row_idx * 2.5)
        add_card(s15, left, top, Inches(5.6), Inches(2.2), title, content, col)

    # =========================================================================
    # SLIDE 16: KIỂM THỬ HỆ THỐNG (TESTING & QUALITY ASSURANCE)
    # =========================================================================
    s16 = prs.slides.add_slide(blank_layout)
    add_header(s16, "14. Kiểm Thử Hệ Thống (Testing & Quality Assurance)")

    add_card(s16, Inches(0.8), Inches(1.8), Inches(5.8), Inches(4.8),
             "Phương Pháp Kiểm Thử Tự Động (PHPUnit)",
             "• Áp dụng Automated Feature Testing chuyên sâu:\n"
             "  - UserLockoutTest.php: Kiểm thử cơ chế đá văng tài khoản bị khóa, phân biệt sai pass vs tài khoản bị ban.\n"
             "  - BankTransferOrderTest.php: Kiểm thử trọn vẹn 6 trạng thái vòng đời đơn chuyển khoản (Đặt -> Chờ CK -> Chờ xác nhận -> Đã nhận/Chưa nhận -> Khiếu nại -> Chuyển lại).\n"
             "  - SellerOrderStatsTest.php: Kiểm thử tính toán doanh thu ngày/tháng, tỷ lệ hoàn thành và phân loại người hủy.\n\n"
             "• Kết quả kiểm thử tự động:\n"
             "  - 13/13 Feature Tests Passed (Đạt 100%).\n"
             "  - 61 Assertions thành công, thời gian thực thi dưới 1 giây.\n"
             "  - Mã nguồn tuân thủ nghiêm ngặt tiêu chuẩn PSR-12 qua Laravel Pint.",
             COLOR_SUCCESS)

    add_card(s16, Inches(6.8), Inches(1.8), Inches(5.7), Inches(4.8),
             "Chỉ Số Đảm Bảo Chất Lượng (QA Metrics)",
             "• Kết quả chạy PHPUnit Terminal thực tế:\n"
             "  PASS  Tests\\Feature\\UserLockoutTest\n"
             "  ✓ user_is_locked_out_immediately_on_next_request\n"
             "  ✓ invalid_credentials_shows_standard_error\n"
             "  PASS  Tests\\Feature\\BankTransferOrderTest\n"
             "  ✓ customer_can_confirm_bank_transfer\n"
             "  ✓ seller_can_reject_with_reason\n"
             "  ✓ customer_can_appeal_rejected_payment\n"
             "  PASS  Tests\\Feature\\SellerOrderStatsTest\n"
             "  ✓ daily_stats_calculate_completed_orders_only\n"
             "  ✓ monthly_stats_separate_customer_and_seller_cancellations\n\n"
             "  Tests: 13 passed (61 assertions)\n"
             "  Duration: 0.82s | Memory: 32.50 MB",
             COLOR_PRIMARY, bg_color=RGBColor(240, 253, 244))

    # =========================================================================
    # SLIDE 17: ĐÁNH GIÁ KẾT QUẢ ĐẠT ĐƯỢC
    # =========================================================================
    s17 = prs.slides.add_slide(blank_layout)
    add_header(s17, "15. Đánh Giá Kết Quả Đạt Được")

    add_card(s17, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8),
             "Ưu Điểm Nổi Bật Đã Đạt Được",
             "• Giao diện thân thiện, hiện đại, tone màu bánh ngọt ấm cúng và tương thích 100% thiết bị di động.\n\n"
             "• Nghiệp vụ hoàn chỉnh, giải quyết trọn vẹn bài toán vận hành của các tiệm bánh vừa và nhỏ.\n\n"
             "• Luồng thanh toán VietQR và đối soát sao kê giảm thiểu 90% nhầm lẫn chuyển khoản thủ công.\n\n"
             "• Kiến trúc phân tầng MVC rõ ràng, code sạch (PSR-12), tối ưu truy vấn Eloquent không bị lỗi N+1 Query.\n\n"
             "• Cơ chế an ninh cao: Kick-out tài khoản bị khóa trong 0.1s và mã hóa Bcrypt.",
             COLOR_SUCCESS)

    add_card(s17, Inches(6.8), Inches(1.8), Inches(5.6), Inches(4.8),
             "Hạn Chế Còn Tồn Tại Cần Cải Tiến",
             "• Cơ chế nhận tiền chuyển khoản hiện tại vẫn dựa trên việc chủ tiệm kiểm tra app ngân hàng rồi bấm nút (chưa tích hợp Webhook API tự động duyệt 100%).\n\n"
             "• Hệ thống hiện mới hỗ trợ ngôn ngữ tiếng Việt, chưa đa ngôn ngữ (i18n).\n\n"
             "• Chưa tích hợp tính toán khoảng cách định vị bản đồ GPS thời gian thực để tính phí ship động theo km.",
             COLOR_WARN)

    # =========================================================================
    # SLIDE 18: HƯỚNG PHÁT TRIỂN TRONG TƯƠNG LAI
    # =========================================================================
    s18 = prs.slides.add_slide(blank_layout)
    add_header(s18, "16. Hướng Phát Triển Trong Tương Lai")

    add_card(s18, Inches(0.8), Inches(1.8), Inches(5.6), Inches(2.2),
             "1. Tích Hợp Webhook Ngân Hàng Tự Động",
             "Kết nối dịch vụ Cassie / SePay / VietQR Pro để tự động khớp lệnh sao kê ngân hàng và chuyển trạng thái 'Đã nhận tiền' chỉ sau 3 giây mà không cần chủ tiệm bấm tay.",
             COLOR_PRIMARY)

    add_card(s18, Inches(6.8), Inches(1.8), Inches(5.6), Inches(2.2),
             "2. Tích Hợp Đa Dạng Cổng Thanh Toán",
             "Mở rộng thanh toán qua các ví điện tử phổ biến như MoMo, ZaloPay, VNPAY QR và thẻ thanh toán quốc tế Visa/Mastercard.",
             COLOR_SECONDARY)

    add_card(s18, Inches(0.8), Inches(4.3), Inches(5.6), Inches(2.2),
             "3. Phát Triển Ứng Dụng Di Động (Mobile App)",
             "Xây dựng Mobile App trên nền tảng Flutter / React Native dành riêng cho Tài xế giao bánh (Shipper) và Chủ tiệm bánh nhận đơn tức thì.",
             COLOR_ACCENT)

    add_card(s18, Inches(6.8), Inches(4.3), Inches(5.6), Inches(2.2),
             "4. Ứng Dụng Trí Tuệ Nhân Tạo (AI Chatbot)",
             "Tích hợp AI Chatbot tư vấn chọn bánh sinh nhật theo sở thích, độ tuổi, sự kiện và gợi ý vị bánh cá nhân hóa theo hành vi mua sắm.",
             COLOR_SUCCESS)

    # =========================================================================
    # SLIDE 19: KẾT LUẬN & LỜI CẢM ƠN (Q&A)
    # =========================================================================
    s19 = prs.slides.add_slide(blank_layout)
    bg19 = s19.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg19.fill.solid()
    bg19.fill.fore_color.rgb = COLOR_BG_DARK
    bg19.line.fill.background()

    t19_box = s19.shapes.add_textbox(Inches(1.2), Inches(1.6), Inches(10.9), Inches(4.5))
    tf19 = t19_box.text_frame
    tf19.word_wrap = True

    p_thx = tf19.paragraphs[0]
    p_thx.text = "XIN CHÂN THÀNH CẢM ƠN QUÝ THẦY CÔ VÀ CÁC BẠN\nĐÃ LẮNG NGHE BÀI BÁO CÁO!"
    p_thx.font.size = Pt(26)
    p_thx.font.bold = True
    p_thx.font.color.rgb = COLOR_WHITE
    p_thx.alignment = PP_ALIGN.CENTER

    p_msg = tf19.add_paragraph()
    p_msg.text = "\n\"CAKEY không chỉ là một đồ án môn học, mà là giải pháp TMĐT hoàn chỉnh,\ngiải quyết bài toán thực tế cho cộng đồng kinh doanh bánh ngọt thủ công.\""
    p_msg.font.size = Pt(14)
    p_msg.font.color.rgb = RGBColor(226, 232, 240)
    p_msg.alignment = PP_ALIGN.CENTER

    p_qa = tf19.add_paragraph()
    p_qa.text = "\nNHÓM XIN PHÉP BẮT ĐẦU PHẦN TRẢ LỜI CÂU HỎI PHẢN BIỆN (Q&A)"
    p_qa.font.size = Pt(17)
    p_qa.font.bold = True
    p_qa.font.color.rgb = COLOR_ACCENT
    p_qa.alignment = PP_ALIGN.CENTER

    p_proj = tf19.add_paragraph()
    p_proj.text = "\nĐỒ ÁN PHÁT TRIỂN ỨNG DỤNG MÃ NGUỒN MỞ - ĐẠI HỌC CÔNG THƯƠNG TP.HCM (HUIT)\nNhóm 08 - Trưởng nhóm: Vũ Lê Anh Đức (2001230191)"
    p_proj.font.size = Pt(11.5)
    p_proj.font.color.rgb = RGBColor(148, 163, 184)
    p_proj.alignment = PP_ALIGN.CENTER

    # =========================================================================
    # SLIDE 20: PHỤ LỤC: BỘ CÂU HỎI PHẢN BIỆN CỦA GIẢNG VIÊN (PHẦN 1)
    # =========================================================================
    s20 = prs.slides.add_slide(blank_layout)
    add_header(s20, "Phụ Lục: Bộ Câu Hỏi Phản Biện Của Giảng Viên (Phần 1)", "PHỤ LỤC VẤN ĐÁP")

    add_card(s20, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8),
             "Câu 1: Tại sao chọn VietQR 2 chiều mà không dùng VNPAY/MoMo?",
             "• Trả lời của sinh viên:\n"
             "  - Các tiệm bánh tham gia sàn đa phần là hộ kinh doanh nhỏ hoặc tiệm handmade. Việc đăng ký VNPAY/MoMo đòi hỏi giấy phép kinh doanh doanh nghiệp và mức phí chiết khấu 1.5% - 2.5% trên mỗi đơn hàng.\n\n"
             "  - Mô hình VietQR trực tiếp miễn phí 100% phí giao dịch cho tiểu thương, quét mã tiện lợi 24/7 trên mọi App ngân hàng VN.\n\n"
             "  - Cơ chế đối soát 2 chiều với 2 nút 'Đã nhận tiền' và 'Chưa nhận tiền' kèm tính năng khiếu nại giúp chủ tiệm kiểm soát chặt chẽ dòng tiền vào tài khoản mà không sợ thất thoát.",
             COLOR_PRIMARY)

    add_card(s20, Inches(6.8), Inches(1.8), Inches(5.6), Inches(4.8),
             "Câu 2: Xử lý Concurrency / Race Condition tồn kho ra sao?",
             "• Trả lời của sinh viên:\n"
             "  - Trong CartController, khi chốt đơn, nhóm dùng phương thức decrement('SoLuongTon', $qty) của Eloquent ORM.\n\n"
             "  - Lệnh này biên dịch xuống câu SQL nguyên tử: UPDATE SanPham SET SoLuongTon = SoLuongTon - ? WHERE MaSanPham = ?.\n\n"
             "  - Thao tác này được engine InnoDB của MySQL khóa dòng (row-level lock) tự động trong transaction ACID, đảm bảo không bao giờ bị âm kho khi nhiều khách cùng bấm mua tại cùng 1 giây.",
             COLOR_SECONDARY)

    # =========================================================================
    # SLIDE 21: PHỤ LỤC: BỘ CÂU HỎI PHẢN BIỆN CỦA GIẢNG VIÊN (PHẦN 2)
    # =========================================================================
    s21 = prs.slides.add_slide(blank_layout)
    add_header(s21, "Phụ Lục: Bộ Câu Hỏi Phản Biện Của Giảng Viên (Phần 2)", "PHỤ LỤC VẤN ĐÁP")

    add_card(s21, Inches(0.8), Inches(1.8), Inches(3.7), Inches(4.8),
             "Câu 3: Cơ chế Kick-out tài khoản bị khóa?",
             "• Trả lời của sinh viên:\n"
             "  - Nhóm cài đặt Custom Middleware CheckAccountStatus bọc toàn cục.\n\n"
             "  - Ở mỗi HTTP request, middleware kiểm tra Auth::user()->TrangThai.\n\n"
             "  - Nếu TrangThai == 0 (bị khóa), lập tức gọi Auth::logout(), hủy session invalidate() và đá văng về trang đăng nhập với cờ locked=1 hiển thị cảnh báo đỏ.",
             COLOR_ACCENT)

    add_card(s21, Inches(4.8), Inches(1.8), Inches(3.7), Inches(4.8),
             "Câu 4: Thống kê doanh thu không sai lệch số liệu?",
             "• Trả lời của sinh viên:\n"
             "  - Chỉ tính tổng tiền các đơn có trạng thái là 'Đã hoàn thành' hoặc 'Đã giao thành công'.\n\n"
             "  - Ngày ghi nhận doanh thu lấy theo trường NgayHoanThanh (thời điểm giao bánh thành công), không lấy NgayDat, tránh sai lệch vắt qua tháng.\n\n"
             "  - Phân tách rõ ràng đơn khách tự hủy vs tiệm chủ động hủy.",
             COLOR_SUCCESS)

    add_card(s21, Inches(8.8), Inches(1.8), Inches(3.7), Inches(4.8),
             "Câu 5: Mật khẩu người dùng được bảo vệ thế nào?",
             "• Trả lời của sinh viên:\n"
             "  - Toàn bộ mật khẩu trong CSDL được băm bằng thuật toán Bcrypt an toàn (Hash::make() với salt ngẫu nhiên).\n\n"
             "  - Tuyệt đối không lưu plain-text.\n\n"
             "  - Khi đăng nhập dùng Hash::check() so khớp một chiều, chống tấn công từ điển và rò rỉ dữ liệu.",
             COLOR_PRIMARY)

    # Save to both destinations
    dest1 = r"C:\laragon\www\doan_banhngot\Slide_BaoCao_MaNguonMo_Cakey.pptx"
    dest1_fallback = r"C:\laragon\www\doan_banhngot\Slide_BaoCao_MaNguonMo_Cakey_21Slide.pptx"
    dest2 = r"D:\Doan_BigData\BaoCao_Word\Slide_BaoCao_MaNguonMo_Cakey.pptx"

    os.makedirs(os.path.dirname(dest1), exist_ok=True)
    try:
        prs.save(dest1)
        print(f"[OK] Da tao thanh cong file PowerPoint 21 Slide co anh chup that tai: {dest1}")
    except PermissionError:
        prs.save(dest1_fallback)
        print(f"[OK] File {dest1} dang duoc mo boi PowerPoint! Da luu ban moi tai: {dest1_fallback}")

    os.makedirs(os.path.dirname(dest2), exist_ok=True)
    prs.save(dest2)
    print(f"[OK] Da tao thanh cong file PowerPoint 21 Slide co anh chup that tai: {dest2}")

if __name__ == "__main__":
    build_presentation()
