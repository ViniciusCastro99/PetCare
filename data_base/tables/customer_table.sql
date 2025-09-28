USE petcare;

CREATE TABLE customer (
    customer_id VARCHAR(14) NOT NULL PRIMARY KEY,
    customer_name VARCHAR(150) NOT NULL,
    customer_phone VARCHAR(20) NOT NULL,
    address_street VARCHAR(200),
    address_neighborhood VARCHAR(80),
    address_number VARCHAR(6),
    address_city VARCHAR(60) NOT NULL,
    address_state VARCHAR(2) NOT NULL,
    address_postal_code VARCHAR(9) NOT NULL,
    address_country varchar(20),
    address_complement VARCHAR(50),
    birth_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);