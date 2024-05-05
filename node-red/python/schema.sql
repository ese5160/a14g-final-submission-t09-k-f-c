CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS inventories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_name INTEGER NOT NULL,
    food_name TEXT NOT NULL,
    type TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    expiration DATE NOT NULL,
    FOREIGN KEY(user_name) REFERENCES users(name)
);

-- Default user
INSERT INTO users (id, name) VALUES (0, 'DEFAULT');

--
INSERT INTO inventories (user_name, food_name, type, quantity, expiration)
VALUES ('DEFAULT', 'Apple', 'fruit', 3, '2024-05-01');