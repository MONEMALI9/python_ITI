import json

def get_value_from_json(file_path, key):
    with open(file_path, 'r') as json_file:
        json_data = json.load(json_file)
    
    # Access the value of the specified key
    value = json_data.get(key)  # Use .get() method to safely access the key
    
    return value


def authenticate_user(email, password):
    # Check if the provided email is in the registered_users dictionary
    if email in get_value_from_json("data.json", email):
        return True
    return False

def login():
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    if authenticate_user(email, password):
        return "User Name", email  # Replace "User Name" with the actual user's name
    else:
        print("Invalid credentials. Please try again.")
        return None, None
