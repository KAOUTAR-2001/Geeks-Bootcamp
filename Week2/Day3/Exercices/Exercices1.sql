SELECT *FROM language



SELECT f.title, f.description, l.name AS language_name
FROM film f
JOIN language l ON f.language_id = l.language_id;




SELECT f.title, f.description, l.name AS language_name
FROM language l
LEFT JOIN film f ON l.language_id = f.language_id;




CREATE TABLE new_film (
id serial Primary key,
name varchar(255) not null
);



insert into new_film(name) values
('The Matrix'),
('Inception'),
('Titanic');



create table customer_review(
review_id SERIAL PRIMARY KEY,
    film_id INT REFERENCES new_film(id) ON DELETE CASCADE,
    language_id INT REFERENCES language(language_id),
    title VARCHAR(255) NOT NULL,
    score INT CHECK (score BETWEEN 1 AND 10),
    review_text TEXT,
    last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



insert into customer_review (film_id,language_id,title,score,review_text) values
(1, 1, 'Amazing Sci-Fi', 9, 'One of the best sci-fi movies ever!'),
(2, 2, 'Mind-Blowing', 10, 'Inception was an absolute masterpiece.');


DELETE from new_film where id =1;
select *from new_film
