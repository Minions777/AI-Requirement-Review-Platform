from pymilvus import Collection, connections

from backend.config import MILVUS_COLLECTION, MILVUS_URI

connections.connect(uri=MILVUS_URI)
collection = Collection(MILVUS_COLLECTION)


def search_similar(vector: list[float], limit: int = 5):
    result = collection.search(
        data=[vector],
        anns_field="embedding",
        param={"metric_type": "COSINE", "params": {"nprobe": 10}},
        limit=limit,
        output_fields=["text"],
    )
    return result[0]
