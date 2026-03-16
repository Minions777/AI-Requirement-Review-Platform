# AI Requirement Review Platform

基于 **Python + Dify + LLM + 向量检索 + 飞书机器人** 的需求评审 Agent。

## 启动

```bash
pip install -r requirements.txt
uvicorn backend.main:app --reload
```

## 目录

- `backend/`: FastAPI 与系统集成代码
- `dify/`: Workflow 与 Prompt
- `database/`: PostgreSQL 初始化 SQL
- `docker/`: 容器部署文件
