-- Titanic passengers database schema
CREATE TABLE passengers (
    passenger_id INTEGER PRIMARY KEY,
    survived INTEGER CHECK (survived IN (0,1)),
    pclass INTEGER CHECK (pclass IN (1,2,3)),
    name TEXT,
    sex TEXT CHECK (sex IN ('male', 'female')),
    age REAL,
    sibsp INTEGER DEFAULT 0,
    parch INTEGER DEFAULT 0,
    ticket TEXT,
    fare REAL,
    cabin TEXT,
    embarked TEXT CHECK (embarked IN ('C', 'Q', 'S'))
);

-- Indexes for faster queries
CREATE INDEX idx_pclass ON passengers(pclass);
CREATE INDEX idx_sex ON passengers(sex);
CREATE INDEX idx_survived ON passengers(survived);
