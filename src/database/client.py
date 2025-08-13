from abc import ABC, abstractmethod
from typing import Any, List, Optional, Tuple

class Client(ABC):
    def __init__(self, **params):
        self.connection = None
        self.params = params
        self.connect(**params)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    @abstractmethod
    def connect(self, **kwargs) -> None:
        pass

    @abstractmethod
    def close(self) -> None:
        pass

    @abstractmethod
    def execute(self, query: str, params: Optional[Tuple] = None) -> Any:
        pass

    @abstractmethod
    def fetch_all(self, query: str, params: Optional[Tuple] = None) -> List[Tuple]:
        pass

    @abstractmethod
    def fetch_one(self, query: str, params: Optional[Tuple] = None) -> Any:
        pass