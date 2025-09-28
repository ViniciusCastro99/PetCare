import json

def save_apointments_to_json(filename="appointments.json"):
    from models.appointment import Appointment

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(Appointment.appointments_list,f,ensure_ascii=False, indent=4)