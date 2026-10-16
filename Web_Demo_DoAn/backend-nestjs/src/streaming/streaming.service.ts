import { Injectable } from '@nestjs/common';
import * as fs from 'fs';
import * as path from 'path';

@Injectable()
export class StreamingService {
  private getOutputDir(): string {
    return path.resolve(process.cwd(), '..', 'data', 'output');
  }

  getLatestEvents() {
    const filePath = path.join(this.getOutputDir(), 'kafka_stream_events.json');
    if (fs.existsSync(filePath)) {
      try {
        return JSON.parse(fs.readFileSync(filePath, 'utf-8'));
      } catch (e) {
        return [];
      }
    }
    return [];
  }

  generateSimulatedEvent() {
    const templates = [
      { code: 'CHECK_IN_LATE', desc: 'Nhân viên đi muộn > 45 phút không báo trước', delta: 7.0 },
      { code: 'OVERTIME_NIGHT', desc: 'Làm thêm giờ ca đêm > 4 tiếng liên tục', delta: 15.0 },
      { code: 'WEEKEND_ACCESS', desc: 'Đăng nhập hệ thống nội bộ vào ngày nghỉ', delta: 5.5 },
      { code: 'COMPENSATION_LOOKUP', desc: 'Tra cứu bảng lương & quy chế thôi việc', delta: 13.0 },
      { code: 'JOB_PORTAL_DETECTED', desc: 'Truy cập các trang tuyển dụng bên ngoài', delta: 19.5 },
      { code: 'NEGATIVE_FEEDBACK', desc: 'Gửi khảo sát không hài lòng về quản lý', delta: 23.0 },
      { code: 'COMMENDATION_AWARD', desc: 'Được khen thưởng hoàn thành xuất sắc dự án', delta: -14.0 },
      { code: 'ON_TIME_CHECKIN', desc: 'Check-in đúng giờ và hoàn thành tốt ca làm', delta: -3.0 },
    ];

    const roles = ['Sales Executive', 'Research Scientist', 'Laboratory Technician', 'Developer', 'HR Specialist'];
    const departments = ['Research & Development', 'Sales', 'Human Resources'];
    
    const empId = `EMP_${Math.floor(1001 + Math.random() * 469)}`;
    const tpl = templates[Math.floor(Math.random() * templates.length)];
    const dept = departments[Math.floor(Math.random() * departments.length)];
    const role = roles[Math.floor(Math.random() * roles.length)];
    
    const priorRisk = Math.random() * 55 + 20;
    let newRisk = Math.max(5, Math.min(99, priorRisk + tpl.delta + (Math.random() * 4 - 2)));
    newRisk = Math.round(newRisk * 10) / 10;

    let alertLevel = 'CẤP 1: AN TOÀN (LOW RISK)';
    let badgeColor = '#10b981';
    if (newRisk >= 70.0) {
      alertLevel = 'CẤP 3: BÁO ĐỘNG ĐỎ (HIGH RISK)';
      badgeColor = '#ef4444';
    } else if (newRisk >= 30.0) {
      alertLevel = 'CẤP 2: CẢNH BÁO (MEDIUM RISK)';
      badgeColor = '#f59e0b';
    }

    const now = new Date();
    const timeStr = now.toISOString().replace('T', ' ').substring(0, 19);

    const newEvent = {
      event_id: `EVT-${Date.now()}`,
      timestamp: timeStr,
      employee_id: empId,
      department: dept,
      role: role,
      event_type: tpl.code,
      description: tpl.desc,
      risk_delta: `${tpl.delta > 0 ? '+' : ''}${tpl.delta}%`,
      current_risk_score: newRisk,
      alert_level: alertLevel,
      badge_color: badgeColor,
    };

    // Lưu vào buffer
    const list = this.getLatestEvents();
    list.unshift(newEvent);
    if (list.length > 50) list.pop(); // giữ 50 events gần nhất
    try {
      const p = path.join(this.getOutputDir(), 'kafka_stream_events.json');
      fs.writeFileSync(p, JSON.stringify(list, null, 2), 'utf-8');
    } catch (e) {}

    return newEvent;
  }
}
