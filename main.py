from auth import login, reset_password
from patient_records import (
    add_patient, 
    view_patient,
    update_patient,
    list_patients
)
from appointments import (
    schedule_appointment,
    view_appointments,
    cancel_appointment
)
from admin import admin_menu
import sys

def show_main_menu(user):
    while True:
        print(f"\nHospital Management System - {user['role'].capitalize()} Panel")
        
        # Common options for all roles
        print("1. View Profile")
        print("2. Change Password")
        
        # Role-specific options
        if user['role'] in ['doctor', 'nurse', 'admin']:
            print("3. Patient Records")
            print("4. Appointments")
        
        if user['role'] == 'patient':
            print("3. My Appointments")
            print("4. My Medical Records")
        
        if user['role'] == 'admin':
            print("5. Admin Panel")
            
        print("0. Logout")
        
        choice = input("\nSelect option: ")
        
        if choice == '1':
            view_patient(user.get('patient_id'))
        elif choice == '2':
            reset_password()
        elif choice == '3' and user['role'] != 'patient':
            manage_patient_records()
        elif choice == '3' and user['role'] == 'patient':
            view_appointments()
        elif choice == '4' and user['role'] != 'patient':
            manage_appointments()
        elif choice == '4' and user['role'] == 'patient':
            view_patient(user.get('patient_id'))
        elif choice == '5' and user['role'] == 'admin':
            admin_menu()
        elif choice == '0':
            print("Logging out...")
            break
        else:
            print("Invalid option")

def manage_patient_records():
    while True:
        print("\nPatient Records Management")
        print("1. Add New Patient")
        print("2. View Patient")
        print("3. Update Patient")
        print("4. List All Patients")
        print("5. Back to Main Menu")
        
        choice = input("Select option: ")
        
        if choice == '1':
            add_patient()
        elif choice == '2':
            view_patient()
        elif choice == '3':
            update_patient()
        elif choice == '4':
            list_patients()
        elif choice == '5':
            break
        else:
            print("Invalid option")

def manage_appointments():
    while True:
        print("\nAppointments Management")
        print("1. Schedule Appointment")
        print("2. View Appointments")
        print("3. Cancel Appointment")
        print("4. Back to Main Menu")
        
        choice = input("Select option: ")
        
        if choice == '1':
            schedule_appointment()
        elif choice == '2':
            view_appointments()
        elif choice == '3':
            cancel_appointment()
        elif choice == '4':
            break
        else:
            print("Invalid option")

def main():
    print("Hospital Management System")
    print("-------------------------")
    
    while True:
        print("\n1. Login")
        print("2. Password Recovery")
        print("3. Exit")
        
        choice = input("Select option: ")
        
        if choice == '1':
            user = login()
            if user:
                show_main_menu(user)
        elif choice == '2':
            reset_password()
        elif choice == '3':
            print("Exiting system...")
            sys.exit()
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()