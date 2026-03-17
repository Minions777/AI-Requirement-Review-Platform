def parse_doc(doc: dict) -> dict:
    # 初始化结构化字段，便于后续评审流程统一消费。
    sections = {
        "background": "",
        "features": [],
        "rules": [],
        "flows": [],
        "raw": doc,
    }

    # 遍历飞书文档块并按关键词粗分类。
    blocks = doc.get("blocks", [])
    for block in blocks:
        text = block.get("text", "").strip()
        if not text:
            continue

        if "背景" in text:
            sections["background"] += f"{text}\n"
        if "功能" in text:
            sections["features"].append(text)
        if "规则" in text:
            sections["rules"].append(text)
        if "流程" in text:
            sections["flows"].append(text)

    # 提供简短摘要，作为向量检索的种子文本。
    sections["summary"] = (
        f"背景: {sections['background']}\n"
        f"功能数: {len(sections['features'])}, "
        f"规则数: {len(sections['rules'])}, "
        f"流程数: {len(sections['flows'])}"
    )
    return sections
