import logging


def get_logger(name: str) -> logging.Logger:
    # 配置全局日志格式与级别（重复调用 basicConfig 时后续调用会被忽略）。
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
    )
    # 按模块名返回 logger。
    return logging.getLogger(name)
