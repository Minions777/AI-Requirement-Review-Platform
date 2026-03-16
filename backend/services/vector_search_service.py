from backend.rag.embedding_service import embed
from backend.rag.vector_store import search_similar


def retrieve_similar_requirements(structured_doc: dict, top_k: int = 5) -> list[str]:
    seed_text = structured_doc.get("summary") or str(structured_doc)
    vector = embed(seed_text)
    result = search_similar(vector=vector, limit=top_k)

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
