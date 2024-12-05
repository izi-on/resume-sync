from abc import ABC, abstractmethod
from typing import Any

__all__ = ["IUploader"]


class IUploader(ABC):
    @abstractmethod
    def get_uploader(self, value: Any):
        pass
