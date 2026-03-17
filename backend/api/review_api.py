from fastapi import APIRouter
from pydantic import BaseModel

from backend.services.report_service import build_review_report
from backend.services.review_service import review_requirement

# 人工触发评审接口，方便在没有飞书事件时直接调试。
router = APIRouter(prefix="/review", tags=["review"])


class ReviewPayload(BaseModel):
    # 文档标识，默认值用于手工输入场景。
    doc_id: str = "manual-input"
    # 可选标题；为空时回落到 doc_id。
    title: str | None = None
    # 需求正文。
    content: str


@router.post("")
def run_review(payload: ReviewPayload) -> dict:
    # 组装统一的结构化输入，和飞书入口保持一致。
    structured_doc = {
        "title": payload.title or payload.doc_id,
        "raw": payload.content,
    }
    # 执行需求评审。
    review = review_requirement(structured_doc)
    # 生成可直接发送/存档的评审报告文本。
    report = build_review_report(doc_id=payload.doc_id, review=review)
    return {"review": review, "report": report}
