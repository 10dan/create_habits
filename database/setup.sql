CREATE USER habit_user WITH PASSWORD 'password';
CREATE DATABASE create_habits;
GRANT ALL PRIVILEGES ON DATABASE create_habits TO habit_user;

CREATE TABLE habits (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description VARCHAR(255)
);

CREATE TABLE habit_log (
    log_id SERIAL PRIMARY KEY,
    habit_id INT REFERENCES habits(id),
    date DATE NOT NULL,
    status BOOLEAN NOT NULL,
    value FLOAT
);

INSERT INTO habits (name, description) VALUES
('Meditation', 'Practice of mindfulness or concentration'),
('Eat No Sugar', 'Avoiding sugar intake'),
('Workout', 'Physical exercise routine'),
('Read', 'Reading books or articles');

INSERT INTO habit_log (habit_id, date, status, value) VALUES
(1, CURRENT_DATE, TRUE, 20.0);  -- Use 20 for INTEGER type
