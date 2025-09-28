CREATE TABLE animals(
	animal_id INT AUTO_INCREMENT PRIMARY KEY,
    owner_id VARCHAR (14) NOT NULL,
    animal_name VARCHAR (50) NOT NULL,
    animal_specie VARCHAR(50) NOT NULL,
    animal_race VARCHAR(50) NOT NULL,
    animal_birthday DATE,
    FOREIGN KEY (owner_id) REFERENCES customer(customer_id) ON DELETE CASCADE
);

