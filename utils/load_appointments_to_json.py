import json

def load_appointments_to_json(filename="appointments.json")
    from models.appointments import Appointment
    try:
        with open(filename, "r", encoding='utf-8') as f
            Appointment.appointments_list = json.load(f)
    except:

