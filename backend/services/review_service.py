from backend.services.dify_service import run_dify_workflow
from backend.services.vector_search_service import retrieve_similar_requirements


def review_requirement(structured_doc: dict) -> dict:
    context = retrieve_similar_requirements(structured_doc)
    return run_dify_workflow(structured_doc, context)
