import { Module } from '@nestjs/common';
import { SparkSqlController } from './spark-sql.controller';
import { SparkSqlService } from './spark-sql.service';

@Module({
  controllers: [SparkSqlController],
  providers: [SparkSqlService],
  exports: [SparkSqlService],
})
export class SparkSqlModule {}
