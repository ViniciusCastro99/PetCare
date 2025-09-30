class Veterinarian:
    def __init__(self, professionalRegistration,user_id, name, specialty):
        self._professionalRegistration = professionalRegistration
        self._user_id = user_id
        self._name = name
        self._specialty = specialty
        self._appointments = None

    def register_veterinarian(self, conn):
        cursor = conn.cursor()
        sql = """ 
            INSERT INTO veterinarians (professional_registration, user_id, veterinarian_name, specialty)
            VALUES (%s, %s, %s, %s)  
            """
        val = (
            self._professionalRegistration,
            self._user_id,
            self._name,
            self._specialty
        )
        cursor.execute(sql, val)
        conn.commit()
        cursor.close()

    def update_data(conn):
        cursor = conn.cursor()

        def execute_commit_close_sql(query,value):  
            cursor.execute(query,value)
            conn.commit()
            cursor.close()

        professional_registration = input('\nQual o CRMV do veterinário?\n')
        option = int(input('\nQual dado deseja alterar?\n' \
        '1 - CRMV\n2 - Nome\n3 - Especialidade\n'))
        
        match(option):
            case 1:
                new_professional_registration = input('\nQual o CRMV do veterinário?\n')
                sql = 'UPDATE veterinarians SET professional_registration = %s WHERE professional_registration = %s;'
                val = (new_professional_registration, professional_registration)
                execute_commit_close_sql(sql,val)
            case 2:
                new_name = input('\nDigite o nome:\n')
                sql = 'UPDATE veterinarians SET veterinarian_name = %s WHERE professional_registration = %s;'
                val = (new_name, professional_registration)
                execute_commit_close_sql(sql,val)
            case 3: 
                new_specialty = input('\nDigite a especialidade:\n')
                sql = 'UPDATE veterinarians SET specialty = %s WHERE professional_registration = %s;'
                val = (new_specialty, professional_registration)
                execute_commit_close_sql(sql,val)
    def list_specialty(conn):
        cursor = conn.cursor()
        professional_registration = input('\nQual o CRMV do veterinário?\n')
        
        sql = 'SELECT specialty FROM veterinarians WHERE professional_registration = %s'
        val = (professional_registration,)

        cursor.execute(sql,val)
        result = cursor.fetchall()# Lê **todos os registros retornados pela query** e armazena na variável 'result' como uma lista de tuplas.

        if result:
            for row in result:
             print('Especialidade: ', row[0])
        else:
            print('\nSem registro de especialidade\n')
        cursor.close()

    def appointment_history():
        pass ##NECESSÁRIO IMPLEMENTAR!

    