from backend.rag.embedding_service import embed
from backend.rag.vector_store import search_similar


def retrieve_similar_requirements(structured_doc: dict, top_k: int = 5) -> list[str]:
    # 优先使用 summary 进行召回；没有则退化为全文字符串。
    seed_text = structured_doc.get("summary") or str(structured_doc)
    # 文本向量化。
    vector = embed(seed_text)
    # 在向量库中召回相似需求。
    result = search_similar(vector=vector, limit=top_k)

    # 标准化输出为纯文本列表，方便拼接进 prompt。
    items: list[str] = []
    for hit in result:
        entity = getattr(hit, "entity", None)
        text = None
        if entity and isinstance(entity, dict):
            text = entity.get("text")
        if text is None:
            text = str(hit)
        items.append(text)

    return items
