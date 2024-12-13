from abc import ABC
from core.config import RESUME_KEY
from core.repositories.abc import MongoRepository, IRepository


class ResumeRepository(IRepository, ABC):
    def save_resume(self, resume: dict):
        self.save(resume)


class MongoResumeRepository(MongoRepository, ResumeRepository):
    def get_db(self) -> str:
        return RESUME_KEY

    def get_collection(self) -> str:
        return RESUME_KEY
