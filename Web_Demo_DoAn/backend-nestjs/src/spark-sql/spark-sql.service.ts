import { Injectable, NotFoundException } from '@nestjs/common';
import * as fs from 'fs';
import * as path from 'path';

@Injectable()
export class SparkSqlService {
  private getOutputDir(): string {
    return path.resolve(process.cwd(), '..', 'data', 'output');
  }

  getOverview() {
    const filePath = path.join(this.getOutputDir(), 'spark_sql_analytics.json');
    if (fs.existsSync(filePath)) {
      const raw = fs.readFileSync(filePath, 'utf-8');
      return JSON.parse(raw);
    }
    return {
      metadata: { error: 'Dữ liệu Spark SQL chưa được khởi tạo. Hãy chạy Bước 5.' },
      kpis: {},
      queries: {},
    };
  }

  getQueryById(id: string) {
    const overview = this.getOverview();
    const queryKey = `query_${id}`;
    if (overview.queries && overview.queries[queryKey]) {
      return overview.queries[queryKey];
    }
    throw new NotFoundException(`Không tìm thấy truy vấn Spark SQL với ID '${id}'`);
  }
}
