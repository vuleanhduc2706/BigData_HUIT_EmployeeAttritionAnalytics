import { Module } from '@nestjs/common';
import { MlAnalyticsController } from './ml-analytics.controller';
import { MlAnalyticsService } from './ml-analytics.service';

@Module({
  controllers: [MlAnalyticsController],
  providers: [MlAnalyticsService],
  exports: [MlAnalyticsService],
})
export class MlAnalyticsModule {}
