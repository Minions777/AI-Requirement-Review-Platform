from fastapi import APIRouter, HTTPException, Request

from backend.services.doc_parser import parse_doc
from backend.services.feishu_doc_service import get_doc_content
from backend.services.report_service import build_review_report, send_review_report
from backend.services.review_service import review_requirement

# 飞书回调路由，无额外前缀，直接暴露 /feishu/webhook。
router = APIRouter()


@router.post("/feishu/webhook")
async def feishu_event(req: Request) -> dict[str, str]:
    # 接收飞书机器人 webhook 推送，提取文档 ID。
    # webhook 请求体通常为 JSON，这里直接解析。
    data = await req.json()
    doc_id = data.get("doc_id")
    if not doc_id:
        raise HTTPException(status_code=400, detail="Missing doc_id")

    # 拉取飞书文档内容并结构化解析。
    doc_content = get_doc_content(doc_id)
    structured_doc = parse_doc(doc_content)

    # 进入需求评审主流程：向量检索 + Dify/LLM。
    review = review_requirement(structured_doc)

    # 组装报告并通过飞书机器人回传。
    report = build_review_report(doc_id=doc_id, review=review)
    send_review_report(report)

    return {"status": "ok"}
