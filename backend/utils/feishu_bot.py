import requests

from backend.config import FEISHU_BOT_WEBHOOK


def send_message(text: str) -> None:
    # 飞书机器人文本消息格式。
    data = {
        "msg_type": "text",
        "content": {"text": text},
    }
    # 发消息失败不在此处吞掉异常，交给上层处理。
    requests.post(FEISHU_BOT_WEBHOOK, json=data, timeout=15)
