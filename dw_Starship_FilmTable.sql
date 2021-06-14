/* creating the dw.Starship_Film table
along with its columns and respective data types
(primary and foreign key constraints were not used
because of time and having constraints make it more
difficult to continuously test with inserting/updating/deleting data) */
CREATE TABLE IF NOT EXISTS dw.Starship_Film(
    starship_film_id INT NOT NULL,
    starship_name VARCHAR(100) NOT NULL,
    film_appeared VARCHAR(100) NOT NULL,
    film_made DATE NOT NULL
);