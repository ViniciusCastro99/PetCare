CREATE TABLE veterinarians (
	professional_registration VARCHAR(11) PRIMARY KEY,
    user_id INT NOT NULL,
    veterinarian_name VARCHAR(150) NOT NULL,
    specialty VARCHAR(150) NOT NULL,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY(user_id) REFERENCES users(user_id)
    );
    
    