import { Controller, Get, Param } from '@nestjs/common';
import { SparkSqlService } from './spark-sql.service';

@Controller('api/spark-sql')
export class SparkSqlController {
  constructor(private readonly sparkSqlService: SparkSqlService) {}

  @Get('overview')
  getOverview() {
    return this.sparkSqlService.getOverview();
  }

  @Get('query/:id')
  getQueryById(@Param('id') id: string) {
    return this.sparkSqlService.getQueryById(id);
  }
}
