import requests

from backend.config import FEISHU_ACCESS_TOKEN


class FeishuDocError(RuntimeError):
    """Raised when the Feishu Doc API call fails."""


def get_doc_content(doc_id: str) -> dict:
    # 使用飞书开放平台 Docx 原始内容接口拉取文档。
    url = f"https://open.feishu.cn/open-apis/docx/v1/documents/{doc_id}/raw_content"
    headers = {"Authorization": f"Bearer {FEISHU_ACCESS_TOKEN}"}

    # 先校验 HTTP 层状态码。
    response = requests.get(url, headers=headers, timeout=30)
    response.raise_for_status()

    # 再校验飞书业务层 code 字段。
    payload = response.json()
    if payload.get("code") not in (None, 0):
        raise FeishuDocError(payload.get("msg", "Failed to fetch Feishu doc"))

    return payload.get("data", payload)
