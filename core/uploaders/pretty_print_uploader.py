from pprint import pprint
from typing import Any

from core.types import Uploader

__all__ = ["get_pretty_printer"]


def get_pretty_printer() -> Uploader:
    def printer(data: Any) -> Any:
        print(type(data))
        print("---------------")
        pprint(data)
        return data

    return printer
