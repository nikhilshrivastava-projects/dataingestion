-- Create table
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    date TEXT
);

-- Insert data
INSERT INTO users (id, name, age, date) VALUES (1, 'John Doe', 29, '2023-09-28');
INSERT INTO users (id, name, age, date) VALUES (2, 'Jane Smith', 34, '2023-09-27');
INSERT INTO users (id, name, age, date) VALUES (3, 'Mary Johnson', 25, '2023-09-26');