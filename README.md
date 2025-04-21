### Overview

This is the backend for analyzing a book and generating a character interaction graph using a language model (LLM). It uses a task-based architecture with Redis for async processing.

### Tech Stack

- **FastAPI** – Web framework
- **Redis** – Task/result storage
- **Uvicorn** – ASGI server

### API Endpoints

| Method | Endpoint            | Description |
|--------|---------------------|-------------|
| POST   | `/analyze`          | Starts a background task. Returns a `task_id`. Accepts `book_id` and optional `mock=1`. |
| GET    | `/status/{task_id}` | Returns status/result of the analysis task. |

### Architecture

https://wasinaseer.notion.site/Book-Analyzer-Project-Gutenberg-1dcddb6ac91c80aa8d20d0f04dcbe770

---

### Getting Started

#### 1. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
```

#### 1.  Install dependencies
```
pip install -r requirements.txt
```

#### 1. Start Redis (Docker example)
```
docker run -d -p 6379:6379 redis
```

#### 4. Run the app
```
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```
