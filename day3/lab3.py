#!/usr/bin/env python
# coding: utf-8

# 1. Write a function that accepts two arguments (length, start) to
# generate an array of a specific length filled with integer numbers
# increased by one from start

# In[4]:


def generate_array(length,start):
    if length.isdigit() and start.isdigit():
        length = int(length)
        l = []
        while length:
            start = int(start)
            l.append(start)
            start +=1
            length -= 1
    else:
        x = "Please enter a valid integer"
        return x
    return l


# In[5]:


## main
if __name__== "__main__":
    length = input("enter array length : ")
    start = input("enter the begin of array : ")
    print(generate_array(length,start))


# 2. write a function that takes a number as an argument and if the
# number divisible by 3 return "Fizz" and if it is divisible by 5 return
# "buzz" and if is is divisible by both return "FizzBuzz"

# In[6]:


def divisable(num):
    if num.isnumeric():
        num = int(num)
        if num%3 == 0 and num%5 == 0:
            x = "FizzBuzz"
            return x
        elif num%3 == 0:
            x = "Fizz"
            return x
        elif num%5 == 0:
            x = "buzz"
            return x
    else:
        x = "Please enter a valid integer"
        return x


# In[10]:


## main
if __name__== "__main__":
    num = input("enter the number : ")
    print(divisable(num))


# 3. Write a function which has an input of a string from user then it
# will return the same string reversed.

# In[11]:


def revers_string(strs):
    return strs[::-1]


# In[12]:


## main
if __name__== "__main__":
    strs = input("enter the number : ")
    print(revers_string(strs))


# 4. Ask the user for his name then confirm that he has entered his
# name(not an empty string/integers). then proceed to ask him for
# his email and print all this data (Bonus) check if it is a valid email
# or not

# In[33]:


def check_name(name):
    name.strip()
    if name.isalpha():
        confirm_name = "name is confirmed\n"
        print(confirm_name)
        email = input("enter your email : ")
        email.strip()
        if  '@' in email and '.' in email:
            confirm_email = "email is confirmed"
            print(confirm_email)
            return confirm_email
    else:
        x = "Please enter a valid string"
        return x


# In[35]:


## main
if __name__== "__main__":
    name = input("enter the user name : ")
    print(check_name(name))


# 5. Write a function that takes a string and prints the
# longest alphabetical ordered substring occurred For example, if
# the string is 'abdulrahman' then the output is: Longest substring in
# alphabetical order is: abdu

# In[28]:


def longest_alphabetical_substring(s):
    longest_substring = ""
    current_substring = ""

    for char in s:
        if not current_substring or char >= current_substring[-1]:
            current_substring += char
        else:
            current_substring = char

        if len(current_substring) > len(longest_substring):
            longest_substring = current_substring

    return f"Longest substring in alphabetical order is: {longest_substring}"


# In[29]:


if __name__ == "__main__":
    input_string = input("enter your string : ")
    result = longest_alphabetical_substring(input_string)
    print(result) 


# 6. Write a program which repeatedly reads numbers until the user enters “done”.
#     1. Once “done” is entered, print out the total, count, and average of the numbers.
#     2. If the user enters anything other than a number, detect their mistake, print an error message and skip to the next number.

# In[3]:


def track_number():
    l = []
    while True:
        num = input("enter number : ")
        num.lower()
        if num == 'done':
            if l == []:
                print('No Numbers Entered')
                break
            else:
                print(f"number of numbers you entered = {len(l)}")
                print(f"summation of numbers you entered = {sum(l)}")
                print(f"average of numbers you entered = {sum(l)/len(l)}")
                break
        elif num.isnumeric():
            num = int(num) 
            l.append(num)
        else:
            print("Please enter a valid number")


# In[5]:


if __name__ == "__main__":
    result = track_number()


# Word guessing game (hangman)
# 1. A list of words will be hardcoded in your program, out of which the interpreter will
# 2. choose 1 random word.
# 3. The user first must input their names
# 4. Ask the user to guess any alphabet. If the random word contains that alphabet, it
# 5. will be shown as the output(with correct placement)
# 6. Else the program will ask you to guess another alphabet.
# 7. Give 7 turns maximum to guess the complete word.

# In[ ]:





# In[7]:


get_ipython().system('jupyter nbconvert --to script lab3.ipynb')

