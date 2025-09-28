CREATE TABLE veterinarians (
	professional_registration VARCHAR(11) PRIMARY KEY,
    veterinarian_name VARCHAR(150) NOT NULL,
    specialty VARCHAR(150) NOT NULL,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    )
    
    