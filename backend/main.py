from fastapi import FastAPI

from backend.api.feishu_webhook import router as feishu_router
from backend.api.review_api import router as review_router

app = FastAPI(title="AI Requirement Review")

app.include_router(feishu_router)
app.include_router(review_router)


@app.get("/")
def health() -> dict[str, str]:
    return {"status": "running"}
