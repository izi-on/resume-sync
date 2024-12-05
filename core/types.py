from typing import Any, Callable

Parser = Callable[[str], dict]
Uploader = Callable[[dict], dict]
Extractor = Callable[[Any], str]
