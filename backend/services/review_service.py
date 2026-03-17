from backend.services.dify_service import run_dify_workflow
from backend.services.vector_search_service import retrieve_similar_requirements


def review_requirement(structured_doc: dict) -> dict:
    # 接收结构化需求文档，执行完整的评审流水线。
    # 先走向量检索召回历史需求，给 LLM 提供可参考的上下文。
    context = retrieve_similar_requirements(structured_doc)
    # 再调用 Dify 工作流（底层连接 LLM）生成评审结论。
    return run_dify_workflow(structured_doc, context)
