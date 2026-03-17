import os

# 飞书开放平台访问令牌。
FEISHU_ACCESS_TOKEN = os.getenv("FEISHU_ACCESS_TOKEN", "")
# 飞书机器人 webhook 地址。
FEISHU_BOT_WEBHOOK = os.getenv("FEISHU_BOT_WEBHOOK", "")
# Dify API Key。
DIFY_API_KEY = os.getenv("DIFY_API_KEY", "")
# Dify 工作流运行端点。
DIFY_URL = os.getenv("DIFY_URL", "http://dify/api/workflows/run")
# OpenAI API Key（用于 embedding）。
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
# Milvus 服务地址。
MILVUS_URI = os.getenv("MILVUS_URI", "http://milvus:19530")
# Milvus 需求向量集合名。
MILVUS_COLLECTION = os.getenv("MILVUS_COLLECTION", "requirements")
