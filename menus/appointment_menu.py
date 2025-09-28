
def appointment_menu():
        print('\n***AGENDAMENTOS:***: \n')
        print('\n***ESCOLHA O NÚMERO DA OPÇÃO***\n')
        from models.appointment import Appointment

        appointment_option = int(input('\n 1 - Cadastro \n 2 - Reagendar \n'))
        ##animal, veterinarian, date, time, description
        match(appointment_option):
            case 1: 
                animal = input('\nQual o nome do animal?')
                veterinarian = input('\nQual o veterinário que realizará o atendimento?\n')
                date = input('\nQual a data do agendamento?\n')
                time = input('\nQual o horário do agendamento?\n')
                description = input('\n Adicione uma descrição ao agendamento:\n')
                new_appointment = Appointment(animal, veterinarian, date, time, description)
                new_appointment.schedule_appointment()