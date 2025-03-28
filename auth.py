import json
import bcrypt
from getpass import getpass

def load_data(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_data(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def verify_password(password, hashed):
    return bcrypt.checkpw(password.encode(), hashed.encode())

def login():
    username = input("Username: ")
    password = getpass("Password: ")
    
    users = load_data('users.json')
    user = next((u for u in users if u['username'] == username), None)
    
    if user and verify_password(password, user['password_hash']):
        print(f"\nWelcome, {user['role'].capitalize()} {username}!")
        return user
    print("\nInvalid credentials")
    return None

def reset_password():
    username = input("Username: ")
    users = load_data('users.json')
    user = next((u for u in users if u['username'] == username), None)
    
    if not user:
        print("User not found")
        return
    
    answer = input(f"\nSecurity question: {user['security_question']}\nAnswer: ")
    if verify_password(answer, user['security_answer']):
        new_pass = getpass("New password: ")
        user['password_hash'] = hash_password(new_pass)
        save_data('users.json', users)
        print("\nPassword updated successfully")
    else:
        print("\nIncorrect answer")

def create_user(role):
    users = load_data('users.json')
    
    username = input("Enter username: ")
    if any(u['username'] == username for u in users):
        print("Username already exists")
        return
    
    password = getpass("Enter password: ")
    security_question = input("Enter security question: ")
    security_answer = getpass("Enter security answer: ")
    
    users.append({
        'id': len(users) + 1,
        'username': username,
        'password_hash': hash_password(password),
        'role': role,
        'security_question': security_question,
        'security_answer': hash_password(security_answer)
    })
    
    save_data('users.json', users)
    print(f"\n{role.capitalize()} account created successfully")