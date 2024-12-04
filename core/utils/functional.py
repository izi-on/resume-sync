from typing import Callable
from functools import reduce

__all__ = ["pipeline"]


def pipeline(*functions: Callable) -> Callable:
    return lambda x: reduce(lambda v, f: f(v), functions, x)
