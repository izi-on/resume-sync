from dotenv import load_dotenv
from core.config import PROMPT, RESUME_KEY
from core.extractors import get_file_extractor
from core.parsers import get_llm_file_parser
from core.uploaders import get_redis_uploader, get_pretty_printer
from core.database import redis_client
from core.utils import get_full_filename, pipeline, to_json_str

load_dotenv()

resume_dict_getter = pipeline(
    get_file_extractor(get_full_filename(RESUME_KEY)),
    get_llm_file_parser(PROMPT),
    to_json_str,
    get_pretty_printer(),
    get_redis_uploader(redis_client(), RESUME_KEY),
)

if __name__ == "__main__":
    resume_dict_getter(None)
