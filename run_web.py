"""
Trình khởi chạy nhanh Web Dashboard từ thư mục gốc D:\\Doan_BigData
Sinh viên: Vũ Lê Anh Đức - MSSV: 2001230191
"""
import os
import sys
import subprocess

if __name__ == '__main__':
    root_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.join(root_dir, "Web_Demo_DoAn")
    app_path = os.path.join(project_dir, "app.py")
    
    print("=" * 70)
    print(">>> BIGDATA LAB - HỆ THỐNG PHÂN TÍCH ĐA CHIỀU & DỰ ĐOÁN NGHỈ VIỆC")
    print("    Sinh viên: Vũ Lê Anh Đức - MSSV: 2001230191")
    print(f"    Thư mục làm việc: {project_dir}")
    print("    Đang khởi động Web Dashboard tại: http://localhost:5000")
    print("=" * 70)
    
    os.chdir(project_dir)
    subprocess.run([sys.executable, app_path])
