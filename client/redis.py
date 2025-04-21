import redis
import os
from dotenv import load_dotenv

load_dotenv()
redis = redis.Redis(host=os.getenv("REDIS_URL"), port=6379, decode_responses=True)