from client.redis import redis
from book.book_analyzer import analyze_book_using_llm
from utils import get_book_analysis_key, download_book_content, mock_response
from models import BookStatus, CharacterInteractions, AnalysisState
    
def process_book(book_id: int, task_id: str, is_mock: int):
    redis_key = get_book_analysis_key(task_id).redis_key
    try:
        redis.set(redis_key, 
                  BookStatus(task_id=task_id,
                             status=AnalysisState.in_progress)
                  .model_dump_json())

        book_text = download_book_content(book_id)
        result = analyze_book_using_llm(book_text) if is_mock == 0 else mock_response()
        redis.set(redis_key, 
                  BookStatus(task_id=task_id,
                             status=AnalysisState.done,
                             progress=100,
                             result=CharacterInteractions(**result))
                  .model_dump_json())

    except Exception as e:
        redis.set(redis_key, 
            BookStatus(task_id=task_id,
                        status=AnalysisState.error,
                        progress=100,
                        error=str(e))
            .model_dump_json())


