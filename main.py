from fastapi import FastAPI, BackgroundTasks, Response, Query
from models import BookAnalyzeRequest, BookAnalyzeResponse, BookStatus, CharacterInteractions, AnalysisState
from utils import get_book_analysis_key, create_book_analysis_key
from client.redis import redis
from book.book_processor import process_book
from fastapi.middleware.cors import CORSMiddleware
from constants import ERROR_TASK_NOT_FOUND
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"], 
)

@app.post("/analyze")
def start_analysis(book: BookAnalyzeRequest, background_tasks: BackgroundTasks, mock: int = Query(0) ):
    key = create_book_analysis_key()
    
    redis.set(key.redis_key, 
              BookStatus(task_id=key.task_id,status=AnalysisState.pending).model_dump_json())
    
    background_tasks.add_task(process_book, book.book_id, key.task_id, mock)

    return BookAnalyzeResponse(task_id=key.task_id)

@app.get("/status/{task_id}")
def get_status(task_id: str):
    key = get_book_analysis_key(task_id)
    
    data = redis.get(key.redis_key)
    
    if not data:
        return BookStatus(task_id=task_id, error=ERROR_TASK_NOT_FOUND)
    
    return BookStatus.model_validate_json(data)