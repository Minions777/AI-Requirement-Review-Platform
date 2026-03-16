from datetime import datetime

from backend.utils.feishu_bot import send_message


def build_review_report(doc_id: str, review: dict) -> str:
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%SZ")
    return (
        f"需求评审完成\n"
        f"文档ID: {doc_id}\n"
        f"时间: {timestamp}\n"
        f"结果: {review}"
    )


def send_review_report(review_report: str) -> None:
    send_message(review_report)
