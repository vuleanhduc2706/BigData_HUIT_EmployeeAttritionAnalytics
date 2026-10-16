import { Controller, Get, Post, Body } from '@nestjs/common';
import { MlAnalyticsService, PredictRiskDto } from './ml-analytics.service';

@Controller('api/ml')
export class MlAnalyticsController {
  constructor(private readonly mlService: MlAnalyticsService) {}

  @Get('metrics')
  getMetrics() {
    return this.mlService.getMetrics();
  }

  @Get('kmeans')
  getKMeans() {
    return this.mlService.getKMeans();
  }

  @Get('risk-distribution')
  getRiskDistribution() {
    return this.mlService.getRiskDistribution();
  }

  @Get('high-risk-employees')
  getHighRiskEmployees() {
    return this.mlService.getHighRiskEmployees();
  }

  @Get('experiments')
  getExperiments() {
    return this.mlService.getExperiments();
  }

  @Get('misclassified-cases')
  getMisclassifiedCases() {
    return this.mlService.getMisclassifiedCases();
  }

  @Post('predict-risk')
  predictRisk(@Body() dto: PredictRiskDto) {
    return this.mlService.predictRisk(dto);
  }
}
