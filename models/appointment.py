from utils.db import create_connection

class Appointment:

    appointments_list = []

    def __init__(self, animal, veterinarian, date, time, description):
        self._animal = animal
        self._veterinarian = veterinarian
        self._date = date
        self._time = time
        self._description = description
        self._id = None
        self._status = 'scheduled'

    def schedule_appointment(self,conn):
        cursor = conn.cursor()
        sql = """INSERT INTO appointments (id_animal, id_veterinarian, appointment_date, appointment_time,
         appointment_description, appointment_status) VALUES (%s, %s, %s, %s, %s, %s)"""
        val = (
        self._animal,
        self._veterinarian,
        self._date,
        self._time,
        self._description,
        self._status
        )
        cursor.execute(sql,val)
        conn.commit()
        cursor.close()

    def reschedule_appointment(conn,val):
       cursor = conn.cursor()
       sql = """UPDATE appointments SET appointment_date = %s, appointment_time = %s WHERE id = %s;"""
       cursor.execute(sql,val)
       conn.commit()
       cursor.close()

    def cancel_appointment(conn, val):
        cursor = conn.cursor()
        sql = """ UPDATE appointments SET appointment_status = %s WHERE id = %s """
        cursor.execute(sql,val)
        conn.commit()
        cursor.close()


        pass
        #for appointment in Appointment.appointments_list:
            
            #if appointment["Id"] == self._id:
                #if appointment["Status"] == True:
                    #self._status = False
                    #appointment["Status"] = self._status
                    #print(f'A consulta de id {self._id} com o doutor {self._veterinarian} foi cancelada com sucesso!')
                #else:
                    #print('Consulta já consta como cancelada!\n')
