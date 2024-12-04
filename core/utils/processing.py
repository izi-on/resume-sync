__all__ = ["to_json_str"]


import json


def to_json_str(data: dict):
    return json.dumps(data, indent=4, sort_keys=True)
