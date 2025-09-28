from appointment import Appointment

class VeterinaryMedicalRecord: ##prontuário
    def __init__(self, animal):
        self._animal = animal
        self._appointment_historic = []
        self._treatments = []

    def add_records(self, appointment, treatment = None ):
        print('***Adicionar Registros: \n')
        if not isinstance(appointment, Appointment):
            print('Dado invalido, você precisa adicionar uma consulta!')
        else:    
            data = {
            "Id" : appointment._id,
            "Animal" : appointment._animal,
            "Veterinarian" : appointment._veterinarian,
            "Date" : appointment._date,
            "Time" : appointment._time,
            "Description" : appointment._description,
            "Status" : appointment._status
        }
        self._appointment_historic.append(data)
        if treatment:
            self._treatments.append(treatment)

    def access_history(self):
        print(f'CONSULTAS:\n')
        for appointment in self._appointment_historic:
            print(appointment)
        print(f'TRATAMENTOS: \n')
        for treatment in self._treatments:
            print(treatment)