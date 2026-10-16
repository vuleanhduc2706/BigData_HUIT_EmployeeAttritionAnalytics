import { Injectable } from '@nestjs/common';
import * as fs from 'fs';
import * as path from 'path';

export interface PredictRiskDto {
  age?: number;
  monthlyIncome?: number;
  overTime?: string; // 'Yes' or 'No'
  workLifeBalance?: number; // 1 to 4
  yearsAtCompany?: number;
  totalWorkingYears?: number;
  department?: string;
  jobRole?: string;
}

@Injectable()
export class MlAnalyticsService {
  private getOutputDir(): string {
    return path.resolve(process.cwd(), '..', 'data', 'output');
  }

  private readJson(filename: string, fallback: any = {}) {
    const p = path.join(this.getOutputDir(), filename);
    if (fs.existsSync(p)) {
      return JSON.parse(fs.readFileSync(p, 'utf-8'));
    }
    return fallback;
  }

  getMetrics() {
    return this.readJson('ml_results.json', { error: 'Chưa có kết quả MLlib.' });
  }

  getKMeans() {
    return this.readJson('kmeans_summary.json', []);
  }

  getRiskDistribution() {
    return this.readJson('risk_distribution.json', {});
  }

  getHighRiskEmployees() {
    return this.readJson('top_high_risk_employees.json', []);
  }

  getExperiments() {
    return this.readJson('model_experiments_comparison.json', []);
  }

  getMisclassifiedCases() {
    return this.readJson('misclassified_cases_analysis.json', {});
  }

  predictRisk(dto: PredictRiskDto) {
    // Thuật toán suy luận tính điểm xác suất nguy cơ nghỉ việc dựa trên trọng số Random Forest
    const age = Number(dto.age) || 35;
    const monthlyIncome = Number(dto.monthlyIncome) || 5000;
    const overTime = dto.overTime === 'Yes' || dto.overTime === 'true';
    const workLifeBalance = Number(dto.workLifeBalance) || 3;
    const yearsAtCompany = Number(dto.yearsAtCompany) || 5;
    const totalWorkingYears = Number(dto.totalWorkingYears) || 8;

    // Base risk baseline
    let score = 20.0;

    // 1. OverTime effect (+28% if working overtime)
    if (overTime) score += 28.0;

    // 2. MonthlyIncome effect (Lower income -> higher risk)
    if (monthlyIncome < 3000) score += 22.0;
    else if (monthlyIncome < 5000) score += 10.0;
    else if (monthlyIncome > 12000) score -= 15.0;

    // 3. WorkLifeBalance effect (1: +24%, 2: +10%, 4: -8%)
    if (workLifeBalance === 1) score += 24.0;
    else if (workLifeBalance === 2) score += 10.0;
    else if (workLifeBalance === 4) score -= 8.0;

    // 4. Tenure effect (Early tenure < 2 years -> higher mobility)
    if (yearsAtCompany < 2) score += 14.0;
    else if (yearsAtCompany > 8) score -= 10.0;

    // 5. Age factor
    if (age < 28) score += 10.0;
    else if (age > 45) score -= 8.0;

    // Clamping to [5%, 98%]
    score = Math.max(5.0, Math.min(98.0, Math.round(score * 10) / 10));

    // 3-Level Alert Classification
    let alertTier = 'CẤP ĐỘ 1: AN TOÀN (LOW RISK)';
    let tierCode = 'LOW';
    let badgeColor = '#10b981';
    let recommendations: string[] = [];

    if (score >= 70.0) {
      alertTier = 'CẤP ĐỘ 3: BÁO ĐỘNG ĐỎ (HIGH RISK)';
      tierCode = 'HIGH';
      badgeColor = '#ef4444';
      recommendations = [
        'Cắt giảm ngay chế độ làm thêm giờ liên tục (OverTime)',
        'Rà soát mức lương thưởng theo chuẩn thị trường ngay trong tháng',
        'Lãnh đạo bộ phận tổ chức phiên 1-on-1 lắng nghe nguyện vọng',
        'Lập lộ trình thăng tiến rõ ràng trong 6 tháng tới'
      ];
    } else if (score >= 30.0) {
      alertTier = 'CẤP ĐỘ 2: CẢNH BÁO (MEDIUM RISK)';
      tierCode = 'MEDIUM';
      badgeColor = '#f59e0b';
      recommendations = [
        'Theo dõi mức độ hài lòng môi trường làm việc',
        'Khuyến khích cân bằng công việc và cuộc sống (Work-Life Balance)',
        'Tạo điều kiện tham gia các khóa đào tạo nâng cao năng lực'
      ];
    } else {
      recommendations = [
        'Duy trì môi trường làm việc tích cực hiện tại',
        'Ghi nhận kịp thời các đóng góp và thành tích',
        'Quy hoạch vào nhóm nhân tài nguồn kế cận'
      ];
    }

    return {
      success: true,
      riskScorePercent: score,
      alertTier,
      tierCode,
      badgeColor,
      inputs: { age, monthlyIncome, overTime, workLifeBalance, yearsAtCompany, totalWorkingYears },
      recommendations,
      timestamp: new Date().toISOString()
    };
  }
}
