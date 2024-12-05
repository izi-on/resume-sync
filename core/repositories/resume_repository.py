from abc import ABC, abstractmethod
from core.config import RESUME_KEY
from core.repositories.abc import MongoRepository, IRepository


class IResumeRepository(IRepository, ABC):
    @abstractmethod
    def save_resume(self, resume: dict):
        pass


class MongoResumeRepository(MongoRepository, IResumeRepository):
    def get_db(self) -> str:
        return RESUME_KEY

    def get_collection(self) -> str:
        return RESUME_KEY

    def save_resume(self, resume: dict):
        self.save(resume)
