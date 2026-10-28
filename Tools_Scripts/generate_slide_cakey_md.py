# -*- coding: utf-8 -*-
"""
Script tao file 'slide bao cao do an cakey.md' dong bo 100% voi Slide_BaoCao_MaNguonMo_Cakey.pptx.
Bao gom 14 slide:
- Bo cuc Visual & Noi dung slide
- Vi tri chen anh chup thuc te tu Web Cakey (Screenshot guidance)
- Loi thoai thuyet trinh chi tiet (Speaker Notes)
- Diem nhan ky thuat an diem barem
- Cau hoi phan bien du kien cua Giang vien & Cau tra loi chuan
"""

import os

md_content = """# SLIDE BÁO CÁO ĐỒ ÁN MÃ NGUỒN MỞ – WEBSITE BÁNH NGỌT CAKEY
**Tên tệp trình chiếu đi kèm:** `Slide_BaoCao_MaNguonMo_Cakey.pptx` (14 slide chuẩn Widescreen 16:9)  
**Vị trí tệp trình chiếu:** `C:\\laragon\\www\\doan_banhngot\\Slide_BaoCao_MaNguonMo_Cakey.pptx`  
**Đề tài:** Xây dựng Website Bán Hàng Trực Tuyến – Sàn Bánh Ngọt Đa Cửa Hàng CAKEY (Laravel 11 + MySQL)  
**Nhóm sinh viên thực hiện:**
1. **Vũ Lê Anh Đức** (MSSV: **2001230191** - Trưởng nhóm, Backend, Auth/Middleware, VietQR, Soft Delete)
2. **Nguyễn Hoàng Long** (MSSV: **2001230188** - Thành viên, CSDL MySQL, Migration, Seeder, Seller Module)
3. **Trần Minh Quân** (MSSV: **2001230195** - Thành viên, Frontend Blade + Bootstrap 5, AJAX Live Search & Cart)
4. **Lê Thị Kim Ngân** (MSSV: **2001230182** - Thành viên, Client Checkout, Khiếu nại, Validation Form)  
**Đơn vị:** Khoa Công Nghệ Thông Tin – Trường Đại học Công Thương TP.HCM (HUIT)

---

## 🧭 MỤC LỤC 14 SLIDE THUYẾT TRÌNH

* **Slide 1:** Trang bìa (Tiêu đề đề tài & Thành viên nhóm)
* **Slide 2:** 1. Tổng Quan & Lý Do Chọn Đề Tài
* **Slide 3:** 2. Công Nghệ Sử Dụng & Kiến Trúc Hệ Sinh Thái
* **Slide 4:** 3. Thiết Kế Cơ Sở Dữ Liệu (CSDL) & Sơ Đồ Quan Hệ (ERD 8 Bảng)
* **Slide 5:** 4. Sơ Đồ Use Case Tổng Quát (UML Use Case - 3 Actor)
* **Slide 6:** 5. Phân Hệ Khách Hàng (Customer / Client)
* **Slide 7:** 6. Phân Hệ Chủ Tiệm Bánh (Seller / Shop Partner)
* **Slide 8:** 7. Phân Hệ Quản Trị Viên Toàn Quyền (Admin)
* **Slide 9:** 8. Đối Chiếu 4 Yêu Cầu Mở Rộng Đạt Điểm Cộng (+1.0 Điểm)
* **Slide 10:** 9. Các Tính Năng Đặc Biệt Làm Thêm Vượt Barem (5 Tính năng nâng cao)
* **Slide 11:** 10. Kịch Bản Demo Trực Tiếp Sản Phẩm (Live Demo 4 Bước)
* **Slide 12:** 11. Bảng Phân Công Công Việc & Đánh Giá Đóng Góp Nhóm
* **Slide 13:** 12. Đánh Giá Ưu Điểm, Tồn Tại & Hướng Phát Triển
* **Slide 14:** Lời Cảm Ơn Hội Đồng & Khởi Động Phần Vấn Đáp (Q&A)

---

## 🎬 CHI TIẾT TỪNG SLIDE: NỘI DUNG, ẢNH CHỤP THỰC TẾ & LỜI THOẠI THUYẾT TRÌNH

---

### 📌 SLIDE 1: TRANG BÌA (TITLE SLIDE)
* **Thời lượng đề xuất:** 45 giây.
* **Bố cục hiển thị trên Slide PPTX:**
  * Header cơ quan: *TRƯỜNG ĐẠI HỌC CÔNG THƯƠNG TP. HỒ CHÍ MINH (HUIT) - KHOA CÔNG NGHỆ THÔNG TIN*.
  * Tiêu đề lớn: **BÁO CÁO ĐỒ ÁN HỌC PHẦN: MÃ NGUỒN MỞ**
  * Tên đề tài nổi bật: **XÂY DỰNG WEBSITE BÁN BÁNH NGỌT CAKEY**
  * Phụ đề công nghệ: *Hệ thống sàn thương mại điện tử Multi-vendor chuyên biệt ngành bánh (Laravel 11, MySQL, Blade Template, Bootstrap 5, AJAX & VietQR API)*.
  * Thông tin thực hiện: Nhóm 08 - Trưởng nhóm: Vũ Lê Anh Đức (2001230191) & Các thành viên.
* **Gợi ý ảnh chụp / Visual:** Nền xanh đen Slate-900 sang trọng, logo HUIT và biểu tượng bánh ngọt bánh kem cách điệu.
* **Lời thoại thuyết trình (Speaker Notes):**
  > *"Kính chào Thầy và các bạn! Hôm nay, nhóm 08 chúng em xin đại diện báo cáo đồ án kết thúc học phần môn học Phát triển ứng dụng Mã Nguồn Mở với đề tài: **'Xây dựng Website Bán Hàng Trực Tuyến – Sàn Bánh Ngọt Đa Cửa Hàng CAKEY trên nền tảng Laravel 11 và MySQL'**.  
  Đề tài được phát triển bởi 4 thành viên do bạn Vũ Lê Anh Đức làm trưởng nhóm cùng các bạn Nguyễn Hoàng Long, Trần Minh Quân và Lê Thị Kim Ngân. Chúng em xin phép được bắt đầu phần trình bày ngay sau đây!"*
* **Điểm kỹ thuật:** Khẳng định ngay việc sử dụng phiên bản Laravel 11 mới nhất cùng hệ sinh thái mã nguồn mở chuẩn mực.

---

### 📌 SLIDE 2: TỔNG QUAN & LÝ DO CHỌN ĐỀ TÀI
* **Thời lượng đề xuất:** 1 phút.
* **Bố cục hiển thị trên Slide PPTX:** Gồm 2 thẻ khối đối xứng (2 Cards):
  1. *Thẻ Trái: Bối Cảnh & Thực Trạng Thực Tế*
     * Ngành F&B và bánh ngọt phát triển bùng nổ, nhu cầu đặt bánh tiệc/sinh nhật online tăng vọt.
     * Các tiệm bánh truyền thống gặp khó khăn khi bán qua tin nhắn: sót đơn, nhầm tiền chuyển khoản, khó quản lý lượng tồn kho.
     * Khách hàng thiếu công cụ xem hình ảnh bánh chân thực, tìm vị bánh theo sở thích và thanh toán tự động.
  2. *Thẻ Phải: Mục Tiêu & Giải Pháp Đề Tài*
     * Lựa chọn Đề tài số 3 ("Website Bán hàng Online") trong danh sách gợi ý của Giảng viên.
     * Nâng cấp thành mô hình **Sàn Bánh Ngọt Multi-vendor** (Hỗ trợ 3 nhóm đối tượng: Khách mua, Chủ tiệm bánh, Quản trị viên).
     * Trải nghiệm hiện đại: Tìm kiếm tức thì AJAX Live Search, quét mã QR VietQR Napas 24/7 tự động và bảo mật xác thực Email OTP.
* **Gợi ý ảnh chụp từ Web:** Ảnh chụp phối cảnh một món bánh kem nổi bật trên trang chủ CAKEY kèm giá bán và nút "Thêm vào giỏ".
* **Lời thoại thuyết trình (Speaker Notes):**
  > *"Xuất phát từ thực tế thị trường ẩm thực và bánh ngọt phát triển cực kỳ năng động, nhu cầu đặt bánh kem, bánh mì, tiệc ngọt giao tận nơi của giới trẻ là rất lớn. Tuy nhiên, phần lớn các tiệm bánh vừa và nhỏ hiện nay vẫn kinh doanh phân mảnh qua Facebook hay Zalo, dẫn đến việc dễ sót đơn và sai sót khi kiểm tra số tiền khách chuyển khoản.  
  Vì vậy, nhóm đã lựa chọn Đề tài số 3 trong danh mục gợi ý của Thầy và quyết tâm nâng cấp từ một website bán hàng đơn lẻ thông thường thành **Sàn thương mại điện tử Bánh Ngọt Đa Cửa Hàng CAKEY**. Hệ thống giải quyết triệt để bài toán kết nối giữa các tiệm bánh thủ công và người tiêu dùng thông qua tìm kiếm AJAX thời gian thực và cổng thanh toán VietQR tự động hóa."*

---

### 📌 SLIDE 3: CÔNG NGHỆ SỬ DỤNG & KIẾN TRÚC HỆ SINH THÁI
* **Thời lượng đề xuất:** 1 phút 15 giây.
* **Bố cục hiển thị trên Slide PPTX:** Bố trí dạng lưới 4 khối công nghệ (4 Grid Cards):
  1. *Backend Framework:* Laravel Framework 11.x (MVC, Eloquent ORM, Custom Middleware, Form Request Validation).
  2. *Cơ Sở Dữ Liệu:* MySQL InnoDB (8 bảng chuẩn hóa, Foreign Keys ràng buộc toàn vẹn, Migration & Seeder tự động).
  3. *Frontend & UI:* Blade Template + Bootstrap 5 (Responsive Mobile, FontAwesome 6, AJAX tương tác không reload trang).
  4. *Tích Hợp Bên Ngoài (API):* VietQR API sinh mã thanh toán ngân hàng Napas 24/7, Dịch vụ Email OTP và Chuông thông báo In-App.
* **Gợi ý ảnh chụp từ Web:** Sơ đồ luồng MVC Laravel (Request -> Route -> Middleware -> Controller -> Model/DB -> Blade View).
* **Lời thoại thuyết trình (Speaker Notes):**
  > *"Để hệ thống vận hành mượt mà và bảo mật, nhóm áp dụng 100% các tiêu chuẩn mã nguồn mở chuẩn mực:  
  • Ở tầng Backend: Sử dụng Laravel 11 với mô hình MVC, khai thác Eloquent ORM để quan hệ bảng đa chiều, phân quyền chặt chẽ bằng Middleware và băm mật khẩu bằng Bcrypt.  
  • Ở tầng CSDL: Sử dụng MySQL InnoDB với 8 bảng dữ liệu quan hệ, thiết lập khóa ngoại và hỗ trợ Transaction đảm bảo không bao giờ thất thoát dữ liệu đơn hàng.  
  • Ở tầng Frontend: Sử dụng Blade Template kết hợp Bootstrap 5 theo thiết kế Mobile-First và Fetch API AJAX để nâng cao trải nghiệm người dùng.  
  • Về tích hợp mở rộng: Sử dụng cổng VietQR API tạo mã QR chuyển khoản tự động và hệ thống gửi mã OTP qua Email."*
* **Câu hỏi phản biện dự kiến của Thầy:** *"Tại sao dùng Laravel 11 mà không dùng phiên bản cũ hơn?"*
* **Câu trả lời chuẩn:** *"Dạ thưa Thầy, Laravel 11 là phiên bản Long Term Support mới nhất, có cấu trúc thư mục tinh gọn, hỗ trợ PHP 8.2+ giúp tăng tốc độ xử lý request nhanh hơn 20% và tích hợp sẵn hệ thống mã hóa bảo mật cao cấp nhất."*

---

### 📌 SLIDE 4: THIẾT KẾ CƠ SỞ DỮ LIỆU (ERD 8 BẢNG QUAN HỆ)
* **Thời lượng đề xuất:** 1 phút 30 giây.
* **Bố cục hiển thị trên Slide PPTX:** Bảng tổng hợp cấu trúc 8 thực thể chuẩn hóa:
  * `nguoidung (Users)`: PK: `MaND`. Quản lý tài khoản 3 vai trò, mật khẩu băm Bcrypt, trạng thái kích hoạt/khóa.
  * `CuaHang (Shops)`: PK: `MaCuaHang`, FK: `MaND`. Mỗi người bán quản lý 1 cửa hàng tiệm bánh.
  * `danhmuc (Categories)`: PK: `MaDanhMuc`. Phân loại bánh (Bánh kem sinh nhật, Cupcake, Bánh mì mặn, Bánh ăn kiêng).
  * `SanPham (Products)`: PK: `MaSanPham`, FK: `MaDanhMuc`, `MaCuaHang`. Lưu tên, giá, số lượng tồn, hình ảnh, trạng thái xóa mềm.
  * `GioHang (Cart)`: PK: `id`, FK: `MaNguoiDung`, `MaSanPham`. Giỏ hàng tạm thời, ràng buộc UNIQUE chống trùng món.
  * `DonHang (Orders)`: PK: `MaDon`, FK: `MaKhachHang`. Lưu địa chỉ, SĐT, PTTT (COD / VietQR), trạng thái, tổng tiền, ghi chú đối soát.
  * `ChiTietDonHang (OrderItems)`: PK: `id`, FK: `MaDon`, `MaSanPham`. Lưu số lượng mua và đơn giá lịch sử tại thời điểm chốt đơn.
  * `ThongBao (Notifications)`: PK: `id`, FK: `user_id`. Chuông thông báo trạng thái đơn hàng thời gian thực.
* **Vị trí cần chèn ảnh Web Screenshot:**
  * **[ẢNH 1]:** Ảnh chụp sơ đồ ERD trực quan (hoặc ảnh chụp bảng CSDL trong phpMyAdmin / HeidiSQL hiển thị 8 bảng `BanhNgot`).
* **Lời thoại thuyết trình (Speaker Notes):**
  > *"Về thiết kế dữ liệu, nhóm xây dựng CSDL gồm 8 bảng quan hệ liên kết chặt chẽ:  
  • Trung tâm là bảng `nguoidung` liên kết 1-1 với `CuaHang` và liên kết 1-n với `GioHang` và `DonHang`.  
  • Bảng `SanPham` nhận khóa ngoại từ cả `CuaHang` và `danhmuc`, cho phép mỗi tiệm bánh tự quản lý các danh mục bánh độc lập.  
  • Điểm nhấn đặc biệt nằm ở bảng `ChiTietDonHang`: Nhóm lưu trường `DonGia` tại thời điểm mua, giúp bảo toàn tính toàn vẹn tài chính, ngay cả khi sau này chủ tiệm có tăng hay giảm giá món bánh thì tổng tiền đơn cũ vẫn hoàn toàn chính xác.  
  • Toàn bộ khóa ngoại đều được cài đặt `ON UPDATE CASCADE` và `ON DELETE RESTRICT` để ngăn chặn việc xóa nhầm dữ liệu đang có ràng buộc."*

---

### 📌 SLIDE 5: SƠ ĐỒ USE CASE TỔNG QUÁT (3 NHÓM ACTOR)
* **Thời lượng đề xuất:** 1 phút.
* **Bố cục hiển thị trên Slide PPTX:** 3 cột đại diện cho 3 nhóm Tác nhân:
  1. *Actor 1: Khách Hàng (Customer - ROLE_NguoiMua):* Đăng ký Email OTP, Tìm kiếm AJAX Live Search, Quản lý giỏ hàng AJAX, Đặt hàng thanh toán VietQR, Theo dõi tiến độ đơn, Gửi khiếu nại, Nộp đơn mở shop.
  2. *Actor 2: Chủ Tiệm Bánh (Seller - ROLE_NguoiBan):* Quản lý thông tin tiệm bánh, CRUD Sản phẩm bánh có Upload ảnh, Xóa mềm & Khôi phục món bánh, Duyệt đơn hàng và Xác nhận nhận tiền chuyển khoản.
  3. *Actor 3: Quản Trị Viên (Admin - ROLE_Admin):* Bảng điều khiển phân tích số liệu toàn sàn, Xét duyệt hồ sơ mở tiệm bánh, Khóa/Mở khóa tài khoản vi phạm, Kiểm duyệt sản phẩm và can thiệp xử lý khiếu nại.
* **Vị trí cần chèn ảnh Web Screenshot:**
  * **[ẢNH 2]:** Sơ đồ UML Use Case đồ họa phân nhánh 3 Actor rõ ràng.
* **Lời thoại thuyết trình (Speaker Notes):**
  > *"Để đáp ứng bài toán sàn đa cửa hàng, hệ thống được thiết kế theo 3 nhóm tác nhân riêng biệt, vượt qua yêu cầu tối thiểu 2 role của Thầy:  
  • Nhóm Khách hàng tập trung vào trải nghiệm mua sắm mượt mà, tiện lợi và minh bạch.  
  • Nhóm Người bán sở hữu bộ công cụ quản lý bán hàng độc lập, tự chủ về giá cả và tồn kho.  
  • Nhóm Quản trị viên đóng vai trò trọng tài sàn, kiểm soát chất lượng các tiệm bánh tham gia và bảo vệ quyền lợi người tiêu dùng."*

---

### 📌 SLIDE 6: PHÂN HỆ KHÁCH HÀNG (CUSTOMER / CLIENT)
* **Thời lượng đề xuất:** 1 phút 30 giây.
* **Bố cục hiển thị trên Slide PPTX:** 4 thẻ tính năng nổi bật:
  1. *Tìm kiếm AJAX Live Search:* Gõ phím tới đâu danh sách bánh hiện ra tức thì không reload trang.
  2. *Phân trang chuẩn Bootstrap 5:* Cố định 8 sản phẩm/trang, tự động bảo lưu từ khóa tìm kiếm và bộ lọc danh mục.
  3. *Giỏ hàng tương tác nhanh (AJAX Cart):* Thêm món, tăng giảm số lượng mượt mà, cập nhật badge số lượng trên header.
  4. *Thanh toán quét mã VietQR Napas 24/7:* Tự động sinh mã QR với số tài khoản MBBank, số tiền chính xác và mã đơn hàng.
* **Vị trí cần chèn ảnh Web Screenshot:**
  * **[ẢNH 3 - RẤT QUAN TRỌNG]:** Chụp màn hình Trang chủ (`http://doan_banhngot.test/`) với thanh Live Search đang bung gợi ý danh sách bánh.
  * **[ẢNH 4]:** Chụp màn hình Trang danh mục sản phẩm (`/products`) hiển thị thanh phân trang Bootstrap 5 ở chân trang.
* **Lời thoại thuyết trình (Speaker Notes):**
  > *"Kính mời Thầy xem qua giao diện phân hệ Khách hàng:  
  • Đầu tiên là thanh tìm kiếm AJAX Live Search: Ngay khi khách gõ từ 'bánh kem', JavaScript ngầm gửi fetch request và đổ ngay kết quả gợi ý có hình ảnh, giá bán mà không cần bấm Enter hay load lại trang.  
  • Trang danh mục bánh được chia trang chuẩn mực 8 sản phẩm/trang bằng Bootstrap 5 Pagination, giúp trang tải cực nhanh dù có hàng trăm sản phẩm.  
  • Thao tác giỏ hàng hoàn toàn dùng AJAX, không gây giật lag giao diện.  
  • Và đặc biệt tại bước Checkout, khi khách chọn chuyển khoản, hệ thống gọi VietQR API render ngay mã QR thông minh. Khách chỉ cần mở app ngân hàng quét 1 giây là thông tin tài khoản, số tiền và nội dung đơn được điền tự động 100%."*

---

### 📌 SLIDE 7: PHÂN HỆ CHỦ TIỆM BÁNH (SELLER / SHOP PARTNER)
* **Thời lượng đề xuất:** 1 phút 15 giây.
* **Bố cục hiển thị trên Slide PPTX:** 4 tính năng quản trị cửa hàng:
  1. *Dashboard Seller:* Thống kê số lượng bánh đang bán, đơn hàng mới nhận và doanh thu trong ngày.
  2. *CRUD Sản phẩm có Upload ảnh:* Thêm món bánh mới, chọn tệp hình ảnh từ máy tính (lưu vào `public/img`), cập nhật giá và số lượng tồn.
  3. *Cơ chế Xóa mềm (Soft Delete) & Khôi phục:* Nút 'Tạm ẩn' bánh hết mùa vụ và nút 'Khôi phục' bất kỳ lúc nào mà không làm lỗi các đơn hàng cũ.
  4. *Quy trình xử lý đơn hàng:* Xem chi tiết đơn đặt tại tiệm mình, bấm nút 'Xác nhận đã nhận tiền chuyển khoản' để kích hoạt làm bánh và giao hàng.
* **Vị trí cần chèn ảnh Web Screenshot:**
  * **[ẢNH 5]:** Chụp màn hình Seller Dashboard (`/seller/products`) danh sách quản lý bánh với các nút Sửa, Xóa mềm, Khôi phục.
  * **[ẢNH 6]:** Chụp màn hình Form thêm bánh mới có ô chọn ảnh Upload file và các trường Validate.
* **Lời thoại thuyết trình (Speaker Notes):**
  > *"Đối với chủ tiệm bánh, chúng em xây dựng một không gian quản trị chuyên nghiệp:  
  • Chủ tiệm có toàn quyền CRUD món bánh của mình. Khi đăng bánh mới, form upload ảnh kiểm tra định dạng và dung lượng tối đa 5MB, tự động đổi tên tránh trùng lặp.  
  • Chúng em áp dụng kỹ thuật Xóa mềm (Soft Delete): Khi bấm xóa, món bánh chỉ chuyển trạng thái 'Tạm gỡ' trên sàn bán, nhưng dòng dữ liệu vẫn lưu trong CSDL để đảm bảo các hóa đơn cũ trong `ChiTietDonHang` không bị lỗi khóa ngoại.  
  • Chủ tiệm cũng có giao diện đối soát đơn hàng: Xem được khách đã thanh toán COD hay chuyển khoản để bấm xác nhận nhận tiền chính xác."*

---

### 📌 SLIDE 8: PHÂN HỆ QUẢN TRỊ VIÊN TOÀN QUYỀN (ADMIN)
* **Thời lượng đề xuất:** 1 phút.
* **Bố cục hiển thị trên Slide PPTX:** 4 đặc quyền tối cao của Admin:
  1. *Bảng điều khiển 3D trực quan:* Tổng quan toàn sàn về tổng số người dùng, số tiệm bánh đối tác, tổng đơn hàng và doanh số.
  2. *Xét duyệt hồ sơ mở tiệm bánh mới:* Xem thông tin người nộp đơn, 1-click 'Phê duyệt' nâng cấp quyền lên `ROLE_NguoiBan` hoặc 'Từ chối'.
  3. *Quản trị tài khoản & Khóa vi phạm:* Bộ lọc trạng thái người dùng (Đang hoạt động, Chờ duyệt, Bị khóa), nút Khóa tài khoản có hành vi gian lận.
  4. *Giám sát toàn sàn & Trọng tài khiếu nại:* Theo dõi mọi giao dịch và đứng ra xử lý tranh chấp giữa khách hàng và tiệm bánh.
* **Vị trí cần chèn ảnh Web Screenshot:**
  * **[ẢNH 7]:** Chụp màn hình Admin Dashboard (`/admin/sellers/pending`) với danh sách tiệm bánh đang chờ phê duyệt.
  * **[ẢNH 8]:** Chụp màn hình Quản lý người dùng (`/admin/users`) với các nút chuyển đổi trạng thái Khóa / Mở khóa.
* **Lời thoại thuyết trình (Speaker Notes):**
  > *"Tại phân hệ Quản trị viên Admin, hệ thống trao công cụ kiểm soát toàn diện:  
  • Bảng điều khiển phân tích trực quan toàn bộ hoạt động kinh doanh trên sàn.  
  • Admin có thể phê duyệt tiệm bánh mới chỉ với 1 cú click chuột. Khi duyệt, hệ thống tự động đổi `QuyenHan` của người dùng thành `ROLE_NguoiBan` và kích hoạt gian hàng ngay lập tức.  
  • Admin có thể khóa tài khoản vi phạm để ngăn chặn spam, đồng thời theo dõi các đơn hàng bị khiếu nại để đảm bảo uy tín cho toàn sàn."*

---

### 📌 SLIDE 9: ĐỐI CHIẾU 4 YÊU CẦU MỞ RỘNG ĐẠT ĐIỂM CỘNG (+1.0 ĐIỂM)
* **Thời lượng đề xuất:** 1 phút 15 giây.
* **Bố cục hiển thị trên Slide PPTX:** Bảng đối chiếu 4/4 tiêu chí điểm cộng tuyệt đối:
  * **Tiêu chí 1: Upload file an toàn (+0.25):** Upload ảnh bánh vào `public/img`, kiểm tra MIME Type (`jpeg, png, jpg, webp`), dung lượng max 5MB, sinh tên file duy nhất theo timestamp.
  * **Tiêu chí 2: Sử dụng AJAX tương tác không reload (+0.25):** Tích hợp ở 3 nơi vượt chuẩn: AJAX Live Search, Thao tác giỏ hàng popup và Chuông thông báo đếm số lượng tin mới.
  * **Tiêu chí 3: Tích hợp API bên ngoài (+0.25):** Cổng VietQR API tự động sinh ảnh QR Napas 24/7 theo số tài khoản MBBank `0867441036`, điền sẵn số tiền hóa đơn và mã đơn hàng.
  * **Tiêu chí 4: Giao diện Responsive tốt trên Mobile (+0.25):** Thiết kế Mobile-First bằng Bootstrap 5 Grid, Offcanvas Navbar, co giãn mượt mà trên iPhone, iPad và Máy tính.
* **Vị trí cần chèn ảnh Web Screenshot:**
  * **[ẢNH 9 - ĐIỂM CỘNG]:** Chụp màn hình popup thanh toán có ảnh mã VietQR MBBank tự động sinh ra.
  * **[ẢNH 10 - ĐIỂM CỘNG]:** Chụp màn hình giao diện web Cakey co về kích thước Mobile (iPhone 12/14) hiển thị đẹp mắt.
* **Lời thoại thuyết trình (Speaker Notes):**
  > *"Kính thưa Thầy, đối chiếu với 4 tiêu chuẩn cộng điểm tối đa 1.0 điểm trong quy chế đánh giá của bộ môn, nhóm tự hào đã hoàn thiện xuất sắc 100% cả 4 tiêu chuẩn:  
  1. Upload file an toàn với xác thực đuôi file và giới hạn dung lượng.  
  2. Ứng dụng AJAX không chỉ ở 1 chức năng mà ở cả 3 khu vực: Tìm kiếm, Giỏ hàng và Thông báo.  
  3. Tích hợp API bên ngoài VietQR chuẩn ngân hàng quốc gia.  
  4. Giao diện Responsive thích ứng hoàn hảo trên mọi thiết bị di động."*

---

### 📌 SLIDE 10: 5 TÍNH NĂNG ĐẶC BIỆT LÀM THÊM VƯỢT BAREM
* **Thời lượng đề xuất:** 1 phút.
* **Bố cục hiển thị trên Slide PPTX:** 5 khối tính năng nâng cao:
  1. *Kiến trúc Multi-vendor 3 cấp bậc:* Quy trình đăng ký mở shop -> Admin phê duyệt -> Nâng quyền thành Seller.
  2. *Bảo mật Email OTP 2 bước (2FA):* Mã OTP 6 chữ số gửi qua mail khi Đăng ký mới và Quên mật khẩu.
  3. *Chuông thông báo In-App Real-time:* Thông báo nổi khi có đơn mới, khi đơn được giao và khi tiệm xác nhận tiền.
  4. *Quy trình đối soát 2 chiều & Cơ chế Khiếu nại:* Bảo vệ khách hàng khi chuyển khoản ngân hàng nếu có sai sót.
  5. *Cơ chế Xóa mềm & Khôi phục (Soft Delete):* Bảo toàn dữ liệu lịch sử kế toán, hóa đơn.
* **Lời thoại thuyết trình (Speaker Notes):**
  > *"Ngoài các yêu cầu trong đề cương, nhóm đã đầu tư nghiên cứu và hoàn thiện thêm 5 tính năng nâng cấp thực tế: Mô hình đa người bán Multi-vendor bài bản, bảo mật 2 bước bằng mã Email OTP, chuông thông báo In-App tức thời, quy trình giải quyết khiếu nại đơn hàng chuyển khoản và kỹ thuật Xóa mềm bảo toàn dữ liệu tài chính."*

---

### 📌 SLIDE 11: KỊCH BẢN DEMO TRỰC TIẾP TRÊN MÁY (LIVE DEMO)
* **Thời lượng đề xuất:** 2 phút 30 giây (Thuyết minh kèm thao tác trên trình duyệt).
* **Bố cục hiển thị trên Slide PPTX:** 4 bước thao tác khép kín toàn trình:
  * **Bước 1:** Khách hàng (`user@cakey.local`) tìm bánh kem dâu tây bằng Live Search -> Thêm vào giỏ -> Đặt hàng chọn VietQR -> Quét mã thanh toán.
  * **Bước 2:** Khách hàng nộp đơn xin mở tiệm bánh mới tên 'HUIT Bakery' tại quận Tân Phú.
  * **Bước 3:** Đăng nhập Admin (`admin@cakey.local`) -> Vào duyệt tiệm bánh 'HUIT Bakery' -> Quyền hạn tự động nâng lên `ROLE_NguoiBan`.
  * **Bước 4:** Đăng nhập Seller tiệm bánh -> Đăng món bánh mới có Upload ảnh -> Vào đơn hàng bấm 'Xác nhận đã nhận tiền chuyển khoản' cho đơn ở Bước 1.
* **Lời thoại thuyết trình (Speaker Notes):**
  > *"Sau đây nhóm xin phép được Demo trực tiếp sản phẩm thực tế trên máy theo quy trình 4 bước khép kín:  
  Đầu tiên, em đóng vai Khách hàng trải nghiệm tìm kiếm Live Search và đặt hàng quét mã VietQR.  
  Tiếp theo, khách hàng nộp hồ sơ xin mở tiệm bánh mới.  
  Sau đó, em đăng nhập tài khoản Admin vào duyệt tiệm bánh.  
  Và cuối cùng, em đăng nhập tài khoản Seller vừa được cấp quyền để đăng bánh mới có upload ảnh và xác nhận thanh toán cho đơn hàng ban đầu."*

---

### 📌 SLIDE 12: BẢNG PHÂN CÔNG CÔNG VIỆC NHÓM
* **Thời lượng đề xuất:** 45 giây.
* **Bố cục hiển thị trên Slide PPTX:** Bảng phân chia trách nhiệm 4 thành viên (Chuẩn 3-5 sinh viên, 100% hoàn thành).
* **Lời thoại thuyết trình (Speaker Notes):**
  > *"Nhóm gồm 4 thành viên phối hợp chặt chẽ. Trưởng nhóm Vũ Lê Anh Đức chịu trách nhiệm kiến trúc tổng thể, bảo mật phân quyền và tích hợp API. Các bạn Long, Quân và Ngân phụ trách CSDL, Frontend AJAX và kiểm thử chức năng. Cả 4 thành viên đều hoàn thành 100% khối lượng công việc được giao."*

---

### 📌 SLIDE 13: ĐÁNH GIÁ HỆ THỐNG & HƯỚNG PHÁT TRIỂN
* **Thời lượng đề xuất:** 45 giây.
* **Bố cục hiển thị trên Slide PPTX:**
  * *Ưu điểm:* Giao diện đẹp, mượt mà, phân quyền chặt chẽ, thanh toán VietQR tiện lợi, CSDL chuẩn hóa không dư thừa.
  * *Hướng phát triển:* Tích hợp Webhook tự động nhận thông báo biến động số dư ngân hàng theo thời gian thực và xây dựng hệ thống đánh giá sao (Review 5 sao kèm bình luận có ảnh).
* **Lời thoại thuyết trình (Speaker Notes):**
  > *"Hệ thống đã đạt được độ hoàn thiện cao, chạy ổn định và tối ưu trải nghiệm người dùng. Hướng phát triển trong tương lai, nhóm sẽ tích hợp thêm hệ thống Webhook ngân hàng tự động cập nhật số dư và module đánh giá bình luận sao cho từng món bánh."*

---

### 📌 SLIDE 14: LỜI CẢM ƠN & PHẦN VẤN ĐÁP (Q&A)
* **Thời lượng đề xuất:** 30 giây.
* **Bố cục hiển thị trên Slide PPTX:** Banner cảm ơn Hội đồng Giảng viên & Lời mời đặt câu hỏi phản biện.
* **Lời thoại thuyết trình (Speaker Notes):**
  > *"Nhóm chúng em xin chân thành cảm ơn Thầy và các bạn đã chú ý lắng nghe bài báo cáo! Nhóm chúng em rất mong nhận được những câu hỏi phản biện và đóng góp quý báu từ Thầy để hoàn thiện đề tài hơn nữa ạ!"*

---

## 📸 HƯỚNG DẪN MỞ WEB ĐỂ CHỤP VÀ CHÈN ẢNH VÀO SLIDE POWERPOINT

### ❓ Trả lời câu hỏi: *"Có cần mở web lên để chụp ảnh không?"*
**👉 CÂU TRẢ LỜI LÀ: RẤT NÊN MỞ WEB ĐỂ CHỤP ẢNH!**

**Lý do:**
1. Khi có ảnh chụp màn hình giao diện thực tế chèn vào Slide 6, 7, 8, 9, bài thuyết trình PowerPoint sẽ đẹp hơn gấp nhiều lần, chứng minh 100% nhóm đã code thật, chạy thật trên máy, không hề dùng ảnh mạng hay ảnh giả lập.
2. Thầy cô chấm điểm cực kỳ thích các slide có hình ảnh demo trực tiếp từ project.

### 📋 Danh sách 6 ảnh cần chụp khi mở Web:
1. **Ảnh 1 (Trang chủ & Live Search):** Mở `http://localhost:8000` (hoặc `http://doan_banhngot.test`), gõ chữ `bánh` vào ô tìm kiếm để menu gợi ý xổ xuống -> Chụp màn hình (Chèn vào Slide 6).
2. **Ảnh 2 (Phân trang sản phẩm):** Bấm vào mục "Sản phẩm", cuộn xuống chân trang để thấy thanh số trang 1, 2, 3... của Bootstrap 5 -> Chụp màn hình (Chèn vào Slide 6).
3. **Ảnh 3 (Thanh toán VietQR):** Cho 1 bánh vào giỏ, bấm đặt hàng, chọn phương thức "Chuyển khoản VietQR" -> Chụp màn hình mã QR ngân hàng MBBank hiện lên (Chèn vào Slide 9).
4. **Ảnh 4 (Seller Dashboard & Đăng bánh):** Đăng nhập `seller@cakey.local` / `123456`, vào trang Quản lý sản phẩm và Form thêm bánh -> Chụp màn hình (Chèn vào Slide 7).
5. **Ảnh 5 (Admin duyệt shop):** Đăng nhập `admin@cakey.local` / `123456`, vào trang Danh sách yêu cầu mở tiệm -> Chụp màn hình (Chèn vào Slide 8).
6. **Ảnh 6 (Responsive Mobile):** Nhấn phím `F12` trên trình duyệt, bấm biểu tượng điện thoại (Toggle device toolbar) chọn iPhone 12/14 -> Chụp màn hình giao diện mobile (Chèn vào Slide 9).

*(Ngay khi bạn mở web hoặc gửi các ảnh chụp này, tôi có thể tự động chạy script Python để chèn thẳng ảnh vào đúng tọa độ của các Slide trong file `Slide_BaoCao_MaNguonMo_Cakey.pptx`!)*
"""

# Ghi vao cac file dich
paths = [
    r"C:\laragon\www\doan_banhngot\slide bao cao do an cakey.md",
    r"C:\laragon\www\doan_banhngot\Slide_BaoCao_DoAn_Cakey.md",
    r"D:\Doan_BigData\slide bao cao do an cakey.md",
    r"D:\Doan_BigData\Slide_BaoCao_DoAn_Cakey.md"
]

for p in paths:
    try:
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8") as f:
            f.write(md_content)
        print(f"[OK] Da tao thanh cong: {p} ({len(md_content)} ky tu)")
    except Exception as e:
        print(f"[ERR] Loi ghi {p}: {e}")
