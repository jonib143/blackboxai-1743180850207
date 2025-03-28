from auth import load_data, save_data

def list_users(role=None):
    users = load_data('users.json')
    if role:
        users = [u for u in users if u['role'] == role]
    
    print("\n--- User List ---")
    for user in users:
        print(f"ID: {user['id']}")
        print(f"Username: {user['username']}")
        print(f"Role: {user['role'].capitalize()}")
        print("-" * 20)

def create_user():
    print("\nCreate New User Account")
    print("1. Admin")
    print("2. Doctor") 
    print("3. Nurse")
    print("4. Patient")
    
    choice = input("Select role (1-4): ")
    roles = {1: 'admin', 2: 'doctor', 3: 'nurse', 4: 'patient'}
    
    if choice.isdigit() and int(choice) in roles:
        from auth import create_user
        create_user(roles[int(choice)])
    else:
        print("Invalid selection")

def delete_user():
    list_users()
    user_id = int(input("\nEnter user ID to delete: "))
    
    users = load_data('users.json')
    user = next((u for u in users if u['id'] == user_id), None)
    
    if not user:
        print("User not found")
        return
    
    if user['role'] == 'admin' and sum(1 for u in users if u['role'] == 'admin') == 1:
        print("Cannot delete the last admin account")
        return
    
    users.remove(user)
    save_data('users.json', users)
    print("\nUser deleted successfully")

def admin_menu():
    while True:
        print("\nAdmin Panel")
        print("1. List Users")
        print("2. Create User")
        print("3. Delete User")
        print("4. Back to Main Menu")
        
        choice = input("Select option (1-4): ")
        
        if choice == '1':
            list_users()
        elif choice == '2':
            create_user()
        elif choice == '3':
            delete_user()
        elif choice == '4':
            break
        else:
            print("Invalid option")