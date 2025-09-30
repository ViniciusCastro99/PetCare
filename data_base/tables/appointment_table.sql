CREATE TABLE appointments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_animal INT NOT NULL,
    id_veterinarian VARCHAR(11) NOT NULL,
    appointment_date DATE NOT NULL,
    appointment_time TIME NOT NULL,
    appointment_description TEXT NOT NULL,
    appointment_status ENUM('scheduled', 'done', 'canceled') DEFAULT 'scheduled',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (id_animal) REFERENCES animals(animal_id),
    FOREIGN KEY (id_veterinarian) REFERENCES veterinarians(professional_registration)
);
