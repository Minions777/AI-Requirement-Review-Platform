from datetime import datetime

from backend.utils.feishu_bot import send_message


def build_review_report(doc_id: str, review: dict) -> str:
    # 统一使用 UTC 时间，方便多时区部署。
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%SZ")
    # 输出可直接发送到飞书群的纯文本报告。
    return (
        f"需求评审完成\n"
        f"文档ID: {doc_id}\n"
        f"时间: {timestamp}\n"
        f"结果: {review}"
    )


def send_review_report(review_report: str) -> None:
    # 通过飞书机器人发送评审报告。
    send_message(review_report)
