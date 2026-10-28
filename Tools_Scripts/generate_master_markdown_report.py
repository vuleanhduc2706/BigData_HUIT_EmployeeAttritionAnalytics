# -*- coding: utf-8 -*-
"""
Script tao file Bao Cao Nhom Mon Ma Nguon Mo & Kich Ban Thuyet Trinh chuan barem HUIT.
Bao gom:
1. Thong tin nhom 4 sinh vien, phan cong ro rang.
2. Mo ta de tai, ly do chon, kien truc cong nghe.
3. Thiet ke CSDL ERD (Mermaid + Bang dac ta 8 thuc the).
4. Thiet ke UML Use Case (Mermaid + Bang dac ta 3 Actor).
5. Chi tiet chuc nang chinh (CRUD, Auth/Middleware, Search + Pagination, Form Validation kem code).
6. 4/4 Diem cong mo rong (+1.0 diem): Upload anh, AJAX, API VietQR, Mobile Responsive.
7. 5 Tinh nang nang cao: Multi-vendor, Email OTP, In-App Notification, Quy trinh 2 chieu & Khieu nai, Soft Delete.
8. Huong dan cai dat, tai khoan test & chay he thong.
9. Kich ban thuyet trinh 14 Slide PowerPoint (Speaker Notes).
10. Bo cau hoi van dap Q&A.
"""

import os
import shutil

content = """# BÁO CÁO ĐỒ ÁN KẾT THÚC HỌC PHẦN MÔN HỌC MÃ NGUỒN MỞ
**Học phần:** Phát triển ứng dụng Mã Nguồn Mở (Open Source Application Development)  
**Đơn vị đào tạo:** Khoa Công Nghệ Thông Tin – Trường Đại học Công Thương TP.HCM (HUIT)  
**Đề tài thực hiện:** Xây dựng Website Bán Hàng Trực Tuyến – Sàn Bánh Ngọt Đa Cửa Hàng CAKEY (Nền tảng Laravel 11 + MySQL)  
**Tệp Slide thuyết trình:** `Slide_BaoCao_MaNguonMo_Cakey.pptx` (14 slide tỉ lệ 16:9)  
**Kho mã nguồn:** `C:\\laragon\\www\\doan_banhngot` (Local Host / GitHub)  

---

## 👥 THÔNG TIN NHÓM THỰC HIỆN & PHÂN CÔNG CÔNG VIỆC

* **Nhóm số:** 08 | **Lớp học phần:** Mã Nguồn Mở (Thứ 2, Tiết 1-3)
* **Quy mô nhóm:** 04 sinh viên (Tuân thủ đúng quy định chuẩn 3–5 sinh viên của Giảng viên).

| STT | Họ và Tên | MSSV | Vai trò | Phân công nhiệm vụ cụ thể | Đóng góp |
| :---: | :--- | :---: | :---: | :--- | :---: |
| **1** | **Vũ Lê Anh Đức** | **2001230191** | **Trưởng nhóm** | - Thiết kế kiến trúc tổng thể MVC Laravel 11.<br>- Xây dựng hệ thống Xác thực, Phân quyền 3 Roles bằng Middleware.<br>- Tích hợp cổng thanh toán trực tuyến VietQR API (MBBank).<br>- Triển khai cơ chế Xóa mềm (Soft Delete) & Khôi phục sản phẩm.<br>- Phân trang danh mục Bootstrap 5 & Tối ưu Responsive Mobile.<br>- Tổng hợp mã nguồn, viết báo cáo & đóng gói Slide. | **100%** |
| **2** | **Nguyễn Hoàng Long** | **2001230188** | **Thành viên** | - Thiết kế mô hình CSDL quan hệ MySQL (8 bảng InnoDB).<br>- Viết Database Migration, Seeder dữ liệu mẫu cho hệ thống.<br>- Xây dựng Module Người bán (Seller Dashboard): Thêm/Sửa/Xóa bánh.<br>- Xử lý Upload file hình ảnh an toàn vào thư mục `public/img`. | **100%** |
| **3** | **Trần Minh Quân** | **2001230195** | **Thành viên** | - Thiết kế giao diện Frontend Blade Template + Bootstrap 5.<br>- Xây dựng chức năng AJAX Live Search sản phẩm thời gian thực.<br>- Xây dựng giỏ hàng tương tác nhanh bằng AJAX không cần reload trang.<br>- Phát triển chuông thông báo In-App Notification real-time. | **100%** |
| **4** | **Lê Thị Kim Ngân** | **2001230182** | **Thành viên** | - Xây dựng Module Khách hàng & Đơn hàng (Checkout, Lịch sử mua hàng).<br>- Xây dựng chức năng Khiếu nại đơn hàng & Quy trình xác nhận 2 chiều.<br>- Viết toàn bộ Form Validation & Custom thông báo lỗi tiếng Việt.<br>- Kiểm thử luồng chức năng (Black-box testing) & Hỗ trợ làm slide. | **100%** |

---

## I. MÔ TẢ ĐỀ TÀI & BỐI CẢNH DỰ ÁN

### 1. Giới thiệu bài toán & Tính cấp thiết
* **Bối cảnh thực tế:** Ngành thực phẩm bánh ngọt (Bakery & Pastry) tại Việt Nam đang bùng nổ mạnh mẽ. Người tiêu dùng hiện đại có xu hướng đặt bánh sinh nhật, bánh kỷ niệm, tiệc teabreak qua internet với nhu cầu xem mẫu thực tế, tùy biến kích thước và thanh toán chuyển khoản nhanh chóng.
* **Hạn chế của các giải pháp truyền thống:** Các tiệm bánh vừa và nhỏ thường bán hàng thủ công qua mạng xã hội, dẫn đến tình trạng sót đơn hàng, nhầm lẫn nội dung chuyển khoản ngân hàng và khó quản lý lượng bánh tồn trong ngày.
* **Đề tài lựa chọn:** Nhóm đăng ký thực hiện **Đề tài số 3: "Website Bán hàng Online"** trong danh mục gợi ý của Giảng viên, và phát triển nâng cấp thành **Sàn thương mại điện tử Bánh Ngọt Đa Cửa Hàng CAKEY (Multi-vendor Bakery Platform)**.

### 2. Mục tiêu của dự án
1. **Tuân thủ tuyệt đối quy định môn học:** Sử dụng thuần túy PHP Laravel 11/10, cơ sở dữ liệu MySQL (Eloquent ORM, Migration, Seeder), giao diện Blade Template kết hợp Bootstrap 5, phân quyền nghiêm ngặt với 3 nhóm vai trò (Admin, Seller, Customer).
2. **Đạt chuẩn 100% các chức năng cốt lõi:** Đăng nhập/Đăng xuất, Phân quyền qua Middleware, CRUD trên các bảng quan hệ, Tìm kiếm và Phân trang chuẩn giao diện, Kiểm tra hợp lệ dữ liệu (Form Validation).
3. **Chinh phục trọn vẹn điểm cộng mở rộng (+1.0 điểm):**
   * Upload file ảnh sản phẩm an toàn (+0.25).
   * Tương tác AJAX Live Search và Giỏ hàng mượt mà (+0.25).
   * Tích hợp cổng thanh toán bên thứ ba VietQR API tự động sinh mã QR ngân hàng (+0.25).
   * Giao diện Responsive tối ưu chuẩn chỉnh trên cả Mobile và Desktop (+0.25).
4. **Phát triển 5 tính năng nâng cao thực tiễn:** Kiến trúc Multi-vendor duyệt shop, Xác thực Email OTP 2 bước, Chuông thông báo In-App, Quy trình đối soát chuyển khoản 2 chiều kèm Khiếu nại, và Cơ chế Xóa mềm bảo toàn dữ liệu lịch sử hóa đơn.

---

## II. THIẾT KẾ CƠ SỞ DỮ LIỆU (CSDL) & SƠ ĐỒ ERD

Hệ thống CAKEY sử dụng hệ quản trị CSDL **MySQL (Storage Engine: InnoDB)** nhằm bảo đảm tính toàn vẹn tham chiếu qua hệ thống khóa chính (PK) và khóa ngoại (FK) ràng buộc đa tầng (`ON UPDATE CASCADE`, `ON DELETE RESTRICT/CASCADE`).

### 1. Sơ đồ Thực thể Liên kết (ERD - Entity Relationship Diagram)

```mermaid
erDiagram
    nguoidung ||--o| CuaHang : "so_huu (1 - 0..1)"
    nguoidung ||--o{ DonHang : "dat_hang (1 - n)"
    nguoidung ||--o{ GioHang : "co_gio_hang (1 - n)"
    nguoidung ||--o{ ThongBao : "nhan (1 - n)"
    CuaHang ||--o{ SanPham : "dang_ban (1 - n)"
    danhmuc ||--o{ SanPham : "phan_loai (1 - n)"
    SanPham ||--o{ GioHang : "duoc_chon (1 - n)"
    DonHang ||--|{ ChiTietDonHang : "bao_gom (1 - n)"
    SanPham ||--o{ ChiTietDonHang : "xuat_ban (1 - n)"

    nguoidung {
        varchar(20) MaND PK
        varchar(100) HoTen
        varchar(15) SDT
        varchar(100) Email UK
        varchar(255) DiaChi
        varchar(255) MatKhau
        varchar(50) QuyenHan
        int TrangThai
    }

    CuaHang {
        varchar(20) MaCuaHang PK
        varchar(100) TenCuaHang
        varchar(20) MaND FK
        int TrangThaiCH
        varchar(255) DiaChi
    }

    danhmuc {
        varchar(20) MaDanhMuc PK
        varchar(100) TenDanhMuc
        varchar(255) MoTa
    }

    SanPham {
        varchar(30) MaSanPham PK
        varchar(150) Ten
        decimal GiaBan
        varchar(20) DonViTinh
        varchar(20) TrangThai
        varchar(255) MoTa
        varchar(500) HinhAnh
        int SoLuongTon
        varchar(20) MaDanhMuc FK
        varchar(20) MaCuaHang FK
    }

    GioHang {
        int id PK
        varchar(20) MaNguoiDung FK
        varchar(30) MaSanPham FK
        int SoLuong
        datetime NgayThem
    }

    DonHang {
        varchar(30) MaDon PK
        varchar(20) MaKhachHang FK
        varchar(100) HoTenKhach
        varchar(15) SoDienThoai
        varchar(255) DiaChiGiao
        varchar(20) PhuongThucThanhToan
        datetime NgayDat
        varchar(50) TrangThai
        decimal TongTien
        varchar(255) GhiChu
        varchar(255) GhiChuThanhToan
    }

    ChiTietDonHang {
        int id PK
        varchar(30) MaDon FK
        varchar(30) MaSanPham FK
        int SoLuong
        decimal DonGia
        decimal ThanhTien
    }

    ThongBao {
        int id PK
        varchar(20) user_id FK
        text NoiDung
        varchar(255) LienKet
        int TrangThai
        datetime created_at
    }
```

### 2. Từ điển Dữ liệu (Data Dictionary - Đặc tả 8 bảng)

1. **Bảng `nguoidung` (Quản lý tài khoản toàn sàn):**
   * `MaND` (VARCHAR 20, PK): Mã định danh duy nhất (VD: `NDADMIN`, `NDBAN001`, `NDMUA001`).
   * `HoTen` (VARCHAR 100, NOT NULL): Họ và tên người dùng.
   * `SDT` (VARCHAR 15, NOT NULL): Số điện thoại liên hệ.
   * `Email` (VARCHAR 100, UNIQUE, NOT NULL): Địa chỉ email dùng để đăng nhập và nhận OTP.
   * `DiaChi` (VARCHAR 255): Địa chỉ mặc định nhận bánh.
   * `MatKhau` (VARCHAR 255, NOT NULL): Mật khẩu băm an toàn theo thuật toán `Bcrypt`.
   * `QuyenHan` (VARCHAR 50, NOT NULL): Quyền truy cập (`ROLE_Admin`, `ROLE_NguoiBan`, `ROLE_NguoiMua`).
   * `TrangThai` (INT): `1` (Hoạt động bình thường), `2` (Chờ duyệt mở tiệm), `0` (Đang bị khóa).

2. **Bảng `CuaHang` (Thông tin tiệm bánh Multi-vendor):**
   * `MaCuaHang` (VARCHAR 20, PK): Mã tiệm bánh (VD: `CH001`).
   * `TenCuaHang` (VARCHAR 100, NOT NULL): Tên thương hiệu tiệm bánh.
   * `MaND` (VARCHAR 20, FK -> `nguoidung.MaND`, UNIQUE): Mã chủ cửa hàng (Quan hệ 1 - 1).
   * `TrangThaiCH` (INT): `1` (Đang mở bán), `0` (Tạm ngưng/Chờ duyệt).
   * `DiaChi` (VARCHAR 255): Địa chỉ lò bánh/cửa hàng vật lý.

3. **Bảng `danhmuc` (Phân loại bánh):**
   * `MaDanhMuc` (VARCHAR 20, PK): Mã danh mục (VD: `DM001` - Bánh kem sinh nhật, `DM002` - Cupcake, `DM003` - Bánh mỳ mặn).
   * `TenDanhMuc` (VARCHAR 100, NOT NULL): Tên loại bánh.
   * `MoTa` (VARCHAR 255): Giới thiệu ngắn về danh mục bánh.

4. **Bảng `SanPham` (Danh mục các loại bánh ngọt đang kinh doanh):**
   * `MaSanPham` (VARCHAR 30, PK): Mã sản phẩm (VD: `SP001`, `SP002`).
   * `Ten` (VARCHAR 150, NOT NULL): Tên loại bánh (VD: "Bánh kem dâu tây Pháp").
   * `GiaBan` (DECIMAL 12,2, NOT NULL): Giá niêm yết (VNĐ).
   * `DonViTinh` (VARCHAR 20): Đơn vị bán (cái, hộp, set 6 cái).
   * `TrangThai` (VARCHAR 20): `Đang bán`, `Hết hàng`, `Tạm gỡ` (Cơ chế Xóa mềm - Soft Delete).
   * `MoTa` (VARCHAR 255): Mô tả hương vị, thành phần nguyên liệu.
   * `HinhAnh` (VARCHAR 500): Tên tệp ảnh đại diện trong thư mục `public/img`.
   * `SoLuongTon` (INT, DEFAULT 0): Số lượng bánh sẵn có trong ngày.
   * `MaDanhMuc` (VARCHAR 20, FK -> `danhmuc.MaDanhMuc`): Nhóm bánh.
   * `MaCuaHang` (VARCHAR 20, FK -> `CuaHang.MaCuaHang`): Tiệm bánh sở hữu sản phẩm.

5. **Bảng `GioHang` (Giỏ hàng trực tuyến):**
   * `id` (INT, AUTO_INCREMENT, PK): Khóa chính tự tăng.
   * `MaNguoiDung` (VARCHAR 20, FK -> `nguoidung.MaND`): Khách hàng chọn bánh.
   * `MaSanPham` (VARCHAR 30, FK -> `SanPham.MaSanPham`): Sản phẩm thêm vào giỏ.
   * `SoLuong` (INT, NOT NULL): Số lượng bánh đặt mua.
   * `NgayThem` (DATETIME): Thời điểm đưa vào giỏ.
   * *Ràng buộc:* `UNIQUE(MaNguoiDung, MaSanPham)` đảm bảo mỗi loại bánh chỉ xuất hiện 1 dòng trong giỏ, tăng số lượng khi bấm lặp lại.

6. **Bảng `DonHang` (Hóa đơn đặt bánh):**
   * `MaDon` (VARCHAR 30, PK): Mã đơn hàng sinh tự động (VD: `DH20261019-1234`).
   * `MaKhachHang` (VARCHAR 20, FK -> `nguoidung.MaND`): Khách hàng đặt mua.
   * `HoTenKhach`, `SoDienThoai`, `DiaChiGiao`: Thông tin giao hàng nhận bánh.
   * `PhuongThucThanhToan` (VARCHAR 20): `COD` (Tiền mặt khi nhận) hoặc `ChuyenKhoan` (Quét mã VietQR).
   * `NgayDat` (DATETIME, NOT NULL): Thời gian tạo đơn.
   * `TrangThai` (VARCHAR 50, NOT NULL): `Chờ xử lý`, `Đang chuẩn bị bánh`, `Đang giao hàng`, `Đã nhận hàng`, `Đã thanh toán`, `Khiếu nại`, `Đã hủy`.
   * `TongTien` (DECIMAL 14,2, NOT NULL): Tổng giá trị đơn hàng.
   * `GhiChuThanhToan`: Lưu trữ mã tham chiếu chuyển khoản hoặc lý do khiếu nại.

7. **Bảng `ChiTietDonHang` (Danh sách bánh trong từng hóa đơn):**
   * `id` (INT, AUTO_INCREMENT, PK): Khóa chính tự tăng.
   * `MaDon` (VARCHAR 30, FK -> `DonHang.MaDon`): Thuộc đơn hàng nào.
   * `MaSanPham` (VARCHAR 30, FK -> `SanPham.MaSanPham`): Sản phẩm được bán.
   * `SoLuong` (INT, NOT NULL): Số lượng từng loại bánh.
   * `DonGia` (DECIMAL 12,2, NOT NULL): Đơn giá tại thời điểm mua (bảo vệ lịch sử giá).
   * `ThanhTien` (DECIMAL 14,2, NOT NULL): `SoLuong * DonGia`.

8. **Bảng `ThongBao` (Thông báo In-App thời gian thực):**
   * `id` (INT, AUTO_INCREMENT, PK): Khóa chính tự tăng.
   * `user_id` (VARCHAR 20, FK -> `nguoidung.MaND`): Người nhận thông báo.
   * `NoiDung` (TEXT): Lời nhắn (VD: "Đơn hàng #DH... của bạn đã được tiệm bánh giao đi").
   * `LienKet` (VARCHAR 255): Đường dẫn chuyển hướng khi bấm vào thông báo.
   * `TrangThai` (INT): `0` (Chưa đọc), `1` (Đã đọc).
   * `created_at` (DATETIME): Thời điểm phát sinh thông báo.

---

## III. THIẾT KẾ UML USE CASE

Hệ thống CAKEY phân bổ đặc quyền rõ ràng cho **03 Tác nhân (Actors)** thông qua cơ chế phân quyền RBAC (Role-Based Access Control) của Laravel.

### 1. Sơ đồ Tổng quát UML Use Case

```mermaid
graph LR
    subgraph Actors [TÁC NHÂN HỆ THỐNG]
        Customer((Khách hàng\nROLE_NguoiMua))
        Seller((Chủ tiệm bánh\nROLE_NguoiBan))
        Admin((Quản trị viên\nROLE_Admin))
    end

    subgraph GuestFeatures [CHỨC NĂNG CHUNG]
        UC_Auth[Đăng ký, Đăng nhập, Email OTP, Đổi MK]
        UC_Search[Tìm kiếm AJAX Live Search & Lọc bánh]
        UC_Paginate[Xem danh mục bánh có Phân trang]
        UC_Detail[Xem chi tiết món bánh]
    end

    subgraph CustomerFeatures [CHỨC NĂNG KHÁCH HÀNG]
        UC_Cart[Quản lý giỏ hàng: Thêm, Sửa số lượng, Xóa]
        UC_Checkout[Đặt bánh & Thanh toán quét mã VietQR]
        UC_OrderHistory[Xem lịch sử & Tiến độ đơn hàng]
        UC_Appeal[Gửi khiếu nại đơn hàng chuyển khoản]
        UC_RegisterShop[Gửi hồ sơ đăng ký mở tiệm bánh]
    end

    subgraph SellerFeatures [CHỨC NĂNG NGƯỜI BÁN]
        UC_ProductCRUD[CRUD Sản phẩm bánh: Thêm, Sửa, Gỡ, Khôi phục]
        UC_UploadImg[Upload ảnh bánh chất lượng cao]
        UC_SellerOrders[Tiếp nhận & Chuyển trạng thái đơn bánh]
        UC_ConfirmPayment[Xác nhận đã nhận tiền chuyển khoản]
    end

    subgraph AdminFeatures [CHỨC NĂNG QUẢN TRỊ VIÊN]
        UC_ApproveSeller[Xét duyệt đơn mở tiệm bánh mới]
        UC_UserManage[Quản lý tài khoản: Khóa/Mở khóa vi phạm]
        UC_ProductAudit[Kiểm duyệt sản phẩm toàn hệ thống]
        UC_SystemMonitor[Giám sát toàn bộ đơn hàng & Xử lý khiếu nại]
    end

    Customer --> UC_Auth
    Customer --> UC_Search
    Customer --> UC_Paginate
    Customer --> UC_Detail
    Customer --> UC_Cart
    Customer --> UC_Checkout
    Customer --> UC_OrderHistory
    Customer --> UC_Appeal
    Customer --> UC_RegisterShop

    Seller --> UC_Auth
    Seller --> UC_ProductCRUD
    Seller --> UC_UploadImg
    Seller --> UC_SellerOrders
    Seller --> UC_ConfirmPayment

    Admin --> UC_Auth
    Admin --> UC_ApproveSeller
    Admin --> UC_UserManage
    Admin --> UC_ProductAudit
    Admin --> UC_SystemMonitor
```

### 2. Đặc tả Chi tiết các Use Case Trọng yếu

| Tên Use Case | Tác nhân chính | Tiền điều kiện | Luồng sự kiện chính (Main Flow) | Hậu điều kiện (Post-condition) |
| :--- | :--- | :--- | :--- | :--- |
| **UC01: Đăng nhập & Phân quyền** | Tất cả Actor | Tài khoản đã tồn tại trong CSDL | 1. Nhập Email và Mật khẩu.<br>2. Hệ thống kiểm tra `Bcrypt::check()`.<br>3. Kiểm tra cột `TrangThai == 1`.<br>4. Middleware điều hướng: Admin vào `/admin`, Seller vào `/seller`, Khách vào `/`. | Khởi tạo Session đăng nhập, cấp đúng quyền hạn trên thanh điều hướng. |
| **UC02: Live Search & Phân trang** | Khách hàng | Truy cập trang Sản phẩm | 1. Gõ từ khóa vào ô tìm kiếm.<br>2. JavaScript gửi `fetch()` đến `/products/live-search`.<br>3. Kết quả hiển thị dropdown không reload trang.<br>4. Chuyển trang qua thanh phân trang Bootstrap 5 (8 bánh/trang). | Hiển thị sản phẩm chính xác, giữ nguyên các tham số lọc URL. |
| **UC03: Đặt bánh & Thanh toán VietQR** | Khách hàng | Giỏ hàng có ít nhất 1 món | 1. Vào giỏ hàng bấm "Tiến hành đặt hàng".<br>2. Nhập thông tin người nhận, chọn "Chuyển khoản VietQR".<br>3. Hệ thống tạo đơn hàng và gọi API VietQR sinh ảnh QR.<br>4. Khách quét mã chuyển khoản -> Bấm "Xác nhận đã chuyển". | Đơn hàng chuyển trạng thái "Chờ tiệm bánh xác nhận thanh toán", thông báo gửi đến Seller. |
| **UC04: CRUD Sản phẩm có Upload ảnh** | Chủ tiệm bánh | Đăng nhập với quyền `ROLE_NguoiBan` | 1. Vào mục "Quản lý sản phẩm" -> Bấm "Thêm bánh mới".<br>2. Điền form: Tên bánh, Giá, Danh mục, Mô tả.<br>3. Chọn tệp ảnh từ máy tính (`.jpg`, `.png`, `.webp` < 5MB).<br>4. Hệ thống lưu ảnh vào `public/img` và lưu bản ghi vào bảng `SanPham`. | Sản phẩm xuất hiện ngay lập tức trên sàn thương mại điện tử. |
| **UC05: Duyệt đăng ký mở tiệm bánh** | Quản trị viên | Đăng nhập với quyền `ROLE_Admin` | 1. Admin vào "Danh sách yêu cầu mở tiệm".<br>2. Xem xét thông tin: Tên tiệm, Địa chỉ, Chủ tiệm.<br>3. Bấm "Phê duyệt": Cột `QuyenHan` đổi sang `ROLE_NguoiBan`, kích hoạt bản ghi trong bảng `CuaHang`. | Tài khoản khách hàng lập tức có quyền truy cập Seller Dashboard. |

---

## IV. ĐỐI CHIẾU CHỨC NĂNG TỐI THIỂU THEO QUY ĐỊNH MÔN HỌC

Nhóm tự hào đáp ứng **100% đầy đủ và vượt mức** các yêu cầu tối thiểu trong đề cương môn học:

### 1. Thao tác CRUD trên ít nhất 2 bảng dữ liệu có quan hệ (Exceed: 8 bảng)
* **Quan hệ Cửa hàng – Sản phẩm (`CuaHang` 1-n `SanPham`):**
  * **Create:** Seller tạo sản phẩm mới liên kết trực tiếp với `MaCuaHang` của tài khoản đăng nhập.
  * **Read:** Khách hàng duyệt danh mục theo danh mục, Seller quản lý danh sách sản phẩm tiệm mình.
  * **Update:** Sửa tên, đổi giá bán, cập nhật mô tả và thay đổi hình ảnh đại diện.
  * **Delete / Soft Delete:** Tạm gỡ bánh khỏi sàn bán (`TrangThai = 'Tạm gỡ'`) và có nút Khôi phục để tránh mất liên kết trong các hóa đơn cũ.
* **Quan hệ Đơn hàng – Chi tiết Đơn hàng (`DonHang` 1-n `ChiTietDonHang`):**
  * Khởi tạo đồng thời hóa đơn chính và các dòng chi tiết qua giao dịch Eloquent ORM.

```php
// Minh chứng Eloquent Model Relation (app/Models/SanPham.php)
class SanPham extends Model
{
    protected $table = 'SanPham';
    protected $primaryKey = 'MaSanPham';
    public $incrementing = false;
    protected $keyType = 'string';

    public function cuaHang() {
        return $this->belongsTo(CuaHang::class, 'MaCuaHang', 'MaCuaHang');
    }

    public function danhMuc() {
        return $this->belongsTo(DanhMuc::class, 'MaDanhMuc', 'MaDanhMuc');
    }
}
```

### 2. Chức năng Đăng nhập / Đăng xuất & Phân quyền (Auth + Middleware)
* Hệ thống xây dựng 2 Custom Middleware chuyên biệt:
  * `AdminMiddleware` (bảo vệ toàn bộ route `/admin/*`):
    ```php
    public function handle(Request $request, Closure $next): Response {
        if (!Auth::check() || Auth::user()->QuyenHan !== 'ROLE_Admin') {
            return redirect('/')->with('error', 'Bạn không có quyền truy cập Quản trị viên!');
        }
        return $next($request);
    }
    ```
  * `SellerMiddleware` (bảo vệ toàn bộ route `/seller/*`):
    ```php
    public function handle(Request $request, Closure $next): Response {
        if (!Auth::check() || Auth::user()->QuyenHan !== 'ROLE_NguoiBan') {
            return redirect('/')->with('error', 'Chỉ chủ tiệm bánh mới có quyền truy cập khu vực này!');
        }
        return $next($request);
    }
    ```

### 3. Tìm kiếm & Phân trang dữ liệu
* **Tìm kiếm AJAX Live Search:** Khi người dùng nhập từ khóa, hệ thống truy vấn real-time không reload trang:
  ```php
  // app/Http/Controllers/Client/ProductController.php
  public function liveSearch(Request $request) {
      $keyword = trim($request->get('keyword', ''));
      $products = SanPham::where('TrangThai', 'Đang bán')
          ->where('Ten', 'LIKE', "%{$keyword}%")
          ->take(6)
          ->get(['MaSanPham', 'Ten', 'GiaBan', 'HinhAnh']);
      return response()->json(['success' => true, 'data' => $products]);
  }
  ```
* **Phân trang dữ liệu (Pagination):** Áp dụng chuẩn **Bootstrap 5 Pagination** với 8 sản phẩm/trang, giữ nguyên bộ lọc danh mục và từ khóa:
  ```php
  // Khởi tạo phân trang chuẩn tại ProductController.php
  $products = $query->paginate(8)->withQueryString();
  return view('client.products', compact('products', 'categories'));
  ```
  Và cấu hình kích hoạt trong `app/Providers/AppServiceProvider.php`:
  ```php
  use Illuminate\Pagination\Paginator;
  public function boot(): void {
      Paginator::useBootstrapFive();
  }
  ```

### 4. Validation dữ liệu khi nhập Form (Kiểm tra hợp lệ)
* Toàn bộ các form nhập liệu đều được kiểm định chặt chẽ cả ở phía Frontend (HTML5) và Backend (Laravel Validation) với thông báo lỗi tiếng Việt tùy biến trực quan:
  ```php
  $request->validate([
      'Ten' => 'required|string|max:150',
      'GiaBan' => 'required|numeric|min:1000',
      'MaDanhMuc' => 'required|exists:danhmuc,MaDanhMuc',
      'HinhAnh' => 'nullable|image|mimes:jpeg,png,jpg,webp|max:5120',
  ], [
      'Ten.required' => 'Vui lòng nhập tên món bánh!',
      'GiaBan.numeric' => 'Giá bán phải là số hợp lệ!',
      'GiaBan.min' => 'Giá bán tối thiểu từ 1,000 VNĐ!',
      'HinhAnh.image' => 'Tệp tải lên bắt buộc phải là hình ảnh!',
      'HinhAnh.max' => 'Dung lượng ảnh không được vượt quá 5MB!'
  ]);
  ```

---

## V. ĐỐI CHIẾU 4/4 TIÊU CHÍ ĐIỂM CỘNG MỞ RỘNG (+1.0 ĐIỂM)

Nhóm đã hoàn thiện trọn vẹn cả 4 hạng mục điểm cộng được Giảng viên công bố trong quy chế đánh giá:

| STT | Tiêu chí điểm cộng của Giảng viên | Mức điểm | Triển khai thực tế trên Dự án CAKEY | Minh chứng mã nguồn / Giao diện |
| :---: | :--- | :---: | :--- | :--- |
| **1** | **Upload file an toàn** (hình ảnh, tài liệu) | **+0.25** | - Cho phép chủ tiệm bánh tải ảnh thực tế khi đăng bánh.<br>- Kiểm tra MIME Type chặt chẽ (`jpeg,png,jpg,webp`), dung lượng tối đa 5MB.<br>- Sinh tên tệp duy nhất bằng `time() . '_' . $file->getClientOriginalName()` lưu vào `public/img`. | `app/Http/Controllers/Seller/SellerController.php` (Phương thức `store` & `update`) |
| **2** | **Sử dụng AJAX** cho ít nhất 1 chức năng | **+0.25** | Tích hợp AJAX tại **03 tính năng vượt chuẩn**:<br>1. *AJAX Live Search:* Gợi ý bánh tức thì theo từng ký tự gõ phím.<br>2. *AJAX Cart:* Thêm bánh vào giỏ và đổi số lượng trực tiếp không bị reload trang.<br>3. *AJAX Notification:* Kiểm tra và đếm số thông báo mới cho người dùng. | `public/js/client.js` kết hợp Fetch API chuẩn ES6 |
| **3** | **Tích hợp API bên thứ ba** (Thanh toán) | **+0.25** | - Tích hợp dịch vụ **VietQR API** chuẩn chuyển khoản Napas 24/7.<br>- Tự động tạo ảnh QR với số tài khoản ngân hàng MBBank, số tiền chính xác theo hóa đơn và nội dung chuyển khoản mã đơn tự động. | `https://img.vietqr.io/image/MB-0867441036-compact2.png?amount=...&addInfo=...` |
| **4** | **Giao diện Responsive tốt trên Mobile** | **+0.25** | - Thiết kế theo triết lý Mobile-First bằng **Bootstrap 5 Grid System**.<br>- Thanh điều hướng thu gọn Offcanvas / Toggler mượt mà.<br>- Bảng giỏ hàng tự động co giãn và nút bấm thân thiện với thao tác cảm ứng. | Thử nghiệm 100% hiển thị hoàn hảo trên iPhone 12/13/14, iPad và Màn hình Desktop |

---

## VI. 5 TÍNH NĂNG ĐẶC BIỆT NÂNG CAO LÀM THÊM NGOÀI ĐỀ BÀI

Bên cạnh việc hoàn thành xuất sắc các yêu cầu tối thiểu và 4 tiêu chí điểm cộng, nhóm đã chủ động nghiên cứu và cài đặt thêm 5 tính năng nâng cấp thực tế:

1. **Mô hình Sàn đa cửa hàng Multi-vendor 3 cấp bậc:** Khách hàng mua hàng có thể bấm "Đăng ký mở tiệm bánh". Hồ sơ chuyển đến Admin phê duyệt, sau khi duyệt tài khoản tự động nâng cấp lên `ROLE_NguoiBan` và được phân quyền quản lý gian hàng riêng.
2. **Bảo mật Xác thực Email OTP 2 bước (2FA):** Tích hợp mã OTP gồm 6 chữ số gửi qua Email khi đăng ký tài khoản mới và khi thực hiện quy trình Quên mật khẩu, chống đăng ký rác và bảo vệ tài khoản tối đa.
3. **Hệ thống Chuông thông báo In-App Notification:** Khi đơn hàng thay đổi trạng thái (Tiệm bánh đã nhận đơn, Đang giao bánh, Đã xác nhận tiền), chuông thông báo trên thanh điều hướng lập tức sáng đỏ và hiện popup thông báo cho người dùng.
4. **Quy trình Thanh toán 2 chiều & Cơ chế Khiếu nại (Dispute Resolution):** Khi khách chọn chuyển khoản VietQR, đơn hàng hiển thị trạng thái "Chờ tiệm xác nhận". Nếu tiệm bánh từ chối hoặc có sai sót, khách hàng có nút "Gửi khiếu nại" kèm bằng chứng chuyển khoản để Admin can thiệp.
5. **Cơ chế Xóa mềm (Soft Delete) & Khôi phục sản phẩm:** Giúp chủ tiệm bánh có thể tạm ẩn các loại bánh hết mùa vụ mà không làm đứt gãy dữ liệu lịch sử của các đơn hàng cũ trong bảng `ChiTietDonHang`.

---

## VII. HƯỚNG DẪN CÀI ĐẶT & CHẠY THỰC NGHIỆM

Hệ thống được đóng gói chuẩn mực, dễ dàng triển khai trên môi trường Laragon hoặc XAMPP trên hệ điều hành Windows:

### 1. Yêu cầu môi trường
* PHP >= 8.2 (Bật các extension: `pdo_mysql`, `mbstring`, `openssl`, `curl`, `fileinfo`).
* MySQL Server >= 8.0 (hoặc MariaDB >= 10.4).
* Công cụ Composer & Trình quản lý máy chủ ảo Laragon.

### 2. Các bước khởi chạy nhanh
1. **Đặt mã nguồn dự án:** Sao chép thư mục `doan_banhngot` vào thư mục `C:\\laragon\\www\\doan_banhngot`.
2. **Cấu hình Cơ sở dữ liệu:**
   * Mở HeidiSQL hoặc phpMyAdmin trong Laragon, tạo database tên: `BanhNgot`.
   * Nhập (Import) tệp `database.sql` đi kèm trong thư mục gốc của dự án.
3. **Cấu hình tệp môi trường `.env`:**
   ```ini
   APP_NAME="CAKEY Bakery Shop"
   APP_ENV=local
   APP_KEY=base64:XG8dF5uU+oYvXFfF8yD2k5f6hE7g9A1bC2dE3fG4hI0=
   APP_DEBUG=true
   APP_URL=http://localhost:8000

   DB_CONNECTION=mysql
   DB_HOST=127.0.0.1
   DB_PORT=3306
   DB_DATABASE=BanhNgot
   DB_USERNAME=root
   DB_PASSWORD=
   ```
4. **Khởi động ứng dụng:**
   * Mở terminal tại thư mục dự án và chạy:
     ```bash
     $ php artisan serve
     ```
   * Mở trình duyệt và truy cập: `http://localhost:8000` (hoặc tên miền ảo `http://doan_banhngot.test` trên Laragon).

### 3. Danh sách Tài khoản Test mẫu kiểm tra chức năng
Tất cả các tài khoản mẫu đều dùng mật khẩu mặc định là: `123456`

| Vai trò | Email đăng nhập | Mật khẩu | Phạm vi quyền hạn kiểm thử |
| :--- | :--- | :---: | :--- |
| **Quản trị viên (Admin)** | `admin@cakey.local` | `123456` | Duyệt tiệm bánh mới, Khóa tài khoản, Xem toàn bộ đơn hàng sàn. |
| **Chủ tiệm bánh (Seller)**| `seller@cakey.local` | `123456` | Quản lý sản phẩm (CRUD, Upload ảnh), Duyệt đơn và Xác nhận tiền VietQR. |
| **Khách hàng (Customer)** | `user@cakey.local` | `123456` | Tìm kiếm AJAX, Đặt hàng VietQR, Gửi khiếu nại, Nộp đơn mở shop. |
| **Khách chờ duyệt shop** | `pending-seller@cakey.local`| `123456` | Đã nộp đơn mở tiệm, đang chờ Admin phê duyệt để thành Seller. |

---

## 🎤 VIII. KỊCH BẢN THUYẾT MINH SLIDE BÁO CÁO (SPEAKER NOTES CHI TIẾT 14 SLIDE)

Dưới đây là lời thoại gợi ý được xây dựng khoa học, tự tin và chuyên nghiệp dành cho sinh viên khi đứng báo cáo trước Hội đồng Giảng viên:

### 📌 SLIDE 1: TRANG BÌA (MỞ ĐẦU ẤN TƯỢNG)
* **Thời lượng dự kiến:** 45 giây.
* **Lời thoại thuyết trình:**
  > *"Kính chào Thầy và các bạn trong hội đồng báo cáo! Hôm nay, nhóm 08 chúng em rất vinh dự được đại diện trình bày đề tài kết thúc học phần môn học Phát triển ứng dụng Mã Nguồn Mở với tên gọi: **'Xây dựng Website Bán Hàng Trực Tuyến – Sàn Bánh Ngọt Đa Cửa Hàng CAKEY trên nền tảng Laravel 11 và MySQL'**.  
  Nhóm chúng em gồm 4 thành viên do bạn Vũ Lê Anh Đức làm trưởng nhóm, cùng các bạn Nguyễn Hoàng Long, Trần Minh Quân và Lê Thị Kim Ngân phối hợp thực hiện. Kính mời Thầy cùng theo dõi nội dung báo cáo của nhóm!"*

### 📌 SLIDE 2: BỐI CẢNH & LÝ DO CHỌN ĐỀ TÀI
* **Thời lượng dự kiến:** 1 phút.
* **Lời thoại thuyết trình:**
  > *"Thưa Thầy, ngành kinh doanh bánh ngọt tại các đô thị lớn đang có sự chuyển dịch rất nhanh sang mô hình trực tuyến. Khách hàng mong muốn xem hình ảnh bánh chân thực, tìm kiếm vị bánh yêu thích và chuyển khoản ngân hàng ngay trong tích tắc.  
  Xuất phát từ thực tế đó, nhóm đã chọn Đề tài số 3 trong danh mục gợi ý của Thầy là 'Website Bán hàng Online', và quyết định nâng cấp lên thành mô hình **Sàn bánh ngọt đa cửa hàng (Multi-vendor)**, cho phép nhiều tiệm bánh cùng tham gia mở gian hàng, kết hợp công nghệ quét mã QR VietQR thông minh nhằm tự động hóa tối đa khâu thanh toán."*

### 📌 SLIDE 3: KIẾN TRÚC CÔNG NGHỆ ÁP DỤNG
* **Thời lượng dự kiến:** 1 phút.
* **Lời thoại thuyết trình:**
  > *"Về kiến trúc công nghệ, hệ thống CAKEY tuân thủ 100% chuẩn mực bài học môn Mã Nguồn Mở:  
  • Ở tầng Backend: Nhóm sử dụng PHP Laravel 11 theo mô hình MVC hiện đại, khai thác sức mạnh của Eloquent ORM để liên kết dữ liệu, và kiểm soát truy cập bằng Middleware.  
  • Ở tầng Cơ sở dữ liệu: Dùng MySQL InnoDB có ràng buộc khóa ngoại chặt chẽ, khởi tạo tự động bằng Migration và Seeder.  
  • Ở tầng Giao diện: Sử dụng Blade Template kết hợp Bootstrap 5 theo thiết kế chuẩn Responsive Mobile.  
  • Về mặt tương tác: Nhóm sử dụng AJAX để mang lại trải nghiệm mượt mà không reload trang, cùng dịch vụ VietQR API của bên thứ ba để xử lý thanh toán ngân hàng."*

### 📌 SLIDE 4: THIẾT KẾ CƠ SỞ DỮ LIỆU (SƠ ĐỒ ERD 8 THỰC THỂ)
* **Thời lượng dự kiến:** 1 phút 15 giây.
* **Lời thoại thuyết trình:**
  > *"CSDL của nhóm được thiết kế chuẩn hóa mức cao gồm 8 bảng dữ liệu quan hệ:  
  • Bảng trung tâm là `nguoidung` quản lý 3 vai trò, liên kết 1-1 với bảng `CuaHang` và liên kết 1-n với `GioHang` và `DonHang`.  
  • Bảng `SanPham` liên kết n-1 với `CuaHang` và `danhmuc`, lưu trữ đầy đủ hình ảnh, giá bán và số lượng tồn kho.  
  • Mỗi `DonHang` khi được tạo ra sẽ sinh đồng thời các bản ghi trong `ChiTietDonHang` để lưu lại đơn giá tại thời điểm mua, tránh việc giá bánh sau này thay đổi làm sai lệch lịch sử tài chính.  
  • Cuối cùng là bảng `ThongBao` phục vụ hệ thống chuông báo thời gian thực."*

### 📌 SLIDE 5: THIẾT KẾ UML USE CASE (3 VAI TRÒ HỆ THỐNG)
* **Thời lượng dự kiến:** 1 phút.
* **Lời thoại thuyết trình:**
  > *"Về mặt phân quyền, nhóm phân định rõ 3 tác nhân với các đặc quyền độc lập, vượt tiêu chí tối thiểu 2 role của Thầy:  
  • Nhóm Khách hàng: Có thể tìm kiếm bánh bằng AJAX, đặt hàng, thanh toán VietQR, theo dõi trạng thái đơn và nộp đơn xin mở tiệm bánh.  
  • Nhóm Chủ tiệm bánh (Seller): Sở hữu không gian quản trị tiệm bánh riêng, có quyền CRUD sản phẩm, upload ảnh bánh và xác nhận tiền chuyển khoản của khách.  
  • Nhóm Quản trị viên (Admin): Giữ quyền tối cao để phê duyệt đơn mở tiệm bánh mới, khóa tài khoản vi phạm và giám sát toàn bộ đơn hàng trên sàn."*

### 📌 SLIDE 6, 7, 8: CHI TIẾT TỪNG VAI TRÒ
* **Thời lượng dự kiến:** 2 phút.
* **Lời thoại thuyết trình:**
  > *"Đi sâu vào các phân hệ:  
  • Slide 6 mô tả phân hệ Khách hàng: Với thanh tìm kiếm AJAX Live Search gõ đến đâu hiển thị ngay đến đó, phân trang Bootstrap 5 chuẩn 8 sản phẩm/trang, giỏ hàng AJAX thông minh và cổng quét mã QR ngân hàng tiện lợi.  
  • Slide 7 là phân hệ Người bán: Có bảng thống kê doanh thu, form đăng bánh có kiểm tra định dạng ảnh và cơ chế Xóa mềm để bảo vệ lịch sử mua bán.  
  • Slide 8 là phân hệ Quản trị viên: Có bảng điều khiển giám sát người dùng, cơ chế 1-click để duyệt tiệm bánh mới và xử lý khiếu nại đơn hàng."*

### 📌 SLIDE 9: ĐỐI CHIẾU 4 TIÊU CHÍ ĐIỂM CỘNG (+1.0 ĐIỂM)
* **Thời lượng dự kiến:** 1 phút 15 giây.
* **Lời thoại thuyết trình:**
  > *"Kính thưa Thầy, đối chiếu với 4 tiêu chuẩn cộng điểm của đề bài, nhóm tự tin đã chinh phục trọn vẹn 1.0 điểm cộng:  
  1. Upload file an toàn: Có kiểm tra định dạng và giới hạn 5MB.  
  2. AJAX: Không chỉ dùng 1 mà dùng ở cả 3 tính năng: Tìm kiếm trực tiếp, Thao tác giỏ hàng và Chuông thông báo.  
  3. API bên ngoài: Tích hợp VietQR API tự động sinh ảnh thanh toán tài khoản MBBank chuẩn quốc tế.  
  4. Responsive: Giao diện thích ứng hoàn hảo trên mọi kích thước màn hình từ điện thoại đến máy tính."*

### 📌 SLIDE 10: 5 TÍNH NĂNG ĐẶC BIỆT LÀM THÊM
* **Thời lượng dự kiến:** 1 phút.
* **Lời thoại thuyết trình:**
  > *"Không dừng lại ở đó, nhóm còn mở rộng thêm 5 chức năng thực tế:  
  • Quy trình xét duyệt mở shop Multi-vendor bài bản.  
  • Bảo mật 2 bước bằng mã Email OTP khi đăng ký và lấy lại mật khẩu.  
  • Chuông thông báo In-App Notification hiển thị biến động đơn hàng tức thì.  
  • Cơ chế xác nhận tiền chuyển khoản 2 chiều kết hợp tính năng Khiếu nại bảo vệ người tiêu dùng.  
  • Và kỹ thuật Xóa mềm (Soft Delete) giúp giữ nguyên dữ liệu báo cáo tài chính."*

### 📌 SLIDE 11: KỊCH BẢN DEMO THỰC TẾ
* **Thời lượng dự kiến:** 2 phút 30 giây (Vừa nói vừa thao tác trên trình duyệt).
* **Lời thoại thuyết trình:**
  > *"Ngay sau đây, nhóm xin phép được Demo trực tiếp luồng hoạt động khép kín trên máy theo 4 bước:  
  Bước 1: Em đóng vai Khách hàng dùng Live Search tìm bánh kem dâu tây -> thêm vào giỏ hàng -> tiến hành đặt hàng với phương thức quét mã VietQR.  
  Bước 2: Khách hàng nộp đơn đăng ký mở tiệm bánh mới mang tên 'Bakery HUIT'.  
  Bước 3: Em đăng nhập tài khoản Admin, vào duyệt hồ sơ tiệm 'Bakery HUIT' thành công.  
  Bước 4: Em đăng nhập tài khoản tiệm bánh vừa được duyệt, tiến hành đăng món bánh mới có upload ảnh từ máy tính và vào mục Đơn hàng để bấm 'Xác nhận đã nhận tiền' cho đơn hàng ở Bước 1."*

### 📌 SLIDE 12, 13, 14: ĐÁNH GIÁ, BẢNG PHÂN CÔNG & LỜI CẢM ƠN
* **Thời lượng dự kiến:** 1 phút.
* **Lời thoại thuyết trình:**
  > *"Bảng phân công ở Slide 12 thể hiện rõ 4 thành viên trong nhóm đều tham gia tích cực với 100% trách nhiệm và khối lượng công việc được giao.  
  Hệ thống chạy ổn định, code chuẩn MVC và giao diện thân thiện. Hướng phát triển tiếp theo nhóm sẽ tích hợp thêm hệ thống đánh giá sao và cổng Webhook tự động nhận thông báo biến động số dư ngân hàng.  
  Em xin trân trọng cảm ơn Thầy và các bạn đã chú ý lắng nghe! Nhóm chúng em rất mong nhận được những nhận xét và góp ý quý báu của Thầy ạ!"*

---

## ❓ IX. BỘ CÂU HỎI VẤN ĐÁP KỸ THUẬT (Q&A DỰ PHÒNG KHI GIẢNG VIÊN ĐẶT CÂU HỎI)

1. **Câu hỏi 1: Nhóm đã cấu hình và tổ chức phân quyền Middleware như thế nào trong Laravel?**  
   * **Trả lời của sinh viên:**  
     *"Dạ thưa Thầy, nhóm tạo 2 Middleware là `AdminMiddleware` và `SellerMiddleware` trong thư mục `app/Http/Middleware`. Trong mỗi Middleware, hàm `handle()` sẽ kiểm tra `Auth::check()` và so sánh trường `QuyenHan` của người dùng. Trong tệp `routes/web.php`, nhóm gom các route theo Route Group có bọc tiền tố và middleware tương ứng. Nếu một người dùng cố tình truy cập trái phép bằng cách gõ trực tiếp URL, Middleware sẽ chặn lại và redirect về trang chủ kèm theo thông báo cảnh báo qua Flash Message."*

2. **Câu hỏi 2: Kỹ thuật AJAX Live Search được hiện thực như thế nào giữa JavaScript và Laravel Controller?**  
   * **Trả lời của sinh viên:**  
     *"Dạ, ở phía client, nhóm bắt sự kiện `input` trên ô tìm kiếm. Mỗi khi người dùng gõ phím, JavaScript sẽ gửi một request ngầm dạng `fetch('/products/live-search?keyword=' + encodeURIComponent(val))` lên server. Ở phía `ProductController`, phương thức `liveSearch()` nhận từ khóa, dùng Eloquent ORM truy vấn `SanPham::where('Ten', 'LIKE', "%$keyword%")->take(6)->get()` và trả về dữ liệu thuần định dạng JSON `response()->json(...)`. JavaScript nhận mảng JSON này và lặp để tạo các thẻ HTML hiển thị danh sách gợi ý ngay dưới ô tìm kiếm mà trang web không hề bị reload."*

3. **Câu hỏi 3: Tại sao nhóm lại chọn cổng VietQR API qua URL `https://img.vietqr.io` thay vì cài đặt thư viện SDK nặng?**  
   * **Trả lời của sinh viên:**  
     *"Dạ thưa Thầy, dịch vụ chuẩn của VietQR cho phép tạo ảnh mã QR Napas 24/7 trực tiếp qua chuỗi URL RESTful với cú pháp chuẩn: `https://img.vietqr.io/image/{BankCode}-{AccountNumber}-{Template}.png?amount={Amount}&addInfo={Content}`. Cách làm này giúp ứng dụng Laravel của nhóm giữ được độ tinh gọn cao, không bị phình to thư mục `vendor`, tương thích tốt với mọi phiên bản PHP và tốc độ render ảnh QR ngân hàng nhanh gần như tức thì."*

4. **Câu hỏi 4: Khi chủ tiệm bánh xóa một sản phẩm, nếu sản phẩm đó đã nằm trong các đơn hàng cũ thì CSDL xử lý thế nào để không lỗi khóa ngoại?**  
   * **Trả lời của sinh viên:**  
     *"Dạ thưa Thầy, đây là bài toán toàn vẹn dữ liệu rất thực tế. Nhóm đã áp dụng kỹ thuật **Xóa mềm (Soft Delete)**. Trong bảng `SanPham`, nhóm có cột `TrangThai`. Khi chủ tiệm chọn xóa bánh, Controller không thực hiện câu lệnh `DELETE FROM SanPham`, mà chỉ cập nhật `TrangThai = 'Tạm gỡ'`. Như vậy, món bánh sẽ lập tức biến mất khỏi trang danh mục người mua, nhưng dòng dữ liệu vẫn tồn tại trong CSDL để các hóa đơn trong bảng `ChiTietDonHang` vẫn truy xuất được tên bánh và đơn giá lịch sử mà không bị vi phạm ràng buộc khóa ngoại."*

5. **Câu hỏi 5: Nhóm làm cách nào để chống tấn công bảo mật CSRF trong các form và request AJAX?**  
   * **Trả lời của sinh viên:**  
     *"Dạ, đối với các form HTML thông thường, nhóm luôn gắn chỉ thị `@csrf` của Blade để sinh input ẩn chứa token ngẫu nhiên. Còn đối với các request AJAX gửi bằng JavaScript Fetch API, nhóm đặt thẻ `<meta name="csrf-token" content="{{ csrf_token() }}">` ở phần `<head>` của layout chung, sau đó trong mã JS sẽ đọc thẻ này và truyền vào HTTP Header `'X-CSRF-TOKEN'` của request, đảm bảo mọi thao tác đều được Laravel verify hợp lệ."*

6. **Câu hỏi 6: Tính năng phân trang Bootstrap 5 được cấu hình như thế nào?**  
   * **Trả lời của sinh viên:**  
     *"Dạ thưa Thầy, mặc định Laravel sử dụng Tailwind CSS cho phân trang. Để chuyển sang Bootstrap 5, nhóm đã khai báo `Paginator::useBootstrapFive();` trong hàm `boot()` của `app/Providers/AppServiceProvider.php`. Trong Controller, nhóm gọi hàm `paginate(8)->withQueryString()` trên Query Builder. Ở ngoài view Blade, nhóm chỉ cần gọi `{{ $products->links() }}` là Laravel tự động render ra thanh phân trang số trang chuẩn giao diện Bootstrap 5."*

---

*Báo cáo được hoàn thiện và kiểm thử toàn diện vào ngày 19/10/2026 bởi Nhóm 08 - ĐH Công Thương TP.HCM (HUIT).*
"""

# Ghi vao cac tep dich
files_to_write = [
    r"D:\Doan_BigData\BAO_CAO_NHOM_MA_NGUON_MO.md",
    r"D:\Doan_BigData\KICH_BAN_THUYET_TRINH_SLIDE_MA_NGUON_MO.md",
    r"C:\laragon\www\doan_banhngot\BAO_CAO_NHOM_MA_NGUON_MO.md",
    r"C:\laragon\www\doan_banhngot\README.md",
    r"C:\laragon\www\doan_banhngot\KICH_BAN_THUYET_TRINH_SLIDE_MA_NGUON_MO.md"
]

for file_path in files_to_write:
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"[OK] Da ghi thanh cong: {file_path} ({len(content)} ky tu)")
    except Exception as e:
        print(f"[ERR] Khong the ghi {file_path}: {e}")
