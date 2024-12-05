import os
from pymongo import MongoClient

__all__ = ["mongo_client"]

mongodb_instance = None


def mongo_client() -> MongoClient:
    global mongodb_instance
    if not mongodb_instance:
        mongodb_instance = MongoClient(os.environ["MONGO_PUBLIC_URL"])
    return mongodb_instance
