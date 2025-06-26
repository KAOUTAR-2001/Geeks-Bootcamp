CREATE TABLE actors (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    age INT CHECK (age >= 0)
);


INSERT INTO actors (first_name,last_name,age) VALUES
('Leonardo', 'DiCaprio', 48),
('Scarlett', 'Johansson', 39),
('Morgan', 'Freeman', 86),
('Emma', 'Watson', 33);



SELECT COUNT(*) FROM actors;




INSERT INTO actors (first_name, last_name, age) 
VALUES (NULL, 'Smith', 40);



SELECT * FROM actors



INSERT INTO actors (first_name, last_name, age) 
VALUES ('', 'Smith', 40);

INSERT INTO actors (first_name, last_name, age) 
VALUES ('John', 'Doe', -5);