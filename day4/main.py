from registeration import *
from login import *
import json

def check_input(choice):
    choice = choice.lower()
    return choice 
    

def main():
    while True:
        choice = input("please enter login \
            or register to continue\n")
        choice = check_input(choice)
        
        if(choice == "login"):
            user_name, password = login(registered_users)
            print('welcome',user_name)
            break
        
        elif (choice=="register"):

            user_name = user_name()
                
            national_id = user_national_id()
             
            email = is_valid_email(input("enter your email :"))
          
            password_creation = create_password()
               
            check_date = askfordate(input("enter date :" +"like dd/mm/yyy"))
                
            check_phone_number = is_valid_egyptian_phone_number()
            
            
            # Dictionary to store registered users' email and password
            registered_users = [{"user_name" : user_name,
                                "national_id" : national_id,
                                "email":email,
                                "password":password_creation,
                                "date":check_date,
                                "phone_number":check_phone_number}]


            # Store the email and password in the dictionary  
            # convert or dump a Python Dictionary to JSON String, and write this JSON string to a file named data.json.          
            jsonString = json.dumps(registered_users)
            
            jsonFile = open("data.json", "a")
            
            jsonFile.write(jsonString)
            
            jsonFile.close()
            
            print("Account registered successfully!")            
            break
        
        else :
            print ("invalid option please try again")
            
            
if __name__=="__main__":
    main()
    