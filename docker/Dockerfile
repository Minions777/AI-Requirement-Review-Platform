# 基础镜像：Python 3.11 轻量版。
FROM python:3.11-slim

# 容器工作目录。
WORKDIR /app

# 安装依赖（先复制 requirements 以利用构建缓存）。
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# 拷贝项目代码。
COPY . .

# 暴露 FastAPI 服务端口。
EXPOSE 8000

# 启动命令：运行 Uvicorn。
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
