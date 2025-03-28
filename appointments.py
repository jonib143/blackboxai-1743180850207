from auth import load_data, save_data
from datetime import datetime

def schedule_appointment():
    appointments = load_data('appointments.json')
    patients = load_data('patients.json')
    
    # Get patient ID
    patient_id = int(input("Enter patient ID: "))
    if not any(p['id'] == patient_id for p in patients):
        print("Invalid patient ID")
        return
    
    # Get doctor ID
    doctor_id = int(input("Enter doctor ID: "))
    
    # Get appointment datetime
    while True:
        try:
            date_str = input("Enter appointment date/time (YYYY-MM-DD HH:MM): ")
            appointment_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
            if appointment_time < datetime.now():
                print("Cannot schedule appointment in the past")
                continue
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD HH:MM")
    
    # Check for conflicts
    conflict = any(
        a['doctor_id'] == doctor_id and 
        datetime.fromisoformat(a['date_time']) == appointment_time
        for a in appointments
    )
    
    if conflict:
        print("Doctor already has an appointment at that time")
        return
    
    # Create appointment
    appointment = {
        'id': len(appointments) + 1,
        'patient_id': patient_id,
        'doctor_id': doctor_id,
        'date_time': appointment_time.isoformat(),
        'status': 'scheduled',
        'created_at': datetime.now().isoformat()
    }
    
    appointments.append(appointment)
    save_data('appointments.json', appointments)
    print("\nAppointment scheduled successfully")

def view_appointments(doctor_id=None):
    appointments = load_data('appointments.json')
    patients = load_data('patients.json')
    
    if doctor_id is None:
        doctor_id = input("Enter doctor ID (leave blank for all): ")
        doctor_id = int(doctor_id) if doctor_id else None
    
    filtered = [
        a for a in appointments
        if doctor_id is None or a['doctor_id'] == doctor_id
    ]
    
    print("\n--- Appointments ---")
    for appt in sorted(filtered, key=lambda x: x['date_time']):
        patient = next(p for p in patients if p['id'] == appt['patient_id'])
        date = datetime.fromisoformat(appt['date_time']).strftime("%Y-%m-%d %H:%M")
        print(f"{appt['id']}: {patient['name']} at {date} ({appt['status']})")

def cancel_appointment():
    view_appointments()
    appointment_id = int(input("\nEnter appointment ID to cancel: "))
    
    appointments = load_data('appointments.json')
    appointment = next((a for a in appointments if a['id'] == appointment_id), None)
    
    if not appointment:
        print("Appointment not found")
        return
    
    appointment['status'] = 'cancelled'
    save_data('appointments.json', appointments)
    print("\nAppointment cancelled successfully")