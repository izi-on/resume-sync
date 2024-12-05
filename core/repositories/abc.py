from abc import ABC, abstractmethod
from pymongo import MongoClient


class IRepository(ABC):
    @abstractmethod
    def save(self, value: dict):
        pass


class MongoRepository(IRepository, ABC):
    def __init__(self, client: MongoClient):
        self.client = client[self.get_db()][self.get_collection()]

    def save(self, value: dict):
        self.client.insert_one(value)

    @abstractmethod
    def get_db(self) -> str:
        pass

    @abstractmethod
    def get_collection(self) -> str:
        pass
