from fastapi import APIRouter
from pydantic import BaseModel

from backend.services.report_service import build_review_report
from backend.services.review_service import review_requirement

router = APIRouter(prefix="/review", tags=["review"])


class ReviewPayload(BaseModel):
    doc_id: str = "manual-input"
    title: str | None = None
    content: str


@router.post("")
def run_review(payload: ReviewPayload) -> dict:
    structured_doc = {
        "title": payload.title or payload.doc_id,
        "raw": payload.content,
    }
    review = review_requirement(structured_doc)
    report = build_review_report(doc_id=payload.doc_id, review=review)
    return {"review": review, "report": report}
