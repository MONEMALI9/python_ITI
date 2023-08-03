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
    import re
    
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
    import random
    
    lower_char = "abcdefghijklmnopqrstuvwxyz"
    upper_char = lower_char.upper()
    numbers = "1234567890"
    symbols = "[]{}()!@#$%^&*\\/.,\';:"
    
    all = lower_char + upper_char + numbers + symbols
    length = 16
    
    password = "".join(random.sample(all,length))
    
    return password



def create_password(order = "generate"):
    order = input("enter your order if you want to auto generate \
        password  type \" generate\" \
            otherwise enter the custom password \
                type \" create\" ").strip()
     
    if order == "generate" or order != "create":
        passwrd=generate_password()
        return passwrd
    else:
        print("instructions : \n \
            1. your password must contain numbers, characters, symbols \n\
            2. @ least contain one upper character \n\
            3. @ least contain one sympol")
        while True:
            your_pass = input("enter your own password").strip()
            
            lower_char = "abcdefghijklmnopqrstuvwxyz"
            lower_char.split()
            
            upper_char = upper_char.upper()
            upper_char.split()
            
            numbers = "1234567890"
            numbers.split()
            
            symbols = "[]{}()!@#$%^&*\\/.,\';:"
            symbols.split()
            
            if len(your_pass) >= 8:
                fupass = flpass = fspass = fnpass = 0
                for i in upper_char: 
                    if i in your_pass:
                        fupass+=1
                for j in numbers :
                    if j in your_pass:
                        fnpass+=1
                for k in symbols:
                    if k in your_pass:
                        fspass+=1
                for z in lower_char:
                    if z in lower_char :
                        flpass+=1
                if fupass>0 and flpass>0 and fspass>0 and fnpass>0:
                    return your_pass 
            else:
                print("you must enter 8 or more.") 