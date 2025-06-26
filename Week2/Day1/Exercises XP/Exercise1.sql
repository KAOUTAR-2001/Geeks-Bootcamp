-- sql
-- Create the items table
CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price NUMERIC(10, 2) NOT NULL
);

-- Create the customers table
CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL
);

-- Insert data into items
INSERT INTO items (name, price) VALUES
('Small Desk', 100),
('Large Desk', 300),
('Fan', 80);

-- Insert data into customers
INSERT INTO customers (first_name, last_name) VALUES
('Greg', 'Jones'),
('Sandra', 'Jones'),
('Scott', 'Scott'),
('Trevor', 'Green'),
('Melanie', 'Johnson');

--All the items
SELECT * FROM items;

--All the items with a price above 80 (80 not included)
SELECT * FROM items
WHERE price > 80;

--All the items with a price below 300 (300 included)
SELECT * FROM items
WHERE price <= 300;

--All customers whose last name is ‘Smith’ (Expected: 0 rows)
SELECT * FROM customers
WHERE last_name = 'Smith';

--All customers whose last name is ‘Jones’
SELECT * FROM customers
WHERE last_name = 'Jones';

--All customers whose firstname is not ‘Scott’
SELECT * FROM customers
WHERE first_name <> 'Scott';