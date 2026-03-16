from fastapi import APIRouter, HTTPException, Request

from backend.services.doc_parser import parse_doc
from backend.services.feishu_doc_service import get_doc_content
from backend.services.report_service import build_review_report, send_review_report
from backend.services.review_service import review_requirement

router = APIRouter()


@router.post("/feishu/webhook")
async def feishu_event(req: Request) -> dict[str, str]:
    data = await req.json()
    doc_id = data.get("doc_id")
    if not doc_id:
        raise HTTPException(status_code=400, detail="Missing doc_id")

    doc_content = get_doc_content(doc_id)
    structured_doc = parse_doc(doc_content)
    review = review_requirement(structured_doc)
    report = build_review_report(doc_id=doc_id, review=review)
    send_review_report(report)

    return {"status": "ok"}
