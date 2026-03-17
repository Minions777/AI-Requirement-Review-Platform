from fastapi import FastAPI

from backend.api.feishu_webhook import router as feishu_router
from backend.api.review_api import router as review_router

# FastAPI 作为 Python 服务入口，分别挂载飞书回调与人工触发评审接口。
app = FastAPI(title="AI Requirement Review")

app.include_router(feishu_router)
app.include_router(review_router)


@app.get("/")
def health() -> dict[str, str]:
    # 健康检查，便于容器/网关探活。
    return {"status": "running"}
