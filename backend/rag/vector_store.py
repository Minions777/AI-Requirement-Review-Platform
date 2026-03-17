from functools import lru_cache

from pymilvus import Collection, connections

from backend.config import MILVUS_COLLECTION, MILVUS_URI


@lru_cache(maxsize=1)
def _get_collection() -> Collection:
    """Lazily initialize Milvus connection and collection handle."""
    # 建立 Milvus 连接并返回集合句柄；配合 lru_cache 只初始化一次。
    connections.connect(uri=MILVUS_URI)
    return Collection(MILVUS_COLLECTION)


def search_similar(vector: list[float], limit: int = 5):
    # 读取（或懒加载）集合。
    collection = _get_collection()
    # 进行向量检索并返回最相似的若干条。
    result = collection.search(
        data=[vector],
        anns_field="embedding",
        param={"metric_type": "COSINE", "params": {"nprobe": 10}},
        limit=limit,
        output_fields=["text"],
    )
    # pymilvus 返回二维结构，这里只取第一条查询向量对应的结果。
    return result[0]
