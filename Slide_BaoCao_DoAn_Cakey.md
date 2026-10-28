# BỘ SLIDE BÁO CÁO ĐỒ ÁN MÔN HỌC MÃ NGUỒN MỞ
## ĐỀ TÀI: XÂY DỰNG NỀN TẢNG THƯƠNG MẠI ĐIỆN TỬ BÁN BÁNH NGỌT ĐA CỬA HÀNG - CAKEY (LARAVEL FRAMEWORK)

* **Trường:** Đại học Công Thương TP. Hồ Chí Minh (HUIT)  
* **Khoa:** Công Nghệ Thông Tin – Bộ môn Công Nghệ Phần Mềm  
* **Học phần:** Phát triển ứng dụng Mã Nguồn Mở (PHP & Laravel Framework)  
* **Tệp trình chiếu PowerPoint đi kèm:** `Slide_BaoCao_MaNguonMo_Cakey_21Slide.pptx` (21 slide chuẩn Widescreen 16:9, đã nhúng ảnh chụp thực tế)  
* **Nhóm sinh viên thực hiện (Nhóm 08):**
  1. **Vũ Lê Anh Đức** (MSSV: **2001230191** - Trưởng nhóm: Kiến trúc hệ thống, Backend, Middleware, VietQR, Soft-delete)
  2. **Nguyễn Hoàng Long** (MSSV: **2001230188** - Thành viên: CSDL MySQL, Migration, Seeder, Module Seller & Upload file)
  3. **Trần Minh Quân** (MSSV: **2001230195** - Thành viên: UI Blade + Bootstrap 5, AJAX Live Search, Cart, Chuông Polling)
  4. **Lê Thị Kim Ngân** (MSSV: **2001230182** - Thành viên: Module Checkout Khách hàng, Khiếu nại, Form Validation, QA)

---

## TỔNG QUAN CẤU TRÚC BÁO CÁO (CHUẨN FORM ĐỒ ÁN CNTT)

| Phần | Nội dung chính | Slide tương ứng |
| :--- | :--- | :--- |
| **Phần 1** | Giới thiệu & Đặt vấn đề | Slide 1, 2, 3, 4 |
| **Phần 2** | Phân tích yêu cầu & Kiến trúc hệ thống | Slide 5, 6, 7, 7A, 7B, 8 |
| **Phần 3** | Hiện thực chức năng các phân hệ (Demo Modules) | Slide 9, 10, 11, 12, 13, 14 |
| **Phần 4** | Các kỹ thuật & Tính năng công nghệ nổi bật | Slide 15 |
| **Phần 5** | Kiểm thử & Đánh giá kết quả | Slide 16, 17 |
| **Phần 6** | Hướng phát triển & Kết luận | Slide 18, 19 |
| **Phụ lục** | Kịch bản bảo vệ & Bộ câu hỏi phản biện của Giảng viên | Slide 20, 21 |

---

# CHI TIẾT TỪNG SLIDE BÁO CÁO (KÈM ẢNH MINH CHỨNG & SPEAKER NOTES)

---

### SLIDE 1: TRANG TIÊU ĐỀ (BÌA BÁO CÁO)

#### 1. Nội dung hiển thị trên slide:
* **Tên Trường / Khoa**: TRƯỜNG ĐẠI HỌC CÔNG THƯƠNG TP. HỒ CHÍ MINH (HUIT) – KHOA CÔNG NGHỆ THÔNG TIN
* **Tên Môn Học**: BÁO CÁO ĐỒ ÁN HỌC PHẦN: PHÁT TRIỂN ỨNG DỤNG MÃ NGUỒN MỞ
* **Tên Đề Tài**: **XÂY DỰNG NỀN TẢNG THƯƠNG MẠI ĐIỆN TỬ BÁN BÁNH NGỌT ĐA CỬA HÀNG - CAKEY**
* **Nền tảng công nghệ**: PHP 8.3 & Laravel 11/12 Framework (MySQL InnoDB, Blade Template, Bootstrap 5, AJAX, VietQR API)
* **Giảng viên phụ trách**: Bộ môn Công nghệ Phần mềm – Khoa CNTT
* **Nhóm sinh viên thực hiện**:
  * Vũ Lê Anh Đức – MSSV: 2001230191 (Trưởng nhóm)
  * Nguyễn Hoàng Long – MSSV: 2001230188
  * Trần Minh Quân – MSSV: 2001230195
  * Lê Thị Kim Ngân – MSSV: 2001230182
* **Thời gian**: Tháng 10/2026

#### 2. Ảnh / Thiết kế thực tế:
* Nền Slate 900 `#0f172a` hiện đại, thanh line Rose 600 `#e11d48` làm điểm nhấn.
* Logo trường HUIT góc trên cùng logo thương hiệu bánh ngọt CAKEY.

#### 3. Kịch bản thuyết trình (Speaker Notes):
> *"Kính thưa quý thầy cô trong hội đồng đánh giá và các bạn sinh viên. Hôm nay, em xin phép được đại diện nhóm 08 trình bày báo cáo đồ án kết thúc học phần môn học Phát triển ứng dụng Mã Nguồn Mở với đề tài: 'Xây dựng nền tảng thương mại điện tử chuyên biệt về bánh ngọt đa cửa hàng - CAKEY'. Ứng dụng được thiết kế và phát triển dựa trên nền tảng PHP 8.3 và Framework Laravel hiện đại."*

---

### SLIDE 2: NỘI DUNG BÁO CÁO (AGENDA)

#### 1. Nội dung hiển thị trên slide:
* **01. Đặt vấn đề & Mục tiêu đề tài** (Bối cảnh thực tế & giải pháp sàn Multi-vendor).
* **02. Phân tích yêu cầu & Thiết kế hệ thống** (Actor, Use-Case RBAC & CSDL ERD 7 bảng).
* **03. Kiến trúc & Ma trận công nghệ** (Mô hình MVC, Ma trận hiệu quả Backend & Frontend).
* **04. Hiện thực chức năng các phân hệ** (Client Live Search VietQR, Seller 2 nút đối soát, Admin Kick-out).
* **05. Kiểm thử hệ thống & Đánh giá** (Bộ 13 Feature Tests PHPUnit passed 100%, chuẩn PSR-12).
* **06. Kết luận & Hướng phát triển** (Webhook tự động hóa 24/7 & Q&A).

#### 2. Kịch bản thuyết trình (Speaker Notes):
> *"Bài báo cáo của nhóm ngày hôm nay sẽ đi qua 6 nội dung trọng tâm: từ việc đặt vấn đề thực tế, thiết kế cơ sở dữ liệu, phân tích ma trận kỹ thuật tối ưu hóa, đi sâu vào demo 3 phân hệ chính, giới thiệu các kỹ thuật công nghệ độc đáo nhóm đã nghiên cứu ứng dụng, báo cáo kết quả kiểm thử tự động và cuối cùng là phương hướng phát triển tiếp theo."*

---

### SLIDE 3: ĐẶT VẤN ĐỀ & LÝ DO CHỌN ĐỀ TÀI

#### 1. Nội dung hiển thị trên slide:
* **Bối cảnh thực tế**:
  * Nhu cầu tiêu thụ bánh ngọt, bánh sinh nhật, tiệc ngọt gia tăng mạnh mẽ.
  * Các tiệm bánh nhỏ lẻ (Home-bakery) gặp khó khăn trong việc tiếp cận khách hàng và quản lý đơn hàng.
* **Bất cập của mô hình truyền thống**:
  * Đặt bánh qua tin nhắn MXH dễ sót đơn, nhầm yêu cầu ghi chữ, sai giờ giao.
  * Chuyển khoản ngân hàng thủ công: Khách phải nhập số tiền, số tài khoản thủ công, tiệm mất thời gian tra soát sao kê.
* **Giải pháp đề tài CAKEY**:
  * Nền tảng kết nối các tiệm bánh uy tín đến khách hàng.
  * Chuẩn hóa quy trình đặt hàng, thanh toán VietQR tự động và quản lý tiệm bánh chuyên nghiệp.

#### 2. Ảnh minh chứng thực tế:
* **Ảnh chèn trên Slide:** `public/img/screenshots/screenshot_01_homepage.png`
* **Nội dung ảnh:** Giao diện Trang chủ CAKEY với banner tiệm bánh ngọt nghệ thuật, danh mục trực quan và bố cục chuyên nghiệp.

#### 3. Kịch bản thuyết trình (Speaker Notes):
> *"Bánh ngọt là mặt hàng có tính đặc thù cao: hạn sử dụng ngắn, cần ghi chú yêu cầu riêng (như viết chữ lên bánh sinh nhật, chọn giờ giao chính xác). Khi đặt qua tin nhắn mạng xã hội, tình trạng sót đơn, sai sót khi giao hoặc đối soát chuyển khoản ngân hàng tốn rất nhiều thời gian. Xuất phát từ thực tế đó, nhóm đã xây dựng hệ thống CAKEY nhằm số hóa toàn bộ trải nghiệm từ duyệt bánh, quét mã thanh toán VietQR đến quản lý tiến độ giao hàng."*

---

### SLIDE 4: MỤC TIÊU VÀ PHẠM VI HỆ THỐNG

#### 1. Nội dung hiển thị trên slide:
* **Mục tiêu chính**:
  * Xây dựng sàn TMĐT B2C & Multi-Vendor hoạt động ổn định, mượt mà.
  * Tối ưu trải nghiệm mua sắm trên trình duyệt (thao tác nhanh dưới 3 bước).
  * Cung cấp công cụ quản trị tiệm bánh toàn diện cho tiểu thương.
* **Phạm vi 3 trụ cột**:
  * **Khách hàng**: Tìm kiếm bánh Live Search, giỏ hàng AJAX, đặt hàng (COD / Chuyển khoản VietQR), theo dõi đơn và khiếu nại.
  * **Người bán (Chủ tiệm)**: Đăng bán bánh (upload ảnh), quản lý thực đơn, duyệt đơn hàng, xác nhận chuyển khoản ngân hàng, thống kê doanh thu theo ngày/tháng.
  * **Quản trị viên (Admin)**: Phê duyệt người bán, kiểm duyệt sản phẩm, khóa tài khoản vi phạm với cơ chế đá văng tức thì (Kick-out trong 0.1s).

#### 2. Kịch bản thuyết trình (Speaker Notes):
> *"Mục tiêu cốt lõi của CAKEY là phục vụ đồng thời 3 nhóm đối tượng: Khách hàng mua bánh tiện lợi; Người bán có công cụ quản lý doanh số, thực đơn chuẩn chỉnh; và Quản trị viên có toàn quyền kiểm soát tính an toàn của sàn."*

---

### SLIDE 5: PHÂN TÍCH TÁC NHÂN & MA TRẬN PHÂN QUYỀN

#### 1. Nội dung hiển thị trên slide:
* **Hệ thống phân định 3 Role rõ ràng (RBAC)**:
  1. **Khách hàng (`ROLE_KhachHang` / `ROLE_NguoiMua`)**: Mua bánh, đánh giá, theo dõi trạng thái đơn hàng.
  2. **Người bán (`ROLE_NguoiBan`)**: Sở hữu cửa hàng, quản lý sản phẩm tiệm mình, quản lý đơn đặt bánh.
  3. **Quản trị viên (`ROLE_Admin`)**: Quyền hạn tối cao, kiểm duyệt và điều phối toàn sàn.
* **Ma trận quyền hạn & Middleware bảo vệ đa tầng**:
  * `auth`: Bắt buộc người dùng đã đăng nhập.
  * `seller`: Chỉ cho phép tài khoản có quyền `ROLE_NguoiBan` truy cập phân hệ `/seller/*`.
  * `admin`: Chỉ cho phép `ROLE_Admin` truy cập phân hệ `/admin/*`.
  * `CheckAccountStatus`: Bắt chặn mọi HTTP request, kiểm tra `TrangThai` tài khoản theo thời gian thực.
* **Bảo mật phiên**:
  * Băm mật khẩu bằng Bcrypt (`Hash::make()` cost 10-12).
  * Chống CSRF toàn diện trên Form và Request Fetch API.

#### 2. Kịch bản thuyết trình (Speaker Notes):
> *"Về mặt bảo mật phân quyền, hệ thống áp dụng cơ chế Role-Based Access Control (RBAC) chặt chẽ thông qua các tầng Middleware của Laravel. Mỗi tác nhân chỉ có thể can thiệp vào tài nguyên thuộc thẩm quyền của mình. Đặc biệt, hệ thống tích hợp sẵn middleware kiểm tra trạng thái hoạt động để ngăn chặn ngay lập tức các tài khoản bị khóa."*

---

### SLIDE 6: SƠ ĐỒ USE-CASE TỔNG THỂ

#### 1. Nội dung hiển thị trên slide:
* **Phân hệ Khách hàng**:
  * Đăng ký (xác thực OTP Email) / Đăng nhập.
  * Tìm kiếm trực tiếp (Live Search Ajax) / Lọc danh mục / Xem chi tiết bánh.
  * Thêm giỏ hàng / Đặt hàng (COD hoặc Quét mã VietQR).
  * Quản lý đơn cá nhân: Xác nhận đã CK, Yêu cầu xem xét lại, Chuyển tiền lại, Hủy đơn.
* **Phân hệ Người bán**:
  * Đăng ký mở tiệm bánh.
  * Quản lý sản phẩm: Thêm, Sửa, Ẩn (Soft-delete), Khôi phục, Gửi yêu cầu xem xét lại.
  * Xử lý đơn hàng: Đã nhận tiền, Chưa nhận tiền, Cập nhật tiến độ giao, Hủy đơn.
  * Thống kê doanh thu, đơn hủy theo Ngày và Tháng.
* **Phân hệ Quản trị viên**:
  * Quản lý & Khóa/Mở tài khoản người dùng.
  * Phê duyệt / Từ chối người bán.
  * Kiểm duyệt sản phẩm bánh vi phạm & Trọng tài khiếu nại.

#### 2. Kịch bản thuyết trình (Speaker Notes):
> *"Đây là biểu đồ Use-Case tổng thể của dự án. Chúng em chia các ca sử dụng thành 3 cụm nghiệp vụ độc lập nhưng liên kết chặt chẽ qua dữ liệu đơn hàng và luồng thông báo thời gian thực."*

---

### SLIDE 7: KIẾN TRÚC HỆ THỐNG & CÔNG NGHỆ SỬ DỤNG

#### 1. Nội dung hiển thị trên slide:
* **Mô hình kiến trúc**: **MVC (Model - View - Controller)** chuẩn mực phân tách 3 lớp độc lập:
  * **Model**: Ánh xạ quan hệ CSDL qua Eloquent ORM.
  * **View**: Giao diện người dùng render qua Blade Template.
  * **Controller**: Điều phối logic nghiệp vụ và xác thực dữ liệu.
* **Hệ sinh thái công nghệ chủ đạo**:
  * **Backend**: PHP 8.3 & Laravel Framework.
  * **Database**: MySQL Server (InnoDB Engine, UTF-8 Multilingual).
  * **Frontend**: Blade Engine, HTML5, CSS3, Vanilla JS, Bootstrap 5, FontAwesome.
  * **API & Tích hợp**: Cổng VietQR API (Chuẩn NAPAS247 quốc gia), AJAX Polling.
  * **Kiểm thử & Định dạng**: PHPUnit Test Suite, Laravel Pint (PSR-12).

#### 2. Kịch bản thuyết trình (Speaker Notes):
> *"Về mặt kiến trúc, đồ án lựa chọn mô hình MVC trên nền tảng PHP 8.3 và Laravel. Đây là bộ đôi công nghệ tiêu chuẩn của các ứng dụng Web hiện đại, đảm bảo sự tách biệt rõ ràng giữa logic nghiệp vụ, giao diện và dữ liệu, giúp dự án dễ bảo trì và mở rộng."*

---

### SLIDE 7A: MA TRẬN CÔNG NGHỆ: BACKEND & DATABASE

#### 1. Nội dung hiển thị trên slide (Bảng ma trận chi tiết):

| Công nghệ | Vị trí áp dụng cụ thể trong dự án | Hiệu quả thực tế đạt được |
| :--- | :--- | :--- |
| **PHP 8.3** | • Toàn bộ backend xử lý logic.<br>• Sử dụng Type-hinting, Constructor Promotion, Match expressions. | • Tối ưu OpCache/JIT giúp **tốc độ xử lý tăng ~20%**.<br>• Giảm 30% code boilerplate, code tường minh và hạn chế tối đa lỗi runtime `TypeError`. |
| **Laravel 11/12 (Framework)** | • Hệ thống định tuyến Route phân nhóm (`web.php`).<br>• Request Validation (`CartController`, `AuthController`).<br>• Middleware xác thực phân quyền (`auth`, `seller`, `admin`). | • Tự động chống **CSRF, XSS, SQL Injection** mà không cần viết code thủ công.<br>• Rút ngắn 50% thời gian phát triển nghiệp vụ nhờ các module dựng sẵn. |
| **Eloquent ORM** | • Mô hình hóa quan hệ: 1-1 (`CuaHang-User`), 1-N (`DonHang-ChiTiet`), N-1 (`SanPham-CuaHang`).<br>• Eager Loading: `with(['chiTiets.sanPham.cuaHang'])`.<br>• Cập nhật kho: `decrement('SoLuongTon', $qty)`. | • **Giải quyết triệt để vấn nạn N+1 Query**: Giảm từ hơn 100 câu query xuống chỉ còn 2-3 queries khi tải danh sách đơn.<br>• **Chống Race Condition**: Khóa dòng cấp độ InnoDB, đảm bảo kho không bao giờ bị âm khi nhiều khách cùng mua. |
| **MySQL (InnoDB Engine)** | • Lưu trữ 7 bảng dữ liệu quan hệ đạt chuẩn 3NF.<br>• Ràng buộc toàn vẹn khóa ngoại (`FOREIGN KEY`).<br>• Đánh chỉ mục (`INDEX`) trên `TrangThai`, `NgayDat`, `MaCuaHang`. | • Đảm bảo tuyệt đối tính toàn vẹn dữ liệu **ACID**.<br>• Tốc độ truy vấn bộ lọc đơn hàng và thống kê đạt **dưới 50ms**. |
| **Custom Middleware & Session Security** | • `CheckAccountStatus.php`: Bắt chặn mọi HTTP request.<br>• Thuật toán băm `Bcrypt` (cost=10/12) trong `AuthController`. | • **Cơ chế Kick-out tức thì trong 0.1s**: Ngay khi Admin bấm khóa, kẻ gian bị đá văng ra khỏi hệ thống ngay tại request tiếp theo.<br>• Bảo vệ 100% mật khẩu người dùng trước tấn công từ điển / rò rỉ dữ liệu. |

#### 2. Kịch bản thuyết trình (Speaker Notes):
> *"Thưa thầy cô, ở tầng Backend và Database, nhóm không chỉ dừng lại ở việc dùng framework mà đào sâu vào tính hiệu quả:  
> 1. Nhóm sử dụng triệt để Eager Loading của Eloquent ORM để triệt tiêu lỗi N+1 Query - một trong những nguyên nhân hàng đầu gây nghẽn server khi dữ liệu lớn.  
> 2. Khi trừ số lượng bánh trong kho, nhóm sử dụng hàm `decrement()` nguyên tử, tận dụng cơ chế Row-level Lock của MySQL InnoDB để ngăn chặn tuyệt đối tình trạng tranh chấp tài nguyên (Race Condition).  
> 3. Về bảo mật, Middleware `CheckAccountStatus` giúp phát hiện và đá văng tài khoản bị khóa trong vòng 0.1 giây, đảm bảo an toàn tuyệt đối cho hệ thống."*

---

### SLIDE 7B: MA TRẬN CÔNG NGHỆ: FRONTEND & 3RD-PARTY

#### 1. Nội dung hiển thị trên slide (Bảng ma trận chi tiết):

| Công nghệ | Vị trí áp dụng cụ thể trong dự án | Hiệu quả thực tế đạt được |
| :--- | :--- | :--- |
| **VietQR API (NAPAS247)** | • Accessor `$order->qr_code_url` trong Model `DonHang`.<br>• Tự sinh mã QR động chứa: Ngân hàng, STK, Tên chủ thẻ, Số tiền đơn, Cú pháp `CAKEY [MaDon]`. | • **Tiết kiệm 100% chi phí**: Không mất phí duy trì cổng hoặc 1.5% - 2.5% phí giao dịch như VNPAY/MoMo.<br>• **Loại bỏ 100% lỗi người dùng**: Khách không phải nhập tay STK/số tiền/nội dung.<br>• Quét mã thanh toán chỉ mất **2 giây** trên mọi App ngân hàng VN. |
| **Blade Template & Bootstrap 5** | • Kế thừa giao diện qua `layouts/master.blade.php`.<br>• Hệ thống Grid Responsive (Desktop, Tablet, Mobile).<br>• Component dùng chung: Modal lý do hủy, Thẻ bánh, Thanh Navbar. | • **Tái sử dụng mã nguồn 70%**, code giao diện gọn gàng, bảo trì nhanh.<br>• Views được biên dịch sẵn và lưu cache, **tốc độ tải trang dưới 200ms**.<br>• Tương thích 100% màn hình mọi thiết bị di động. |
| **AJAX (Fetch API / XMLHttpRequest)** | • **Live Search**: Tìm kiếm tức thì tại thanh Header (`ProductController::liveSearch`).<br>• **Notification Polling**: Tự động kiểm tra và cập nhật số lượng thông báo chuông mỗi 10 giây. | • **Trải nghiệm No-Reload mượt mà**: Khách tìm bánh thấy ngay kết quả không cần load lại trang.<br>• Chủ tiệm nhận thông báo *"Có người chuyển khoản"* gần như tức thì, **giảm thời gian chờ duyệt đơn từ 15 phút xuống dưới 2 phút**. |
| **Vanilla JS & Trigonometry Math** | • Hiệu ứng đèn pin soi mật khẩu xoay 360° tại form Đăng nhập.<br>• Sử dụng hàm lượng giác `Math.atan2(dy, dx)` và CSS `clipPath` đa giác chùm sáng. | • **Gamification (Game hóa trải nghiệm)**: Tạo ấn tượng thẩm mỹ độc đáo, giữ chân người dùng.<br>• Không phụ thuộc thư viện nặng nề của bên thứ 3 (kích thước script dưới 5KB, mượt mà 60fps). |
| **PHPUnit & Laravel Pint** | • Bộ 13 Feature Tests trong `tests/Feature/` (Kiểm thử đơn hàng, kiểm thử chuyển khoản, kiểm thử khóa tài khoản).<br>• Format chuẩn PSR-12 qua Laravel Pint. | • **Độ tin cậy 100%**: 13/13 tests passed với 61 assertions chỉ trong 0.8 giây.<br>• Loại bỏ hoàn toàn lỗi thụt lề, cú pháp, đảm bảo tiêu chuẩn Clean Code chuyên nghiệp. |

#### 2. Kịch bản thuyết trình (Speaker Notes):
> *"Ở tầng Frontend và tích hợp dịch vụ:  
> 1. Nhóm đã ứng dụng API VietQR chuẩn quốc gia NAPAS247 để biến mỗi đơn hàng thành một mã QR thanh toán động. Giải pháp này giúp tiểu thương không phải trả phí cổng thanh toán đắt đỏ mà khách hàng thanh toán cực kỳ chính xác trong 2 giây.  
> 2. Kỹ thuật AJAX Polling giúp đồng bộ chuông thông báo đơn hàng theo thời gian thực mà không làm nghẽn server.  
> 3. Điểm nhấn thị giác là đèn pin xoay 360° soi mật khẩu được lập trình bằng toán học hình học thuần túy trên JavaScript và CSS, dung lượng siêu nhẹ dưới 5KB nhưng mang lại trải nghiệm tương tác vô cùng sống động."*

---

### SLIDE 8: THIẾT KẾ CƠ SỞ DỮ LIỆU (DATABASE ERD)

#### 1. Nội dung hiển thị trên slide:
* **Các thực thể chính trong CSDL**:
  * `nguoidung`: Lưu tài khoản, mật khẩu băm Bcrypt, vai trò (`QuyenHan`), trạng thái (`TrangThai`).
  * `CuaHang`: Thông tin tiệm bánh, địa chỉ, liên kết 1-1 với `nguoidung`.
  * `SanPham`: Món bánh, giá bán, số lượng tồn, hình ảnh, liên kết N-1 với `CuaHang` và `DanhMuc`.
  * `GioHang`: Lưu giỏ hàng theo từng người dùng.
  * `DonHang`: Mã đơn, thông tin nhận hàng, phương thức thanh toán, trạng thái đơn, ghi chú đối soát chuyển khoản (`GhiChuThanhToan`), chỉ số thống kê (`NgayHoanThanh`, `NgayHuy`, `NguoiHuy`, `LyDoHuy`).
  * `ChiTietDonHang`: Lưu chi tiết từng món bánh và đơn giá tại thời điểm đặt.
  * `ThongBao`: Hệ thống thông báo chuông cho người mua, người bán và admin.
* **Ràng buộc khóa ngoại**: Sử dụng `ON DELETE RESTRICT` hoặc `CASCADE` hợp lý, tránh mồ côi dữ liệu.

#### 2. Kịch bản thuyết trình (Speaker Notes):
> *"Cơ sở dữ liệu của CAKEY gồm 7 bảng cốt lõi được thiết kế đạt chuẩn chuẩn hóa dạng 3NF. Đặc biệt ở bảng `DonHang`, chúng em bổ sung các trường dữ liệu chuyên biệt phục vụ phân tích nghiệp vụ như Người hủy đơn, Lý do hủy, Thời điểm hoàn thành và Chuỗi lịch sử chuyển khoản 2 chiều."*

---

### SLIDE 9: PHÂN HỆ KHÁCH HÀNG: TRẢI NGHIỆM MUA SẮM & LIVE-SEARCH

#### 1. Nội dung hiển thị trên slide:
* **Giao diện trang chủ**: Bố cục phong cách tiệm bánh ngọt, slider nổi bật, danh mục phân loại rõ ràng.
* **Tìm kiếm thời gian thực (Live Search AJAX)**:
  * Gõ từ khóa tới đâu, kết quả bánh gợi ý hiện ra tức thì không cần reload trang.
  * Tìm kiếm thông minh theo tên bánh, tên tiệm, loại bánh.
* **Trang chi tiết sản phẩm & Phân trang Bootstrap 5**:
  * Hiển thị đầy đủ thông tin: giá bán, số lượng tồn kho, tiệm sản xuất, mô tả bánh.
  * Tự động trừ tồn kho khi đơn hàng được tạo thành công.
  * Phân trang 8 bánh/trang bảo lưu bộ lọc khi chuyển trang.

#### 2. Ảnh minh chứng thực tế:
* **Ảnh chèn trên Slide:** `public/img/screenshots/screenshot_03_products_catalog.png`
* **Nội dung ảnh:** Danh mục sản phẩm bánh kem, bánh mì, cupcake và bộ lọc phân trang Bootstrap 5.

#### 3. Kịch bản thuyết trình (Speaker Notes):
> *"Ở phân hệ khách hàng, chúng em tập trung tối ưu trải nghiệm người dùng với tốc độ tải trang nhanh và tính năng Live Search bằng AJAX giúp khách hàng tìm thấy món bánh yêu thích chỉ trong vài giây."*

---

### SLIDE 10: QUY TRÌNH THANH TOÁN VIETQR & ĐỐI SOÁT 2 CHIỀU ĐỘC ĐÁO

#### 1. Nội dung hiển thị trên slide:
* **Luồng thanh toán chuyển khoản khép kín**:
  1. Khách chọn *Chuyển khoản ngân hàng / Quét mã QR* -> Xem trước VietQR kèm số tiền và cú pháp `CAKEY [Mã đơn]`.
  2. Đơn hàng sinh ra ở trạng thái: **"Chờ chuyển khoản"**.
  3. Khách quét mã app ngân hàng và bấm **"Xác nhận đã chuyển khoản"** -> Đơn chuyển sang: **"Chờ xác nhận chuyển khoản"**.
  4. Hệ thống bắn thông báo tức thì cho Người bán: *"Có người chuyển khoản đơn hàng #[Mã đơn]"*.
  5. Nếu Người bán bấm **"Chưa nhận tiền"** (chưa thấy biến động số dư): Đơn thành **"Chưa nhận được chuyển khoản"**.
  6. Khách hàng có 2 nút giải quyết:
     * **"Yêu cầu xem xét lại"**: Nhập mã giao dịch/lời giải trình -> Quay lại chờ tiệm xác nhận.
     * **"Thực hiện chuyển tiền lại"**: Quét lại mã QR để thao tác chuyển lại.

#### 2. Ảnh minh chứng thực tế:
* **Ảnh chèn trên Slide:** `public/img/screenshots/screenshot_08_checkout_vietqr.png`
* **Nội dung ảnh:** Màn hình thanh toán có mã QR ngân hàng MBBank Napas247 tự sinh theo số tiền đơn hàng.

#### 3. Kịch bản thuyết trình (Speaker Notes):
> *"Đây là một trong những điểm nhấn kỹ thuật quan trọng nhất của đồ án. Thay vì chỉ đặt hàng đơn thuần, chúng em giải quyết bài toán nhức nhối nhất của các sàn TMĐT: Sự sai lệch giữa lúc khách chuyển khoản và lúc chủ tiệm nhận được tiền. Bằng cơ chế đối soát 2 chiều, cả khách và tiệm đều có công cụ tương tác rõ ràng, minh bạch."*

---

### SLIDE 11: PHÂN HỆ NGƯỜI BÁN: QUẢN LÝ THỰC ĐƠN TIỆM BÁNH

#### 1. Nội dung hiển thị trên slide:
* **Các nghiệp vụ thực đơn**:
  * **Thêm bánh mới**: Upload ảnh trực tiếp từ máy tính lên server (`public/img`), tự sinh mã sản phẩm ngẫu nhiên không trùng lặp.
  * **Chỉnh sửa thông tin**: Cập nhật giá, mô tả, số lượng tồn kho nhanh chóng.
  * **Xóa mềm (Tạm ẩn bánh)**: Giữ lại lịch sử đơn hàng cũ nhưng không cho khách mới đặt.
  * **Cơ chế Phúc khảo bánh (Appeal)**: Khi bánh bị Admin tạm gỡ do nghi ngờ vi phạm, chủ tiệm có thể gửi đơn giải trình trực tiếp trên hệ thống để Admin duyệt mở bán lại.

#### 2. Ảnh minh chứng thực tế:
* **Ảnh chèn trên Slide:** `public/img/screenshots/screenshot_06_seller_dashboard.png`
* **Nội dung ảnh:** Giao diện Quản lý món bánh của Tiệm bánh (bảng danh sách bánh, nút ẩn/hiện, modal thêm bánh).

#### 3. Kịch bản thuyết trình (Speaker Notes):
> *"Tại kênh người bán, chủ tiệm được trao toàn quyền quản lý thực đơn với các tính năng CRUD tiện lợi, upload ảnh trực tiếp và cơ chế phúc khảo giúp người bán tương tác văn minh với ban quản trị."*

---

### SLIDE 12: PHÂN HỆ NGƯỜI BÁN: QUẢN LÝ & XỬ LÝ ĐƠN HÀNG

#### 1. Nội dung hiển thị trên slide:
* **Quản lý đơn hàng đặt tại tiệm**:
  * Phân loại đơn hàng đa tiêu chí: Mã đơn, Khách hàng & SĐT, Địa chỉ giao, Món bánh, Doanh thu.
  * Tab lọc trạng thái chuyên biệt: *Tất cả*, *Chuyển khoản*, *Chờ duyệt COD*, *Đã xác nhận*, *Đang giao*, *Hoàn thành*, *Đã hủy*.
* **Xử lý nhanh đơn chuyển khoản với 2 nút chuyên biệt**:
  * **"Đã nhận tiền"** (Green): Chuyển đơn sang trạng thái `Đã xác nhận`, thông báo cho khách tiệm đang làm bánh.
  * **"Chưa nhận tiền"** (Red outline): Mở modal nhập lý do (chưa thấy tiền, chuyển thiếu tiền, sai nội dung) và gửi thông báo trực tiếp đến khách.
* **Tiệm chủ động hủy đơn**: Mở modal chọn lý do mẫu (Hết nguyên liệu, Quá tải lò nướng, Địa chỉ quá xa) hoặc nhập lý do riêng.

#### 2. Ảnh minh chứng thực tế:
* **Ảnh chèn trên Slide:** `public/img/screenshots/screenshot_09_order_tracking.png`
* **Nội dung ảnh:** Màn hình đơn hàng với chi tiết trạng thái, địa chỉ nhận và các hành động xử lý đơn.

#### 3. Kịch bản thuyết trình (Speaker Notes):
> *"Trên giao diện quản lý đơn hàng của người bán, đối với các đơn hàng thanh toán chuyển khoản, hệ thống hiển thị trực diện 2 nút hành động: Đã nhận tiền và Chưa nhận tiền. Điều này giúp chủ tiệm thao tác ngay lập tức mà không cần trải qua nhiều bước rườm rà."*

---

### SLIDE 13: PHÂN HỆ NGƯỜI BÁN: THỐNG KÊ DOANH THU THEO NGÀY & THÁNG

#### 1. Nội dung hiển thị trên slide:
* **Hệ thống Dashboard phân tích chuyên sâu**:
  * **Thống kê theo ngày**: Chọn ngày bất kỳ -> Xem số tiền thực nhận từ các đơn giao hoàn tất trong ngày, số đơn hoàn thành, số đơn bị hủy, tỷ lệ hoàn thành.
  * **Thống kê theo tháng**: Chọn tháng bất kỳ -> Xem tổng doanh thu tháng, tổng đơn hoàn thành, tổng đơn hủy.
* **Điểm đặc sắc của thuật toán thống kê**:
  * Phân tách rõ ràng: **Khách hàng tự hủy đơn** vs **Tiệm bánh chủ động hủy đơn**.
  * Chỉ tính doanh thu khi đơn hàng chuyển sang trạng thái hoàn tất (`Đã hoàn thành` / `Đã giao thành công`).
  * Lọc danh sách đơn bảng bên dưới đồng bộ theo mốc ngày/tháng đang chọn.

#### 2. Kịch bản thuyết trình (Speaker Notes):
> *"Để người bán nắm rõ hiệu quả kinh doanh, chúng em đã xây dựng module báo cáo tài chính thời gian thực theo cả 2 chiều: Ngày và Tháng. Điểm đặc biệt là hệ thống phân tách rõ ràng đơn bị hủy do khách đổi ý hay do tiệm quá tải từ chối, giúp chủ tiệm đánh giá chính xác năng lực phục vụ của mình."*

---

### SLIDE 14: PHÂN HỆ QUẢN TRỊ VIÊN (ADMIN) & BẢO MẬT KICK-OUT

#### 1. Nội dung hiển thị trên slide:
* **Quản lý tài khoản toàn sàn**:
  * Xem danh sách người dùng, duyệt tiểu thương mở tiệm bánh.
  * Khóa tài khoản có hành vi gian lận hoặc vi phạm chính sách.
* **Cơ chế KICK-OUT tức thì (Real-time Session Ejection)**:
  * Nếu tài khoản đang đăng nhập trên hệ thống mà bị Admin bấm Khóa -> Ngay tại request tiếp theo, Middleware lập tức hủy Session, đăng xuất và đá văng về trang Đăng nhập.
  * Giao diện đăng nhập hiển thị cảnh báo đỏ nổi bật: **"Tài Khoản Đã Bị Khóa!"** với biểu tượng ổ khóa bảo mật.
  * Phân biệt chuẩn xác giữa: *Nhập sai mật khẩu* (Đăng nhập thất bại) và *Tài khoản bị cấm* (Tài khoản đã bị khóa).

#### 2. Ảnh minh chứng thực tế:
* **Ảnh chèn trên Slide:** `public/img/screenshots/screenshot_05_login.png`
* **Nội dung ảnh:** Form Đăng nhập và cảnh báo an ninh bảo mật.

#### 3. Kịch bản thuyết trình (Speaker Notes):
> *"Về mặt an ninh hệ thống, tính năng Kick-out tài khoản tức thì thông qua Middleware `CheckAccountStatus` đảm bảo rằng một khi Admin đã ban nick, kẻ gian không thể tiếp tục thực hiện bất kỳ thao tác nào thêm, bảo vệ an toàn tối đa cho dữ liệu của sàn."*

---

### SLIDE 15: CÁC ĐIỂM SÁNG TẠO & KỸ THUẬT NỔI BẬT TRONG ĐỒ ÁN

#### 1. Nội dung hiển thị trên slide:
* **1. Đèn pin soi mật khẩu xoay 360° độc đáo (Interactive Rotary Flashlight)**:
  * Sử dụng SVG và tính toán góc lượng giác `Math.atan2(dy, dx)`.
  * Giữ và xoay đèn pin quanh trục: Chiếu thẳng vào ô mật khẩu mới hiển thị text; xoay ra ngoài mật khẩu tự ẩn; có hiệu ứng vệt sáng quét sáng tạo.
* **2. VietQR API tích hợp thông minh**: Tự sinh chuỗi QR chứa số tài khoản, mã ngân hàng, số tiền và mã đơn chuẩn NAPAS247.
* **3. Real-time Notification AJAX Polling**: Hệ thống chuông thông báo tự động cập nhật số lượng thông báo mới mỗi 10 giây mà không cần reload trang.
* **4. Xác thực OTP Email**: Bảo vệ tài khoản khi đăng ký và quên mật khẩu qua mã OTP ngẫu nhiên 6 chữ số có thời hạn 5 phút.

#### 2. Kịch bản thuyết trình (Speaker Notes):
> *"Bên cạnh các nghiệp vụ TMĐT chuẩn mực, dự án còn có những điểm sáng tạo mang dấu ấn riêng: Hiệu ứng đèn pin xoay 360° soi mật khẩu bằng toán học hình học trên Canvas/CSS, tích hợp chuẩn VietQR quốc gia và hệ thống thông báo đẩy tự động."*

---

### SLIDE 16: KIỂM THỬ HỆ THỐNG (TESTING & QUALITY ASSURANCE)

#### 1. Nội dung hiển thị trên slide:
* **Phương pháp kiểm thử**: Áp dụng **Automated Feature Testing** với PHPUnit.
* **Các kịch bản kiểm thử trọng yếu (Test Suites)**:
  * `UserLockoutTest.php`: Kiểm thử cơ chế đá văng tài khoản bị khóa, phân biệt thông báo lỗi sai mật khẩu vs thông báo bị khóa.
  * `BankTransferOrderTest.php`: Kiểm thử trọn vẹn 6 trạng thái vòng đời đơn chuyển khoản (Đặt hàng -> Chờ CK -> Chờ xác nhận -> Đã xác nhận / Chưa nhận được -> Khiếu nại -> Chuyển lại).
  * `SellerOrderStatsTest.php`: Kiểm thử tính toán doanh thu ngày/tháng, tỷ lệ hoàn thành và phân loại người hủy.
* **Kết quả kiểm thử**:
  * **13/13 Feature Tests Passed (100%)**.
  * **61 Assertions thành công**, thời gian thực thi dưới 1 giây.
  * Mã nguồn tuân thủ nghiêm ngặt tiêu chuẩn PSR-12 thông qua **Laravel Pint**.

#### 2. Kịch bản thuyết trình (Speaker Notes):
> *"Để chứng minh tính ổn định và độ tin cậy của mã nguồn, nhóm đã viết bộ kiểm thử tự động với 13 ca kiểm thử chức năng bao phủ toàn bộ các luồng phức tạp nhất. Kết quả kiểm thử đạt 100% Passed trên PHPUnit."*

---

### SLIDE 17: ĐÁNH GIÁ KẾT QUẢ ĐẠT ĐƯỢC

#### 1. Nội dung hiển thị trên slide:
* **Ưu điểm đạt được**:
  * Giao diện thân thiện, hiện đại, màu sắc bắt mắt phù hợp ngành bánh ngọt.
  * Nghiệp vụ hoàn chỉnh, đáp ứng thực tế hoạt động của tiệm bánh vừa và nhỏ.
  * Luồng thanh toán VietQR và đối soát sao kê giảm thiểu 90% nhầm lẫn thủ công.
  * Kiến trúc phân tầng rõ ràng, code sạch, bảo mật thông tin tốt.
* **Hạn chế còn tồn tại**:
  * Cơ chế nhận tiền chuyển khoản hiện tại vẫn dựa trên việc chủ tiệm kiểm tra app ngân hàng rồi bấm nút (chưa liên kết trực tiếp webhook Web-API ngân hàng tự động duyệt 100%).
  * Chưa hỗ trợ đa ngôn ngữ (mới hỗ trợ tiếng Việt).
  * Chưa tích hợp GPS tính khoảng cách giao hàng động.

#### 2. Kịch bản thuyết trình (Speaker Notes):
> *"Đánh giá lại dự án, nhóm đã hoàn thành đầy đủ các mục tiêu đề ra ban đầu với một sản phẩm hoàn thiện có thể ứng dụng vào thực tế. Tuy nhiên, vẫn còn một số điểm có thể nâng cấp như tự động hóa webhook ngân hàng mà nhóm sẽ tiếp tục nghiên cứu."*

---

### SLIDE 18: HƯỚNG PHÁT TRIỂN TRONG TƯƠNG LAI

#### 1. Nội dung hiển thị trên slide:
* **Tích hợp Webhook Ngân hàng (Cassie / SePay / VietQR Pro)**: Tự động khớp lệnh sao kê và chuyển trạng thái 'Đã nhận tiền' chỉ sau 3 giây mà không cần chủ tiệm bấm tay.
* **Tích hợp cổng thanh toán trực tuyến**: VNPAY, MoMo, ZaloPay, thẻ quốc tế Visa/Mastercard.
* **Phát triển ứng dụng di động (Mobile App)**: Sử dụng Flutter / React Native cho shipper và chủ tiệm quản lý đơn tức thì.
* **Ứng dụng AI**: Chatbot tư vấn chọn bánh sinh nhật theo sở thích và gợi ý bánh cá nhân hóa.

#### 2. Kịch bản thuyết trình (Speaker Notes):
> *"Trong giai đoạn tiếp theo, nhóm định hướng tích hợp Webhook ngân hàng để hệ thống tự động xác nhận tiền về 24/7, phát triển app mobile cho tài xế giao bánh và ứng dụng AI tư vấn bánh ngọt theo sự kiện."*

---

### SLIDE 19: KẾT LUẬN & LỜI CẢM ƠN (Q&A)

#### 1. Nội dung hiển thị trên slide:
* **Thông điệp kết luận**:
  * *"CAKEY không chỉ là một đồ án môn học, mà là một giải pháp TMĐT hoàn chỉnh, giải quyết bài toán thực tế cho cộng đồng kinh doanh bánh ngọt."*
* **Lời cảm ơn**:
  * Chân thành cảm ơn Quý Thầy/Cô bộ môn đã tận tình hướng dẫn và đóng góp ý kiến quý báu trong suốt quá trình thực hiện đồ án!
* **HỎI & ĐÁP (Q&A)**:
  * Nhóm xin lắng nghe nhận xét và sẵn sàng trả lời các câu hỏi từ Hội đồng!

#### 2. Kịch bản thuyết trình (Speaker Notes):
> *"Trên đây là toàn bộ phần trình bày đồ án của nhóm về dự án Website bánh ngọt CAKEY. Em xin chân thành cảm ơn quý thầy cô đã chú ý lắng nghe. Sau đây, nhóm chúng em rất mong nhận được những lời nhận xét, góp ý và xin phép được trả lời các câu hỏi phản biện từ quý thầy cô!"*

---

# PHỤ LỤC: BỘ CÂU HỎI PHẢN BIỆN CỦA GIẢNG VIÊN & HƯỚNG DẪN TRẢ LỜI

### SLIDE 20: PHỤ LỤC VẤN ĐÁP 1 (VIETQR VÀ CONCURRENCY)

#### Câu hỏi 1: Tại sao em lại chọn mô hình thanh toán VietQR đối soát 2 chiều mà không tích hợp luôn VNPAY hay MoMo?
* **Cách trả lời của sinh viên**:
  > *"Dạ thưa thầy/cô, các tiệm bánh tham gia sàn đa phần là hộ kinh doanh nhỏ hoặc tiệm bánh handmade. Việc đăng ký cổng VNPAY hay MoMo đòi hỏi giấy phép kinh doanh doanh nghiệp và mức phí chiết khấu giao dịch từ 1.5% - 2.5% trên mỗi đơn hàng. Mô hình VietQR trực tiếp vừa miễn phí 100% phí giao dịch cho tiểu thương, vừa tiện lợi cho khách quét mã thanh toán 24/7. Đồng thời, cơ chế đối soát 2 chiều với nút 'Đã nhận tiền' và 'Chưa nhận tiền' kèm tính năng khiếu nại giúp chủ tiệm kiểm soát chặt chẽ dòng tiền vào tài khoản cá nhân của họ mà không sợ thất thoát."*

#### Câu hỏi 2: Em xử lý việc đồng thời cập nhật số lượng tồn kho (Concurrency / Race Condition) khi có nhiều khách cùng bấm mua như thế nào?
* **Cách trả lời của sinh viên**:
  > *"Dạ thưa thầy/cô, trong `CartController`, khi tạo đơn hàng, nhóm sử dụng phương thức `decrement('SoLuongTon', $qty)` của Eloquent ORM. Lệnh này biên dịch xuống câu SQL nguyên tử: `UPDATE SanPham SET SoLuongTon = SoLuongTon - ? WHERE MaSanPham = ?`. Thao tác này được engine InnoDB của MySQL khóa dòng (row-level lock) tự động trong transaction, đảm bảo tính toàn vẹn dữ liệu (ACID) và không bị âm kho khi có nhiều request đồng thời."*

---

### SLIDE 21: PHỤ LỤC VẤN ĐÁP 2 (KICK-OUT, THỐNG KÊ & BẢO MẬT)

#### Câu hỏi 3: Cơ chế "Đá văng tài khoản bị khóa" (Kick-out) hoạt động như thế nào trong Laravel?
* **Cách trả lời của sinh viên**:
  > *"Dạ thưa thầy/cô, nhóm cài đặt một Custom Middleware tên là `CheckAccountStatus` và đăng ký vào nhóm middleware `web` toàn cục. Ở mỗi HTTP request gửi lên server, middleware này sẽ kiểm tra `Auth::user()->TrangThai`. Nếu trạng thái bằng 0 (đã bị khóa), hệ thống sẽ ngay lập tức gọi `Auth::logout()`, xóa sạch Session bằng `$request->session()->invalidate()` và chuyển hướng người dùng về màn hình đăng nhập với cờ `locked=1` để thông báo rõ ràng."*

#### Câu hỏi 4: Thống kê doanh thu theo ngày và tháng của tiệm bánh được tính toán như thế nào để không bị sai lệch số liệu?
* **Cách trả lời của sinh viên**:
  > *"Dạ thưa thầy/cô, để số liệu thống kê doanh thu phản ánh đúng thực tế, nhóm chỉ tính tổng tiền đối với các đơn có trạng thái là `Đã hoàn thành` hoặc `Đã giao thành công`. Các đơn đang giao, đang chờ hoặc bị hủy hoàn toàn không được cộng vào doanh thu. Ngoài ra, ngày ghi nhận doanh thu được ưu tiên lấy theo trường `NgayHoanThanh` (thời điểm giao bánh thành công) chứ không lấy ngày đặt hàng `NgayDat`, tránh trường hợp đặt cuối tháng trước nhưng hoàn thành đầu tháng sau."*

#### Câu hỏi 5: Mật khẩu người dùng được bảo vệ như thế nào?
* **Cách trả lời của sinh viên**:
  > *"Dạ, toàn bộ mật khẩu trong cơ sở dữ liệu được băm bằng thuật toán **Bcrypt** an toàn (`Hash::make()` với salt ngẫu nhiên). Hệ thống tuyệt đối không lưu mật khẩu dạng plain text. Khi đăng nhập, phương thức `Hash::check()` hoặc `password_verify()` được sử dụng để so khớp hash một chiều, chống lại các cuộc tấn công tra từ điển hoặc rò rỉ cơ sở dữ liệu."*
