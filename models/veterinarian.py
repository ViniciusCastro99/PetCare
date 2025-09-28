class Veterinarian:
    def __init__(self, professionalRegistration, name, specialty):
        self._professionalRegistration = professionalRegistration
        self._name = name
        self._specialty = specialty
        self._appointments = None

    def register_veterinarian(self, conn):
        cursor = conn.cursor()
        sql = """ 
            INSERT INTO veterinarians (professional_registration, veterinarian_name, specialty)
            VALUES (%s, %s, %s)  
            """
        val = (
            self._professionalRegistration,
            self._name,
            self._specialty
        )
        cursor.execute(sql, val)
        conn.commit()
        cursor.close()

    def update_data(conn):
        cursor = conn.cursor 
        #TERMINAR FUNÇÃO DE EDIÇÃO DE DADOS

    def list_specialty():
        pass
    def appointment_history():
        pass

    