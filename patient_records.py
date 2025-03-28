from auth import load_data, save_data
from datetime import datetime

def add_patient():
    patients = load_data('patients.json')
    user_id = int(input("Enter associated user ID: "))
    
    if any(p['user_id'] == user_id for p in patients):
        print("Patient record already exists for this user")
        return
    
    patient = {
        'id': len(patients) + 1,
        'user_id': user_id,
        'name': input("Full name: "),
        'age': int(input("Age: ")),
        'gender': input("Gender (M/F/O): ").upper(),
        'contact': input("Contact info: "),
        'allergies': input("Allergies (comma separated): ").split(','),
        'chronic_diseases': input("Chronic diseases (comma separated): ").split(','),
        'created_at': datetime.now().isoformat()
    }
    
    patients.append(patient)
    save_data('patients.json', patients)
    print("\nPatient record created successfully")

def view_patient(patient_id=None):
    patients = load_data('patients.json')
    
    if not patient_id:
        patient_id = int(input("Enter patient ID: "))
    
    patient = next((p for p in patients if p['id'] == patient_id), None)
    
    if patient:
        print("\n--- Patient Record ---")
        print(f"ID: {patient['id']}")
        print(f"Name: {patient['name']}")
        print(f"Age: {patient['age']}")
        print(f"Gender: {patient['gender']}")
        print(f"Contact: {patient['contact']}")
        print(f"Allergies: {', '.join(patient['allergies'])}")
        print(f"Chronic Diseases: {', '.join(patient['chronic_diseases'])}")
    else:
        print("Patient not found")
    return patient

def update_patient():
    patient = view_patient()
    if not patient:
        return
    
    patients = load_data('patients.json')
    patient = next(p for p in patients if p['id'] == patient['id'])
    
    print("\nLeave blank to keep current value")
    patient['name'] = input(f"Name [{patient['name']}]: ") or patient['name']
    patient['age'] = int(input(f"Age [{patient['age']}]: ") or patient['age'])
    patient['contact'] = input(f"Contact [{patient['contact']}]: ") or patient['contact']
    patient['allergies'] = input(f"Allergies [{', '.join(patient['allergies'])}]: ").split(',') or patient['allergies']
    
    save_data('patients.json', patients)
    print("\nPatient record updated successfully")

def list_patients():
    patients = load_data('patients.json')
    print("\n--- Patient List ---")
    for p in patients:
        print(f"{p['id']}: {p['name']} ({p['age']} {p['gender']})")