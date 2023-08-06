# Dictionary to store registered users' email and password
registered_users = {}

def register_user():
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    # Store the email and password in the dictionary
    registered_users[email] = password
    print("Account registered successfully!")

def login():
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    # Check if the email is registered and the password is correct
    if email in registered_users and registered_users[email] == password:
        print("Login successful!")
    else:
        print("Invalid email or password. Please try again.")

if __name__ == "__main__":
    # Registration phase
    print("Registration:")
    register_user()

    # Login phase
    print("\nLogin:")
    login()
