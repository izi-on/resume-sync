from pprint import pprint

from core.types import JsonStr, Uploader

__all__ = ["get_pretty_printer"]


def get_pretty_printer() -> Uploader:
    def printer(data: JsonStr) -> JsonStr:
        print(type(data))
        print("---------------")
        pprint(data)
        return data

    return printer
