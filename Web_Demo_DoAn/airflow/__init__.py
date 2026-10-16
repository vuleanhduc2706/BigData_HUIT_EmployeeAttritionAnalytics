"""
Apache Airflow local compatibility stub for Windows & IDE environment.
Cung cấp định nghĩa lớp DAG phục vụ kiểm tra cú pháp, hiển thị IDE và chạy cục bộ.
"""
from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional

class DAG:
    """Mock Apache Airflow DAG class for local syntax validation & execution."""
    def __init__(
        self,
        dag_id: str,
        default_args: Optional[Dict[str, Any]] = None,
        description: Optional[str] = None,
        schedule_interval: Optional[str] = None,
        catchup: bool = False,
        tags: Optional[List[str]] = None,
        **kwargs: Any
    ):
        self.dag_id = dag_id
        self.default_args = default_args or {}
        self.description = description
        self.schedule_interval = schedule_interval
        self.catchup = catchup
        self.tags = tags or []
        self.tasks: List[Any] = []

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

__all__ = ["DAG"]
