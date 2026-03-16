import requests

from backend.config import FEISHU_ACCESS_TOKEN


class FeishuDocError(RuntimeError):
    """Raised when the Feishu Doc API call fails."""


def get_doc_content(doc_id: str) -> dict:
    url = f"https://open.feishu.cn/open-apis/docx/v1/documents/{doc_id}/raw_content"
    headers = {"Authorization": f"Bearer {FEISHU_ACCESS_TOKEN}"}

    response = requests.get(url, headers=headers, timeout=30)
    response.raise_for_status()

    payload = response.json()
    if payload.get("code") not in (None, 0):
        raise FeishuDocError(payload.get("msg", "Failed to fetch Feishu doc"))

    return payload.get("data", payload)
