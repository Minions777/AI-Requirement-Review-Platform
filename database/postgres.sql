-- 需求评审报告表：用于存储评审输出和时间戳。
CREATE TABLE IF NOT EXISTS requirement_review_reports (
    -- 自增主键。
    id SERIAL PRIMARY KEY,
    -- 飞书文档 ID。
    doc_id VARCHAR(128) NOT NULL,
    -- 评审报告正文。
    report_text TEXT NOT NULL,
    -- 创建时间（数据库默认当前时间）。
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
