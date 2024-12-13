from core.repositories.resume_repository import ResumeRepository
from core.types import Uploader
from core.uploaders.abc import IUploader


class ResumeService(IUploader):
    def __init__(self, repository: ResumeRepository):
        self.repository = repository

    def upload(self, resume: dict):
        self.repository.save_resume(resume)

    def get_uploader(self) -> Uploader:
        def uploader(resume: dict):
            self.upload(resume)
            return resume

        return uploader
