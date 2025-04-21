
from uuid import uuid4
from models import BookAnalysisKey
from constants import ERROR_BOOK_NOT_FOUND_OR_NOT_DOWNLOADED
import tiktoken
import requests

def get_book_analysis_key(task_id: str) -> str:
    return BookAnalysisKey(redis_key=f"book_analysis:{task_id}", task_id=task_id)

def create_book_analysis_key() -> str:
    task_id = str(uuid4())
    return get_book_analysis_key(task_id)

def download_book_content(book_id: int) -> str:
    content_url = f"https://www.gutenberg.org/files/{book_id}/{book_id}-0.txt"
    response = requests.get(content_url)
    if response.status_code == 200:
        return response.text
    raise Exception(ERROR_BOOK_NOT_FOUND_OR_NOT_DOWNLOADED)

import json

def mock_response():
    result = """{'character_interactions': [{'character_name': 'David Innes', 'interacted_with': [{'name': 'Perry', 'count': 23}, {'name': 'Dian the Beautiful', 'count': 17}, {'name': 'Ghak the Hairy One', 'count': 10}, {'name': 'Hooja the Sly One', 'count': 8}], 'total_interactions': 58}, {'character_name': 'Perry', 'interacted_with': [{'name': 'David Innes', 'count': 23}, {'name': 'Mahars', 'count': 12}, {'name': 'Sagoths', 'count': 8}], 'total_interactions': 43}, {'character_name': 'Dian the Beautiful', 'interacted_with': [{'name': 'David Innes', 'count': 17}, {'name': 'Ghak the Hairy One', 'count': 5}, {'name': 'Hooja the Sly One', 'count': 5}], 'total_interactions': 27}, {'character_name': 'Ghak the Hairy One', 'interacted_with': [{'name': 'David Innes', 'count': 10}, {'name': 'Dian the Beautiful', 'count': 5}, {'name': 'Perry', 'count': 5}], 'total_interactions': 20}, {'character_name': 'Hooja the Sly One', 'interacted_with': [{'name': 'David Innes', 'count': 8}, {'name': 'Dian the Beautiful', 'count': 5}, {'name': 'Ghak the Hairy One', 'count': 3}], 'total_interactions': 16}, {'character_name': 'Mahars', 'interacted_with': [{'name': 'Perry', 'count': 12}, {'name': 'Sagoths', 'count': 10}, {'name': 'Slaves', 'count': 20}], 'total_interactions': 42}]}"""
    fixed_json = result.replace("'", '"')
    return json.loads(fixed_json)