drop table habit;
CREATE TABLE habit (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description VARCHAR(255),
    display_colour varchar(255)
);

drop table habit_log;
CREATE TABLE habit_log (
    log_id SERIAL PRIMARY KEY,
    habit_id INT REFERENCES habit(id),
    date DATE NOT NULL,
    status BOOLEAN NOT NULL,
    value FLOAT
);
ALTER TABLE habit_log
ADD CONSTRAINT habit_log_unique UNIQUE (habit_id, date);

INSERT INTO habit (habit_id, name, description, display_colour) VALUES
('Meditation', 'Practice of mindfulness or concentration', '#57c27e'),
('Eat No Sugar', 'Avoiding sugar intake', '#d68b22'),
('Workout', 'Physical exercise routine', '#3c74b5'),
('Read', 'Reading books or articles', '#99207f');

INSERT INTO habit_log (habit_id, date, status, value) VALUES
(1,CURRENT_DATE, TRUE, 20.0),
(1,'2023-12-17', TRUE, 20.0);