import { Module } from '@nestjs/common';
import { SparkSqlModule } from './spark-sql/spark-sql.module';
import { MlAnalyticsModule } from './ml-analytics/ml-analytics.module';
import { StreamingModule } from './streaming/streaming.module';
import { PipelineModule } from './pipeline/pipeline.module';

@Module({
  imports: [SparkSqlModule, MlAnalyticsModule, StreamingModule, PipelineModule],
  controllers: [],
  providers: [],
})
export class AppModule {}
