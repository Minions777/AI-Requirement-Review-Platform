import requests

from backend.config import FEISHU_BOT_WEBHOOK


def send_message(text: str) -> None:
    data = {
        "msg_type": "text",
        "content": {"text": text},
    }
    requests.post(FEISHU_BOT_WEBHOOK, json=data, timeout=15)
