from utils.save_appointments_to_json import save_apointments_to_json

class Appointment:

    appointments_list = []

    def __init__(self, animal, veterinarian, date, time, description):
        self._animal = animal
        self._veterinarian = veterinarian
        self._date = date
        self._time = time
        self._description = description
        self._id = None
        self._status = False

    def schedule_appointment(self):
        """
        Verifica se a lista tem conteudo cadastrado, se sim,
        cria o id do novo agendamento somando o id anterior com 1
        se não. o id é 1
        """
        if Appointment.appointments_list:
            last_appointment = Appointment.appointments_list[-1]
            last_id = last_appointment["Id"]
            new_id = last_id + 1
        else:
            new_id = 1
        self._id = new_id
        self._status = True
        "salva as informações num dicionario"
        new_appointment = {
            "Id" : self._id,
            "Animal" : self._animal,
            "Veterinarian" : self._veterinarian,
            "Date" : self._date,
            "Time" : self._time,
            "Description" : self._description,
            "Status" : self._status
        }
        Appointment.appointments_list.append(new_appointment)
        save_apointments_to_json()

    def reschedule_appointment(self, new_date, new_time):
        """
        Utiliza um loop para percorrer a lista e compara se o id do dicionario é igual o id da consulta que queremos reagendar.
        Se for igual, salvamos a nova data e novo horário nas suas respectivas chaves no dicionário e alteramos o valor dos atributos
        no objeto da atual consulta.
        """
        for appointment in Appointment.appointments_list:
            if appointment["Id"] == self._id:
                appointment["Date"] = new_date
                appointment["Time"] = new_time
                self._date = new_date
                self._time = new_time

    def cancel_appointment(self):
        
        for appointment in Appointment.appointments_list:
            
            if appointment["Id"] == self._id:
                if appointment["Status"] == True:
                    self._status = False
                    appointment["Status"] = self._status
                    print(f'A consulta de id {self._id} com o doutor {self._veterinarian} foi cancelada com sucesso!')
                else:
                    print('Consulta já consta como cancelada!\n')
