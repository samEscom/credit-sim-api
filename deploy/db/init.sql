DROP TABLE IF EXISTS credit_simulation;

CREATE TABLE credit_simulation (
    id TEXT PRIMARY KEY,
    amount NUMERIC NOT NULL,
    annual_rate NUMERIC NOT NULL,
    months INTEGER NOT NULL,
    risk_score VARCHAR(20) NULL,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NULL
);
