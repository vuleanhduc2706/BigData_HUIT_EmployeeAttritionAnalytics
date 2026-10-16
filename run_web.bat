@echo off
chcp 65001 > nul
title BigData Lab Dashboard - Vu Le Anh Duc 2001230191
echo ======================================================================
echo    BIGDATA LAB - HE THONG PHAN TICH DA CHIEU & DU DOAN NHAN SU
echo    Sinh vien: Vu Le Anh Duc - MSSV: 2001230191
echo ======================================================================
echo.
echo [*] Dang khoi dong Web Dashboard tai http://localhost:5000 ...
cd Web_Demo_DoAn
python app.py
pause
