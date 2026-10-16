import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  
  // Cho phép CORS cho giao diện Web Client (HTML/JS/Next.js/React)
  app.enableCors({
    origin: '*',
    methods: 'GET,HEAD,PUT,PATCH,POST,DELETE,OPTIONS',
  });

  const PORT = process.env.PORT || 3000;
  await app.listen(PORT);
  console.log('='.repeat(70));
  console.log(`[NestJS Backend API] Server đang chạy tại: http://localhost:${PORT}`);
  console.log(`[NestJS Backend API] Đồ án Big Data - Vũ Lê Anh Đức (2001230191)`);
  console.log(`[NestJS Backend API] REST Endpoints:`);
  console.log(`   - GET  /api/spark-sql/overview      : Toàn bộ 6 truy vấn Spark SQL & KPIs`);
  console.log(`   - GET  /api/spark-sql/query/:id     : Lấy dữ liệu 1 truy vấn Spark SQL`);
  console.log(`   - GET  /api/ml/metrics              : Chỉ số đánh giá RF, LR & Benchmark`);
  console.log(`   - GET  /api/ml/kmeans               : Kết quả phân cụm K-Means 4 nhóm`);
  console.log(`   - POST /api/ml/predict-risk         : AI suy luận rủi ro nghỉ việc tức thời`);
  console.log(`   - GET  /api/streaming/latest        : Luồng Kafka Streaming & Cảnh báo 3 cấp`);
  console.log(`   - GET  /api/pipeline/status         : Trạng thái 9 bước & HDFS Data Lake`);
  console.log('='.repeat(70));
}
bootstrap();
