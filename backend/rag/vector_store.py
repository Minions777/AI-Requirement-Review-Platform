from functools import lru_cache

from pymilvus import Collection, connections

from backend.config import MILVUS_COLLECTION, MILVUS_URI


@lru_cache(maxsize=1)
def _get_collection() -> Collection:
    """Lazily initialize Milvus connection and collection handle."""
    connections.connect(uri=MILVUS_URI)
    return Collection(MILVUS_COLLECTION)


def search_similar(vector: list[float], limit: int = 5):
    collection = _get_collection()
    result = collection.search(
        data=[vector],
        anns_field="embedding",
        param={"metric_type": "COSINE", "params": {"nprobe": 10}},
        limit=limit,
        output_fields=["text"],
    )
    return result[0]
