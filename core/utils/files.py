import os

__all__ = ["get_full_filename"]


def get_full_filename(partial_name: str):
    files = os.listdir()
    partial_name_lower = partial_name.lower()
    for file in files:
        if ".".join(file.lower().split(".")[:-1]) == partial_name_lower:
            return file

    # If no file is found
    raise FileNotFoundError(
        f"No file matching '{partial_name}' found in current directory"
    )
