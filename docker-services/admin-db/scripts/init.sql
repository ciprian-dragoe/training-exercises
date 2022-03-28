CREATE TABLE IF NOT EXISTS users (
    id        INTEGER PRIMARY KEY NOT NULL,
    name      VARCHAR(100)        NOT NULL
);

CREATE TABLE IF NOT EXISTS exercises (
    id        INTEGER PRIMARY KEY NOT NULL,
    name      VARCHAR(100)        NOT NULL,
    user_id   INTEGER,
    CONSTRAINT fk_users
        FOREIGN KEY(user_id)
            REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS files (
    id        INTEGER PRIMARY KEY NOT NULL,
    name      VARCHAR(100)        NOT NULL,
    exercise_id   INTEGER,
    CONSTRAINT fk_exercises
        FOREIGN KEY(exercise_id)
            REFERENCES exercises(id)
);
