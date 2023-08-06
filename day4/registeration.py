import random
import re
import string


def user_name(fname = "monem",lname = "ali"):
    
    while True:
        fname = input("enter your first name : ").strip()
        lname = input("enter your last name : ").strip()
        
        flag_fname = flag_lname = False
        
        if fname.isalpha() and lname.isalpha():
            return fname , lname
        else:
            if (not flag_fname):
                print("your first name is not validator....try again")
            elif (not flag_lname):
                print("your last name is not validator....try again")
            
               
def user_national_id(nid = "11111111111111"):
    
    while True:
        nid = input("enter national id number \
            without any space or special character \
                fully 14 digits").strip()
        if len(id) == 14:
            flag_nid = False
            
            if nid.isdigit():
                return nid
            else:
                if (not  flag_nid):
                    print("your National ID is not validator \
                        ....try again")
        else:
            print ("National Id should be of length exactly 14.")
            

def is_valid_email(email):
    
    # Regular expression pattern for email validation
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    # Use the `re.match` function to match the pattern against the email
    match = re.match(pattern, email)

    # If there is a match and it spans the entire email length, then it's valid
    if match and match.span()[1] == len(email):
        return True
    else:
        return False


def generate_password():
    
    lower_char = "abcdefghijklmnopqrstuvwxyz"
    upper_char = lower_char.upper()
    numbers = "1234567890"
    symbols = "[]{}()!@#$%^&*\\/.,\';:"
    
    all = lower_char + upper_char + numbers + symbols
    length = 16
    
    password = "".join(random.sample(all,length))
    
    return password


def create_password():
    
    order = input("Enter 'generate' to auto-generate a password, "
                  "otherwise enter 'create' to input your own password: ").strip().lower()
    
    if order == "generate" or order != "create":
        return generate_password()
    else:
        print("Instructions:\n"
              "1. Your password must contain numbers, characters, and symbols.\n"
              "2. It should contain at least one uppercase character.\n"
              "3. It should contain at least one symbol.")
        
        while True:
            your_pass = input("Enter your own password: ").strip()
            
            lower_char = string.ascii_lowercase
            upper_char = string.ascii_uppercase
            numbers = string.digits
            symbols = "[]{}()!@#$%^&*\\/.,';:"
            
            if len(your_pass) >= 8:
                fupass = flpass = fspass = fnpass = 0
                for i in upper_char: 
                    if i in your_pass:
                        fupass += 1
                        break
                for j in numbers:
                    if j in your_pass:
                        fnpass += 1
                        break
                for k in symbols:
                    if k in your_pass:
                        fspass += 1
                        break
                for z in lower_char:
                    if z in your_pass:
                        flpass += 1
                        break
                
                if fupass > 0 and flpass > 0 and fspass > 0 and fnpass > 0:
                    return your_pass
                else:
                    print("Your password must contain at least one uppercase character, "
                          "one lowercase character, one symbol, and one number.")
            else:
                print("Your password must be 8 characters or longer.")

if __name__ == "__main__":
    print(create_password())
                
def askfordate(message): 
    import re
    while True: 
        inputdate = input(message+"like dd/mm/yyy") 
        
        pattern = r"\d{4}/\d{2}/\d{2}"
        if re.fullmatch(pattern, inputdate):
            return inputdate 
        
        print("--- not valid date ----")


def is_valid_egyptian_phone_number(phone_number):
    while True:
        # Regular expression pattern for Egyptian phone numbers
        pattern = r'^01[0-9]{9}$'

        # Use the `re.fullmatch` function to match the pattern against the phone number
        match = re.fullmatch(pattern, phone_number)

        # If there is a match, then it's a valid Egyptian phone number
        if match:
            x = "Valid Egyptian phone number!"
            return x
        else:
            print("Invalid Egyptian phone number. Please enter a valid number in the format 01X XXXX XXXX.")
if __name__ == "__main__":
    phone_number = input("Enter your Egyptian phone number (01X XXXX XXXX): ")
    
