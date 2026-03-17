from openai import OpenAI

from backend.config import OPENAI_API_KEY

# OpenAI 客户端用于把需求文本转为向量。
client = OpenAI(api_key=OPENAI_API_KEY)


def embed(text: str) -> list[float]:
    # 使用官方 embedding 模型生成语义向量。
    response = client.embeddings.create(model="text-embedding-3-large", input=text)
    # 当前请求只输入一段文本，因此取第一条结果。
    return response.data[0].embedding
