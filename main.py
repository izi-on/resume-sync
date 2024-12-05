from core.config import PROMPT, RESUME_KEY
from core.database.mongodb import mongo_client
from core.extractors import get_file_extractor
from core.parsers import get_llm_file_parser
from core.repositories.resume_repository import MongoResumeRepository
from core.services.resume_service import ResumeService
from core.uploaders import get_pretty_printer
from core.utils import get_full_filename, pipeline
from dotenv import load_dotenv

load_dotenv()

resume_service = ResumeService(MongoResumeRepository(mongo_client()))

resume_parse_and_upload = pipeline(
    get_file_extractor(get_full_filename(RESUME_KEY)),
    get_llm_file_parser(PROMPT),
    get_pretty_printer(),  # for debugging or printing
    resume_service.get_uploader(),
)

if __name__ == "__main__":
    resume_parse_and_upload(
        None
    )  # None is passed because pipeline creates a function that requires an argument
