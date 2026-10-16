import { Injectable } from '@nestjs/common';
import * as fs from 'fs';
import * as path from 'path';

@Injectable()
export class PipelineService {
  private getBaseDir(): string {
    return path.resolve(process.cwd(), '..');
  }

  getFolderInfo() {
    const dataDir = path.join(this.getBaseDir(), 'data');
    const info: Record<string, any> = {};
    for (const sub of ['raw', 'processed', 'output']) {
      const p = path.join(dataDir, sub);
      if (fs.existsSync(p)) {
        const files = fs.readdirSync(p);
        let sizeKb = 0;
        files.forEach((f) => {
          const fp = path.join(p, f);
          if (fs.statSync(fp).isFile()) {
            sizeKb += fs.statSync(fp).size / 1024;
          }
        });
        info[sub] = { files, count: files.length, size_kb: Math.round(sizeKb * 10) / 10 };
      } else {
        info[sub] = { files: [], count: 0, size_kb: 0 };
      }
    }
    return info;
  }

  getStatus() {
    return {
      student: {
        name: 'Vũ Lê Anh Đức',
        role: 'Học viên',
        id: '2001230191',
        workspace: '/courses/2/projects/3/students/2001230191',
      },
      hadoop: {
        version: 'Hadoop 3.4.0 (Windows Native with WinUtils)',
        status: 'BigData Core sẵn sàng',
        cluster: '5 DataNodes (7 blocks WORM, Replication=2)',
      },
      folders: this.getFolderInfo(),
      storageBenchmark: this.getBenchmark(),
    };
  }

  getBenchmark() {
    const p = path.join(this.getBaseDir(), 'data', 'output', 'storage_benchmark.json');
    if (fs.existsSync(p)) {
      try {
        return JSON.parse(fs.readFileSync(p, 'utf-8'));
      } catch (e) {}
    }
    return null;
  }

  getAirflowDag() {
    const p = path.join(this.getBaseDir(), 'data', 'output', 'airflow_dag_status.json');
    if (fs.existsSync(p)) {
      try {
        return JSON.parse(fs.readFileSync(p, 'utf-8'));
      } catch (e) {}
    }
    return { error: 'Chưa có thông tin DAG. Hãy chạy Bước 9.' };
  }
}
