import requests

from backend.config import DIFY_API_KEY, DIFY_URL


def run_dify_workflow(doc: dict, context: list[str]) -> dict:
    # Dify API 采用 Bearer Token 鉴权。
    headers = {
        "Authorization": f"Bearer {DIFY_API_KEY}",
        "Content-Type": "application/json",
    }

    # 按 Dify workflow 运行接口定义构造输入参数。
    payload = {
        "inputs": {
            "requirement_doc": doc,
            "history_context": "\n".join(context),
        },
        "response_mode": "blocking",
        "user": "feishu-webhook",
    }

    # 阻塞等待工作流执行完毕并返回结构化结果。
    response = requests.post(DIFY_URL, json=payload, headers=headers, timeout=60)
    response.raise_for_status()
    return response.json()
