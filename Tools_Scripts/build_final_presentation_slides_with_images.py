# -*- coding: utf-8 -*-
"""
Script xay dung lai toan bo bo Slide PowerPoint Slide_BaoCao_MaNguonMo_Cakey.pptx
tich hop 100% anh chup man hinh that tu he thong Web Cakey dang chay!
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
        p_title.font.size = Pt(22)
        p_title.font.bold = True
        p_title.font.color.rgb = COLOR_PRIMARY
        p_title.space_before = Pt(4)

        line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.5), Inches(11.7), Inches(0.04))
        line.fill.solid()
        line.fill.fore_color.rgb = COLOR_ACCENT
        line.line.color.rgb = COLOR_ACCENT

    def add_card(slide, left, top, width, height, title, content, border_color=COLOR_PRIMARY):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_CARD_BG
        card.line.color.rgb = border_color
        card.line.width = Pt(1.5)
        
        tb = slide.shapes.add_textbox(left + Inches(0.2), top + Inches(0.2), width - Inches(0.4), height - Inches(0.4))
        tf = tb.text_frame
        tf.word_wrap = True
        
        p_t = tf.paragraphs[0]
        p_t.text = title
        p_t.font.size = Pt(14)
        p_t.font.bold = True
        p_t.font.color.rgb = border_color
        
        p_c = tf.add_paragraph()
        p_c.text = content
        p_c.font.size = Pt(11)
        p_c.font.color.rgb = COLOR_TEXT_DARK
        p_c.space_before = Pt(5)

    def add_image_card(slide, left, top, width, height, img_filename, caption_text):
        img_path = os.path.join(img_dir, img_filename)
        # Background card frame
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_WHITE
        card.line.color.rgb = RGBColor(203, 213, 225)
        card.line.width = Pt(1.5)

        if os.path.exists(img_path):
            img_width = width - Inches(0.3)
            pic = slide.shapes.add_picture(img_path, left + Inches(0.15), top + Inches(0.15), width=img_width)
            # Adjust caption below picture
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
    # SLIDE 1: TRANG BÌA (TITLE SLIDE)
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    bg1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = COLOR_BG_DARK
    bg1.line.fill.background()

    t1_box = s1.shapes.add_textbox(Inches(1.2), Inches(1.2), Inches(10.9), Inches(5.0))
    tf1 = t1_box.text_frame
    tf1.word_wrap = True

    p_u = tf1.paragraphs[0]
    p_u.text = "TRƯỜNG ĐẠI HỌC CÔNG THƯƠNG TP. HỒ CHÍ MINH (HUIT)\nKHOA CÔNG NGHỆ THÔNG TIN - BỘ MÔN CÔNG NGHỆ PHẦN MỀM"
    p_u.font.size = Pt(13)
    p_u.font.bold = True
    p_u.font.color.rgb = RGBColor(148, 163, 184)

    p_m = tf1.add_paragraph()
    p_m.text = "\nBÁO CÁO ĐỒ ÁN HỌC PHẦN: MÃ NGUỒN MỞ"
    p_m.font.size = Pt(16)
    p_m.font.bold = True
    p_m.font.color.rgb = COLOR_ACCENT

    p_main = tf1.add_paragraph()
    p_main.text = "XÂY DỰNG WEBSITE BÁN BÁNH NGỌT CAKEY"
    p_main.font.size = Pt(32)
    p_main.font.bold = True
    p_main.font.color.rgb = COLOR_WHITE
    p_main.space_before = Pt(8)

    p_sub = tf1.add_paragraph()
    p_sub.text = "Hệ thống sàn thương mại điện tử Multi-vendor chuyên biệt ngành bánh\n(Nền tảng: Laravel 11, MySQL, Blade Template, Bootstrap 5, AJAX & VietQR API)"
    p_sub.font.size = Pt(14)
    p_sub.font.color.rgb = RGBColor(226, 232, 240)
    p_sub.space_before = Pt(8)

    p_info = tf1.add_paragraph()
    p_info.text = "\nSinh viên thực hiện: Vũ Lê Anh Đức (MSSV: 2001230191 - Trưởng nhóm)\nCác thành viên: Nguyễn Hoàng Long (2001230188), Trần Minh Quân (2001230195), Lê Thị Kim Ngân (2001230182)\nGiảng viên phụ trách học phần: Khoa CNTT - HUIT"
    p_info.font.size = Pt(12)
    p_info.font.color.rgb = RGBColor(148, 163, 184)

    # =========================================================================
    # SLIDE 2: TỔNG QUAN & LÝ DO CHỌN ĐỀ TÀI
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    add_header(s2, "1. Tổng Quan & Lý Do Chọn Đề Tài")

    add_card(s2, Inches(0.8), Inches(1.8), Inches(5.8), Inches(4.8), 
             "Bối Cảnh & Giải Pháp Đề Tài",
             "• Bối cảnh: Ngành ẩm thực F&B bánh ngọt phát triển bùng nổ. Người tiêu dùng có nhu cầu đặt bánh kem, bánh sinh nhật, tiệc ngọt online nhanh chóng.\n\n"
             "• Thực trạng: Các tiệm bánh thủ công bán qua tin nhắn dễ bị sót đơn, nhầm lẫn tiền chuyển khoản và không quản lý được lượng bánh tồn trong ngày.\n\n"
             "• Giải pháp: Xây dựng Website Bán Hàng Online (Đề tài số 3 trong danh mục gợi ý của giảng viên) mang tên CAKEY.\n\n"
             "• Bước đột phá: Phát triển thành mô hình Sàn Bánh Ngọt Multi-vendor hỗ trợ 3 nhóm đối tượng: Khách mua, Chủ tiệm bánh và Quản trị viên sàn.",
             COLOR_PRIMARY)

    add_image_card(s2, Inches(6.8), Inches(1.8), Inches(5.7), Inches(4.8),
                   "screenshot_01_homepage.png",
                   "Giao diện Trang chủ CAKEY với banner & sản phẩm nổi bật")

    # =========================================================================
    # SLIDE 3: CÔNG NGHỆ SỬ DỤNG & KIẾN TRÚC HỆ THỐNG
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    add_header(s3, "2. Công Nghệ Sử Dụng & Kiến Trúc Hệ Sinh Thái")

    tech_items = [
        ("Backend Framework", "Laravel Framework 11.x\n• Kiến trúc chuẩn MVC\n• Eloquent ORM truy vấn quan hệ\n• Middleware kiểm soát phân quyền\n• Form Request Validation chặt chẽ", COLOR_PRIMARY),
        ("Cơ Sở Dữ Liệu", "MySQL Database (InnoDB)\n• 8 bảng dữ liệu quan hệ chuẩn hóa\n• Ràng buộc khóa ngoại Foreign Keys\n• Hỗ trợ Transaction toàn vẹn đơn hàng\n• Migration & Seeder tự động", COLOR_SECONDARY),
        ("Frontend & Giao Diện", "Blade Template + Bootstrap 5\n• Giao diện Responsive Mobile\n• Tương tác không reload qua AJAX\n• Icon FontAwesome 6 trực quan\n• Bảng điều khiển quản trị hiện đại", COLOR_ACCENT),
        ("Tích Hợp Bên Ngoài (API)", "VietQR API & Email Service\n• Tạo mã QR thanh toán động VietQR\n• Tự động khớp số tiền và nội dung\n• Gửi mã xác thực OTP qua Email\n• Cơ chế In-App Notification tức thời", COLOR_PRIMARY)
    ]

    for idx, (title, content, col) in enumerate(tech_items):
        col_idx = idx % 2
        row_idx = idx // 2
        left = Inches(0.8 + col_idx * 6.0)
        top = Inches(1.8 + row_idx * 2.5)
        add_card(s3, left, top, Inches(5.6), Inches(2.2), title, content, col)

    # =========================================================================
    # SLIDE 4: THIẾT KẾ CƠ SỞ DỮ LIỆU (ERD)
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    add_header(s4, "3. Thiết Kế Cơ Sở Dữ Liệu (CSDL) & Sơ Đồ Quan Hệ (ERD)")

    table_box = s4.shapes.add_textbox(Inches(0.8), Inches(1.8), Inches(11.7), Inches(0.5))
    tf4 = table_box.text_frame
    p4_desc = tf4.paragraphs[0]
    p4_desc.text = "Hệ thống CSDL 'BanhNgot' gồm 8 bảng dữ liệu chuẩn hóa, có quan hệ ràng buộc toàn vẹn khóa ngoại (Foreign Keys):"
    p4_desc.font.size = Pt(13)
    p4_desc.font.bold = True
    p4_desc.font.color.rgb = COLOR_PRIMARY

    erd_table = s4.shapes.add_table(rows=9, cols=4, left=Inches(0.8), top=Inches(2.3), width=Inches(11.7), height=Inches(4.5)).table
    erd_headers = ["Tên Bảng (Table)", "Khóa Chính (PK)", "Khóa Ngoại (FK)", "Ý Nghĩa Nghiệp Vụ & Quan Hệ"]
    for i, h in enumerate(erd_headers):
        cell = erd_table.cell(0, i)
        cell.text = h
        cell.fill.solid()
        cell.fill.fore_color.rgb = COLOR_PRIMARY
        p = cell.text_frame.paragraphs[0]
        p.font.bold = True
        p.font.color.rgb = COLOR_WHITE
        p.font.size = Pt(11)

    erd_data = [
        ("nguoidung (Users)", "MaND", "-", "Lưu tài khoản, mật khẩu băm Bcrypt, quyền hạn (Admin, Seller, User), trạng thái khóa"),
        ("CuaHang (Shops)", "MaCuaHang", "MaND -> nguoidung", "Thông tin tiệm bánh do Seller sở hữu (1 User NguoiBan sở hữu 1 Cửa Hàng)"),
        ("danhmuc (Categories)", "MaDanhMuc", "-", "Phân loại bánh (Bánh Mì, Bánh Ngọt, Bánh Sinh Nhật, Cupcake...)"),
        ("SanPham (Products)", "MaSanPham", "MaDanhMuc, MaCuaHang", "Món bánh: Giá bán, tồn kho, hình ảnh, mô tả, trạng thái (Đang bán, Tạm gỡ, Chờ duyệt)"),
        ("GioHang (Cart)", "id (Auto Inc)", "MaNguoiDung, MaSanPham", "Giỏ hàng tạm thời của khách hàng (lưu số lượng bánh, ngày thêm)"),
        ("DonHang (Orders)", "MaDon", "MaKhachHang -> nguoidung", "Đơn hàng: Họ tên nhận, SĐT, địa chỉ giao, PTTT (COD/Chuyển khoản), trạng thái, tổng tiền"),
        ("ChiTietDonHang (OrderItems)", "id (Auto Inc)", "MaDon, MaSanPham", "Chi tiết các món bánh trong đơn (Số lượng đặt, đơn giá tại thời điểm mua)"),
        ("ThongBao (Notifications)", "id (Auto Inc)", "user_id -> nguoidung", "Hộp thư thông báo tức thì: Đơn hàng mới, duyệt tiệm, trạng thái thanh toán")
    ]

    for r_idx, row in enumerate(erd_data, 1):
        for c_idx, val in enumerate(row):
            c = erd_table.cell(r_idx, c_idx)
            c.text = val
            p = c.text_frame.paragraphs[0]
            p.font.size = Pt(10)
            if c_idx == 0:
                p.font.bold = True
            c.fill.solid()
            c.fill.fore_color.rgb = COLOR_WHITE if r_idx % 2 == 1 else COLOR_CARD_BG

    # =========================================================================
    # SLIDE 5: SƠ ĐỒ USE CASE TỔNG QUÁT (UML USE CASE)
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    add_header(s5, "4. Sơ Đồ Use Case Tổng Quát (UML Use Case)")

    add_card(s5, Inches(0.8), Inches(1.8), Inches(3.7), Inches(4.8),
             "Actor 1: Khách Hàng (Customer)",
             "• Đăng ký / Đăng nhập Email OTP\n"
             "• Xem danh mục & tìm kiếm Live Search\n"
             "• Thêm / sửa / xóa giỏ hàng AJAX\n"
             "• Đặt hàng & thanh toán COD / VietQR\n"
             "• Xem lịch sử đơn hàng & Hủy đơn\n"
             "• Nộp đơn khiếu nại chuyển khoản\n"
             "• Nhận thông báo tiến độ đơn hàng\n"
             "• Nộp hồ sơ đăng ký mở tiệm bánh",
             COLOR_PRIMARY)

    add_card(s5, Inches(4.8), Inches(1.8), Inches(3.7), Inches(4.8),
             "Actor 2: Người Bán (Seller)",
             "• Đăng ký & quản lý hồ sơ tiệm bánh\n"
             "• Đăng món bánh mới (Upload ảnh)\n"
             "• Chỉnh sửa thông tin & giá bánh\n"
             "• Xóa mềm (Tạm ẩn) & Khôi phục bánh\n"
             "• Xem danh sách đơn hàng đặt tại tiệm\n"
             "• Cập nhật trạng thái đơn (Duyệt, Giao)\n"
             "• Xác nhận / Từ chối chuyển khoản\n"
             "• Nhận thông báo khi có đơn hàng mới",
             COLOR_SECONDARY)

    add_card(s5, Inches(8.8), Inches(1.8), Inches(3.7), Inches(4.8),
             "Actor 3: Quản Trị Viên (Admin)",
             "• Quản lý danh sách tài khoản người dùng\n"
             "• Phê duyệt / Từ chối tiệm bánh mới\n"
             "• Khóa / Mở khóa tài khoản vi phạm\n"
             "• Kiểm duyệt toàn bộ món bánh sàn\n"
             "• Xóa cứng / Khôi phục sản phẩm\n"
             "• Quản lý và đổi trạng thái toàn bộ đơn\n"
             "• Thống kê người dùng & doanh thu sàn",
             COLOR_ACCENT)

    # =========================================================================
    # SLIDE 6: CHỨC NĂNG DÀNH CHO KHÁCH HÀNG (KÈM ẢNH THẬT SẢN PHẨM & PHÂN TRANG)
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    add_header(s6, "5. Chức Năng Khách Hàng (Customer / Client)")

    add_card(s6, Inches(0.8), Inches(1.8), Inches(5.8), Inches(4.8),
             "Chi Tiết Tính Năng Khách Hàng",
             "• Tìm kiếm Live Search AJAX: Gợi ý tức thì ngay khi gõ từ khóa, không cần reload trang.\n\n"
             "• Lọc theo danh mục: Bánh kem sinh nhật, Bánh mì mặn, Cupcake, Bánh ăn kiêng.\n\n"
             "• Phân trang chuẩn Bootstrap 5: Phân chia 8 bánh/trang bằng Paginator::useBootstrapFive(), bảo lưu từ khóa tìm kiếm khi chuyển trang.\n\n"
             "• Giỏ hàng AJAX: Thêm bánh, cập nhật số lượng trực tiếp và hiển thị popup thông báo đẹp mắt.\n\n"
             "• Thanh toán quét mã VietQR: Tự động sinh mã ngân hàng MBBank điền sẵn số tiền hóa đơn.",
             COLOR_PRIMARY)

    add_image_card(s6, Inches(6.8), Inches(1.8), Inches(5.7), Inches(4.8),
                   "screenshot_03_products_catalog.png",
                   "Trang Danh mục Sản phẩm & Bộ lọc Bánh ngọt tại CAKEY")

    # =========================================================================
    # SLIDE 7: CHỨC NĂNG DÀNH CHO NGƯỜI BÁN (KÈM ẢNH SELLER DASHBOARD)
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    add_header(s7, "6. Chức Năng Chủ Tiệm Bánh (Seller / Shop Partner)")

    add_card(s7, Inches(0.8), Inches(1.8), Inches(5.8), Inches(4.8),
             "Chi Tiết Tính Năng Người Bán",
             "• Nộp hồ sơ mở tiệm: Khách hàng nộp đơn tại /seller/register, chờ Admin phê duyệt.\n\n"
             "• CRUD Quản lý món bánh: Đăng bánh mới, chỉnh sửa thông tin giá bán và số lượng tồn kho.\n\n"
             "• Upload file ảnh an toàn: Chọn ảnh từ máy tính tải lên public/img, kiểm tra MIME và dung lượng max 5MB.\n\n"
             "• Kỹ thuật Xóa mềm (Soft Delete): Tạm ẩn bánh khỏi sàn bán mà không làm mất liên kết trong các hóa đơn cũ.\n\n"
             "• Xử lý đơn hàng: Duyệt đơn, chuyển trạng thái giao hàng và bấm 'Xác nhận đã nhận tiền chuyển khoản'.",
             COLOR_SECONDARY)

    add_image_card(s7, Inches(6.8), Inches(1.8), Inches(5.7), Inches(4.8),
                   "screenshot_06_seller_dashboard.png",
                   "Giao diện Quản lý Sản phẩm của Chủ tiệm bánh (Seller Dashboard)")

    # =========================================================================
    # SLIDE 8: CHỨC NĂNG QUẢN TRỊ VIÊN (ADMIN)
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    add_header(s8, "7. Chức Năng Quản Trị Viên Toàn Quyền (Admin)")

    add_card(s8, Inches(0.8), Inches(1.8), Inches(5.8), Inches(4.8),
             "Chi Tiết Tính Năng Quản Trị Viên",
             "• Dashboard quản trị 3D: Giám sát toàn bộ lưu lượng, doanh số và người dùng trên sàn.\n\n"
             "• Phê duyệt tiệm bánh mới: 1-Click phê duyệt hồ sơ đối tác, nâng quyền tài khoản thành ROLE_NguoiBan.\n\n"
             "• Quản lý tài khoản & Khóa vi phạm: Bộ lọc tài khoản đa dạng (Tất cả, Chờ duyệt, Bị khóa), nút Khóa tài khoản có hành vi gian lận.\n\n"
             "• Kiểm duyệt sản phẩm toàn sàn: Tạm gỡ bánh không đạt chuẩn vệ sinh an toàn thực phẩm.\n\n"
             "• Trọng tài khiếu nại: Can thiệp xử lý các tranh chấp thanh toán chuyển khoản giữa khách và tiệm.",
             COLOR_ACCENT)

    add_image_card(s8, Inches(6.8), Inches(1.8), Inches(5.7), Inches(4.8),
                   "screenshot_05_login.png",
                   "Giao diện Xác thực Đăng nhập & Phân quyền bảo mật cao")

    # =========================================================================
    # SLIDE 9: ĐỐI CHIẾU 4 YÊU CẦU MỞ RỘNG (ĐIỂM CỘNG THEO ĐỀ BÀI)
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    add_header(s9, "8. Các Yêu Cầu Mở Rộng Đạt Điểm Cộng Tuyệt Đối (+1.0)")

    add_card(s9, Inches(0.8), Inches(1.8), Inches(5.8), Inches(4.8),
             "Đối Chiếu 4/4 Tiêu Chí Điểm Cộng Của Thầy",
             "1. Upload File (Hình Ảnh) [+0.25]:\n"
             "• Form đăng bánh cho phép tải ảnh từ máy tính lên public/img.\n"
             "• Validate đuôi file (jpg, png, webp) và dung lượng tối đa 5MB.\n\n"
             "2. Tương Tác AJAX Không Reload [+0.25]:\n"
             "• AJAX Live Search gợi ý bánh thời gian thực.\n"
             "• AJAX Giỏ hàng thêm và đổi số lượng trực tiếp.\n\n"
             "3. Tích Hợp API Bên Thứ Ba (VietQR) [+0.25]:\n"
             "• Gọi API https://img.vietqr.io tự động tạo mã QR ngân hàng MBBank kèm số tiền và mã đơn hàng chính xác.\n\n"
             "4. Giao Diện Responsive Mobile [+0.25]:\n"
             "• Bootstrap 5 Grid System co giãn hoàn hảo trên Smartphone.",
             COLOR_SUCCESS)

    add_image_card(s9, Inches(6.8), Inches(1.8), Inches(5.7), Inches(4.8),
                   "screenshot_08_checkout_vietqr.png",
                   "Màn hình Thanh toán VietQR & Các phương thức thanh toán")

    # =========================================================================
    # SLIDE 10: CÁC TÍNH NĂNG ĐẶC BIỆT LÀM THÊM VƯỢT BAREM
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    add_header(s10, "9. Các Tính Năng Đặc Biệt Làm Thêm Vượt Barem (5 Điểm Nhấn)")

    feature_cards = [
        ("1. Kiến Trúc Multi-Vendor 3 Cấp", 
         "Mô hình Sàn đa cửa hàng: Khách hàng mua sắm -> Nộp hồ sơ mở tiệm bánh -> Admin duyệt -> Trở thành Seller bán hàng độc lập.", COLOR_PRIMARY),
        ("2. Xác Thực Email OTP Bảo Mật", 
         "Gửi mã OTP 6 chữ số qua Email khi đăng ký tài khoản mới và khi thực hiện quy trình Quên mật khẩu, chống tài khoản rác.", COLOR_SECONDARY),
        ("3. Chuông Báo In-App Realtime", 
         "Hộp thư chuông báo nổi: Tự động đổi màu chuông và hiện số lượng khi có đơn hàng mới, khi đơn được duyệt và khi giao hàng.", COLOR_ACCENT),
        ("4. Đối Soát 2 Chiều & Khiếu Nại", 
         "Chủ tiệm xác nhận nhận tiền VietQR; Khách hàng có nút 'Gửi khiếu nại' kèm bằng chứng chuyển khoản nếu tiệm từ chối oan.", COLOR_PRIMARY),
        ("5. Xóa Mềm & Khôi Phục Sản Phẩm", 
         "Cơ chế Soft Delete: Tạm ẩn bánh hết hàng khỏi sàn bán nhưng giữ nguyên dữ liệu trong bảng ChiTietDonHang để báo cáo tài chính.", COLOR_SUCCESS)
    ]

    for idx, (title, content, col) in enumerate(feature_cards[:4]):
        col_idx = idx % 2
        row_idx = idx // 2
        left = Inches(0.8 + col_idx * 6.0)
        top = Inches(1.8 + row_idx * 2.5)
        add_card(s10, left, top, Inches(5.6), Inches(2.2), title, content, col)

    # =========================================================================
    # SLIDE 11: KỊCH BẢN DEMO TRỰC TIẾP TRÊN MÁY (LIVE DEMO)
    # =========================================================================
    s11 = prs.slides.add_slide(blank_layout)
    add_header(s11, "10. Kịch Bản Demo Trực Tiếp Sản Phẩm (Live Demo)")

    add_card(s11, Inches(0.8), Inches(1.8), Inches(5.8), Inches(4.8),
             "Quy Trình 4 Bước Trực Tiếp Trên Trình Duyệt",
             "• Bước 1 (Khách Hàng user@cakey.local):\n"
             "   Dùng Live Search tìm 'Bánh kem dâu tây' -> Thêm giỏ hàng -> Đặt hàng chọn Chuyển khoản VietQR -> Hệ thống sinh mã QR ngân hàng MBBank.\n\n"
             "• Bước 2 (Nộp Đơn Mở Tiệm Bánh):\n"
             "   Khách hàng vào mục Đăng ký bán hàng -> Nhập tên tiệm 'HUIT Bakery' -> Gửi hồ sơ chờ duyệt.\n\n"
             "• Bước 3 (Admin admin@cakey.local):\n"
             "   Admin vào duyệt tiệm bánh 'HUIT Bakery' -> Quyền hạn tự động nâng lên ROLE_NguoiBan.\n\n"
             "• Bước 4 (Seller Đăng Bánh & Xử Lý Đơn):\n"
             "   Chủ tiệm vào đăng món bánh mới có Upload ảnh -> Vào đơn hàng bấm 'Xác nhận đã nhận tiền chuyển khoản' cho đơn ở Bước 1.",
             COLOR_PRIMARY)

    add_image_card(s11, Inches(6.8), Inches(1.8), Inches(5.7), Inches(4.8),
                   "screenshot_09_order_tracking.png",
                   "Màn hình Theo dõi Đơn hàng & Trạng thái thanh toán của Khách")

    # =========================================================================
    # SLIDE 12: BẢNG PHÂN CÔNG CÔNG VIỆC NHÓM
    # =========================================================================
    s12 = prs.slides.add_slide(blank_layout)
    add_header(s12, "11. Bảng Phân Công Công Việc Giữa Các Thành Viên")

    team_table = s12.shapes.add_table(rows=5, cols=5, left=Inches(0.8), top=Inches(2.0), width=Inches(11.7), height=Inches(4.5)).table
    team_headers = ["STT", "Họ Và Tên", "MSSV", "Nhiệm Vụ Phụ Trách Chính Trong Dự Án", "Đánh Giá"]
    for i, h in enumerate(team_headers):
        cell = team_table.cell(0, i)
        cell.text = h
        cell.fill.solid()
        cell.fill.fore_color.rgb = COLOR_PRIMARY
        p = cell.text_frame.paragraphs[0]
        p.font.bold = True
        p.font.color.rgb = COLOR_WHITE
        p.font.size = Pt(11)

    team_data = [
        ("1", "Vũ Lê Anh Đức", "2001230191", "Trưởng nhóm: Kiến trúc Laravel 11, Auth & Middleware, Cổng VietQR API, Soft Delete, Pagination Bootstrap 5, Báo cáo & Slide", "100%"),
        ("2", "Nguyễn Hoàng Long", "2001230188", "Thành viên: Thiết kế CSDL MySQL (8 bảng), Viết Migration, Seeder, Xây dựng Seller Dashboard & Upload ảnh sản phẩm", "100%"),
        ("3", "Trần Minh Quân", "2001230195", "Thành viên: Thiết kế UI Blade Template + Bootstrap 5, AJAX Live Search sản phẩm, Giỏ hàng AJAX & Chuông thông báo In-App", "100%"),
        ("4", "Lê Thị Kim Ngân", "2001230182", "Thành viên: Xây dựng Module Checkout Khách hàng, Hệ thống Khiếu nại đơn hàng, Form Validation & Kiểm thử toàn diện", "100%")
    ]

    for r_idx, row in enumerate(team_data, 1):
        for c_idx, val in enumerate(row):
            c = team_table.cell(r_idx, c_idx)
            c.text = val
            p = c.text_frame.paragraphs[0]
            p.font.size = Pt(10)
            if c_idx in [0, 1, 4]:
                p.font.bold = True
            c.fill.solid()
            c.fill.fore_color.rgb = COLOR_WHITE if r_idx % 2 == 1 else COLOR_CARD_BG

    # =========================================================================
    # SLIDE 13: ĐÁNH GIÁ HỆ THỐNG & HƯỚNG PHÁT TRIỂN
    # =========================================================================
    s13 = prs.slides.add_slide(blank_layout)
    add_header(s13, "12. Đánh Giá Hệ Thống & Hướng Phát Triển")

    add_card(s13, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8),
             "Ưu Điểm Nổi Bật Đã Đạt Được",
             "• Hoàn thành 100% yêu cầu đề tài môn học Mã Nguồn Mở.\n\n"
             "• Đạt trọn vẹn 4/4 tiêu chuẩn điểm cộng của giảng viên (+1.0 điểm): Upload ảnh an toàn, AJAX không reload, VietQR API và Responsive Mobile.\n\n"
             "• Mở rộng 5 tính năng nâng cao thực tiễn: Multi-vendor 3 cấp bậc, Email OTP, In-App Notification, Quy trình xác nhận 2 chiều và Xóa mềm.\n\n"
             "• Mã nguồn sạch, áp dụng chuẩn MVC Laravel, Eloquent Model Relations và Custom Middleware bảo mật.",
             COLOR_SUCCESS)

    add_card(s13, Inches(6.8), Inches(1.8), Inches(5.6), Inches(4.8),
             "Hạn Chế & Hướng Mở Rộng Tương Lai",
             "• Tích hợp Webhook Ngân Hàng: Tự động bắt biến động số dư chuyển khoản để chuyển trạng thái 'Đã thanh toán' ngay tức khắc mà không cần Seller bấm tay.\n\n"
             "• Hệ thống Đánh giá & Bình luận: Cho phép khách mua đánh giá 5 sao kèm hình ảnh thực tế của món bánh sau khi nhận hàng.\n\n"
             "• Tích hợp API Bản đồ Google Maps / Mapbox: Tính toán chính xác khoảng cách giao hàng từ lò bánh đến nhà khách và tính phí ship tự động.",
             COLOR_SECONDARY)

    # =========================================================================
    # SLIDE 14: LỜI CẢM ƠN & PHẦN VẤN ĐÁP (Q&A)
    # =========================================================================
    s14 = prs.slides.add_slide(blank_layout)
    bg14 = s14.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg14.fill.solid()
    bg14.fill.fore_color.rgb = COLOR_BG_DARK
    bg14.line.fill.background()

    t14_box = s14.shapes.add_textbox(Inches(1.5), Inches(2.0), Inches(10.3), Inches(4.0))
    tf14 = t14_box.text_frame
    tf14.word_wrap = True

    p_thx = tf14.paragraphs[0]
    p_thx.text = "XIN CHÂN THÀNH CẢM ƠN THẦY VÀ CÁC BẠN\nĐÃ LẮNG NGHE BÀI BÁO CÁO!"
    p_thx.font.size = Pt(28)
    p_thx.font.bold = True
    p_thx.font.color.rgb = COLOR_WHITE
    p_thx.alignment = PP_ALIGN.CENTER

    p_qa = tf14.add_paragraph()
    p_qa.text = "\nNHÓM 08 XIN PHÉP BẮT ĐẦU PHẦN TRẢ LỜI CÂU HỎI VẤN ĐÁP (Q&A)"
    p_qa.font.size = Pt(16)
    p_qa.font.bold = True
    p_qa.font.color.rgb = COLOR_ACCENT
    p_qa.alignment = PP_ALIGN.CENTER

    p_proj = tf14.add_paragraph()
    p_proj.text = "\nCAKEY BAKERY SHOP - NỀN TẢNG THƯƠNG MẠI ĐIỆN TỬ BÁNH NGỌT HUIT\nThực hiện: Nhóm 08 - Trưởng nhóm: Vũ Lê Anh Đức (2001230191)"
    p_proj.font.size = Pt(12)
    p_proj.font.color.rgb = RGBColor(148, 163, 184)
    p_proj.alignment = PP_ALIGN.CENTER

    # Save to both destinations
    dest1 = r"C:\laragon\www\doan_banhngot\Slide_BaoCao_MaNguonMo_Cakey.pptx"
    dest2 = r"D:\Doan_BigData\BaoCao_Word\Slide_BaoCao_MaNguonMo_Cakey.pptx"

    os.makedirs(os.path.dirname(dest1), exist_ok=True)
    prs.save(dest1)
    print(f"[OK] Da tao thanh cong file PowerPoint co anh chup that tai: {dest1}")

    os.makedirs(os.path.dirname(dest2), exist_ok=True)
    prs.save(dest2)
    print(f"[OK] Da tao thanh cong file PowerPoint co anh chup that tai: {dest2}")

if __name__ == "__main__":
    build_presentation()
