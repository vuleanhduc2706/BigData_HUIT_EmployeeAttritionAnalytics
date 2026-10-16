"""
Airflow BashOperator stub for Windows & local IDE compatibility.
Hỗ trợ đầy đủ cú pháp BashOperator và toán tử chuỗi phụ thuộc (>>).
"""
from datetime import timedelta
from typing import Any, List, Optional

class BashOperator:
    """Mock Apache Airflow BashOperator class."""
    def __init__(
        self,
        task_id: str,
        bash_command: str,
        execution_timeout: Optional[timedelta] = None,
        **kwargs: Any
    ):
        self.task_id = task_id
        self.bash_command = bash_command
        self.execution_timeout = execution_timeout
        self.upstream: List['BashOperator'] = []
        self.downstream: List['BashOperator'] = []

    def __rshift__(self, other: Any) -> Any:
        if isinstance(other, BashOperator):
            self.downstream.append(other)
            other.upstream.append(self)
        return other

    def __repr__(self) -> str:
        return f"<BashOperator: {self.task_id}>"

__all__ = ["BashOperator"]
