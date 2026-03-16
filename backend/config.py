import os

FEISHU_ACCESS_TOKEN = os.getenv("FEISHU_ACCESS_TOKEN", "")
FEISHU_BOT_WEBHOOK = os.getenv("FEISHU_BOT_WEBHOOK", "")
DIFY_API_KEY = os.getenv("DIFY_API_KEY", "")
DIFY_URL = os.getenv("DIFY_URL", "http://dify/api/workflows/run")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
MILVUS_URI = os.getenv("MILVUS_URI", "http://milvus:19530")
MILVUS_COLLECTION = os.getenv("MILVUS_COLLECTION", "requirements")
