/* creating the salesdb.Sales table
along with its columns and respective data types
(primary and foreign key constraints were not used
because of time and having constraints make it more
difficult to continuously test with inserting/updating/deleting data) */
CREATE TABLE IF NOT EXISTS salesdb.Sales(
    sales_id INT NOT NULL,
    poster_content VARCHAR(100) NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(2,1) NOT NULL,
    email VARCHAR(100) NOT NULL,
    sales_rep VARCHAR(100) NOT NULL,
    promo_code VARCHAR(50) NOT NULL,
    poster_type VARCHAR(50) NOT NULL,
    poster_number INT NOT NULL
);