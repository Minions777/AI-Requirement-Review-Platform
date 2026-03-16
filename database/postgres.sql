CREATE TABLE IF NOT EXISTS requirement_review_reports (
    id SERIAL PRIMARY KEY,
    doc_id VARCHAR(128) NOT NULL,
    report_text TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
