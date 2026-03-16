import requests

from backend.config import DIFY_API_KEY, DIFY_URL


def run_dify_workflow(doc: dict, context: list[str]) -> dict:
    headers = {
        "Authorization": f"Bearer {DIFY_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "inputs": {
            "requirement_doc": doc,
            "history_context": "\n".join(context),
        },
        "response_mode": "blocking",
        "user": "feishu-webhook",
    }

    response = requests.post(DIFY_URL, json=payload, headers=headers, timeout=60)
    response.raise_for_status()
    return response.json()
