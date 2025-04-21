from pydantic import BaseModel
from typing import List, Optional
from typing import List, Optional
from enum import Enum

class BookAnalyzeRequest(BaseModel):
    book_id: int
    
class BookAnalyzeResponse(BaseModel):
    task_id: str

class Interaction(BaseModel):
    name: str
    count: int

class CharacterInteraction(BaseModel):
    character_name: str
    interacted_with: Optional[List[Interaction]]
    total_interactions: Optional[int] = 0
    
class CharacterInteractions(BaseModel):
    character_interactions: Optional[List[CharacterInteraction]] = None

class AnalysisState(str, Enum):
    in_progress  = "in_progress"
    done = "done"
    error = "error"
    pending = "pending"
    

class BookStatus(BaseModel):
    task_id: str
    status: str = AnalysisState
    progress: int = 0
    error: Optional[str] = None
    result: Optional[CharacterInteractions] = None
    
class BookAnalysisKey(BaseModel):
    redis_key: str
    task_id: str
    
