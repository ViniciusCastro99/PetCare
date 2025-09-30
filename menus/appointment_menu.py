import os
from datetime import datetime
from models.appointment import Appointment
from utils.db import create_connection
def appointment_menu():
        os.system('cls')
        print('\n***MENU - AGENDAMENTOS:***: \n')
        print('\n***ESCOLHA O NÚMERO DA OPÇÃO***\n')

        appointment_option = int(input('\n 1 - Cadastrar \n 2 - Reagendar \n 3 - Cancelar \n'))
        ##animal, veterinarian, date, time, description
        match(appointment_option):
            case 1:
                os.system('cls') 
                print('***AGENDAMENTO DE CONSULTA***')

                animal = input('\nQual o ID do animal?\n')
                veterinarian = input('\nQual o CRMV do veterinário que realizará o atendimento?\n')
                date_input = input('\nQual a data do agendamento?\n')
                time_input = input('\nQual o horário do agendamento?\n')
                description = input('\n Adicione uma descrição ao agendamento:\n')

                date_appointment = datetime.strptime(date_input,"%d/%m/%Y").date()
                time_appointment = datetime.strptime(time_input, "%H:%M").time()

                new_appointment = Appointment(animal, veterinarian, date_appointment, time_appointment, description)
                conn=create_connection()
                new_appointment.schedule_appointment(conn)
                conn.close()
            case 2:
                os.system('cls')
                print('***REAGENDAMENTO DE CONSULTA***')
                appointment_id = int(input('\nQual o id do agendamento?\n'))

                date_input = input('\nQual a nova data da consulta?\n')
                time_input = input('\nQual o novo horário da consulta?\n')

                new_date = datetime.strptime(date_input, "%d/%m/%Y").date()
                new_time = datetime.strptime(time_input, "%H:%M").time()
                val = (new_date,new_time,appointment_id)

                conn = create_connection()
                Appointment.reschedule_appointment(conn,val)
                conn.close()
            case 3:
                print('***CANCELAMENTO DE CONSULTA***')
                appointment_id = int(input('\nQual o id do agendamento?\n'))

                new_status = 'canceled'
                val = (new_status, appointment_id)

                conn = create_connection()
                Appointment.cancel_appointment(conn, val)
                conn.close()
                print('Consulta cancelada com sucesso!')

                