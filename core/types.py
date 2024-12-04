from typing import Any, Callable

JsonStr = str
Parser = Callable[[str], dict]
Uploader = Callable[[JsonStr], JsonStr]
Extractor = Callable[[Any], str]
