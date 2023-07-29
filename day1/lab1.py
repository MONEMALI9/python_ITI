#!/usr/bin/env python
# coding: utf-8

# # Lab01

# ## Before you start you should install the python interpreter and vscode or pycharm

# Q1 : add your info in Variables then print them.
# 1. firstname
# 2. lastname
# 3. email
# 4. address
# 5. intake

# In[5]:


fname = "Monem"
lname = "Elmongy"
email = "monem921999@gmail.com"
address = "mansoura"
intake = "Q1 intake 44"
info = "{} {} , {} , {} , {}".format(fname,lname,email,address,intake)
print(info)


# Q2 : write a paragraph about yourself in 5 lines -make
# sure that the string is stored as a multiline string

# In[ ]:





# Q3 : Given the total marks of a student→ write a
# program that prints the grade of a student as follows:
# 
# 1. Grade < 60 failed.
# 2. Grade > 60 passed.
# 3. Grade > 65 Good.
# 4. Grade > 75 very good.
# 5. Grade > 85 Excellent.

# In[1]:


#grade = int(input("enter your grade : "))
grade = 50
if grade < 60:
    print("failed")
elif grade > 60 and grade < 65:
    print("passed")
elif grade > 65 and grade < 75:
    print("good")
elif grade > 75 and grade < 85:
    print("very good")
elif grade > 85 and grade <= 100:
    print("Excellent")
else:
    print("error .... try again")


# Q4 : Write a program that prints the weather state according to the temperature
# 1. If the temperature > 25 then print “the weather is hot”
# 2. If the temperature < 25 print “the weather is cold”
# 3. If the temperature = 25 then print the “weather is fine”

# In[2]:


#temp = int(input("enter your grade : "))
temp = 50
if temp > 25:
    print("the weather is hot")
elif temp < 25:
    print("he weather is cold")
elif temp == 25 :
    print("weather is fine")
else:
    print("error .... try again")


# 5- write a program that checks if the number is greater
# than 0 and then prints positive else prints negative

# In[3]:


#num = int(input("enter your number that you want to check if positve"))
num = 5
if num > 0:
    print("positive")
elif num < 0:
    print("negative")
else :
    print("zero")


# 6- print the types of variables you entered before

# In[6]:


print(type(fname))
print(type(lname))
print(type(email))
print(type(address))
print(type(intake))
print(type(info))
print(type(grade))
print(type(temp))
print(type(num))


# 7- given 2 numbers<br>
# Num1 = 10<br>
# Num2 = 20<br>
# Calculate the sum, diff, multiply, and division of the 2 numbers.
# 

# In[7]:


num1 = 10
num2 = 20
sum = num1+num2
sub = num1-num2
mul = num1*num2
div = num1/num2
print(sum,sub,mul,div)


# 8- ask the user to enter the name of the day
# 1. If he entered Sunday then print(‘wish you a good week ’)
# 2. If he entered Tuesday then print(‘The weekend is near ’)
# 3. he entered Friday then print(‘enjoy your weekend’)
# 4. If he entered other day print(‘ma3lsh’)
# 5. If entered not valid day —> please enter day again.

# In[8]:


#NameOfDay = input("enter the name of day")
NameOfDay = "Sunday"
if NameOfDay == "Sunday":
    print("wish you a good week")
elif NameOfDay == "Tuesday":
    print("The weekend is near")
elif NameOfDay == "Friday":
    print("Enjoy your weekend")
elif NameOfDay == "Saturday" or NameOfDay == "monday" or NameOfDay == "thursday" or NameOfDay == "wednesday":
    print("mal3sh")
else:
    print("try.......again")


# Q9 : ask the user to enter his name then print ‘Nice to meet you name’

# In[10]:


#user_name = input("enter your name")
user_name = "monem"
bye = "Nice to meet you , {}".format(user_name)
print(bye)


# Q10 : ask user to enter his firstname then ask him to enter midname then ask him to enter lastname Then print fullname
# 

# In[11]:


#user_fname = input("enter your first name")
#user_mname = input("enter your middle name")
#user_lname = input("enter your last name")
user_fname = "monem"
user_mname = "ali"
user_lname = "elmongy"
print("{} {} {}".format(user_fname,user_mname,user_lname))


# Q11 : ask the user to enter his age and if he enters it correctly then multiply the age by 10 and print the
# result.

# In[22]:


#user_age = int(input("enter your age"))
user_age = True
check_age = str(user_age)
if check_age.isnumeric():
    print(user_age*10)
else:
    print("data that you entered is not numeric")


# Q12 : ask the user to enter 2 numbers num1 and num2 make sure that he enter them as numbers and if all is
# ok print the multiplication them.

# In[24]:


#fnum = int(input("enter first number"))
fnum = 10
#snum = int(input("enter second number"))
snum = 20
if str(fnum).isnumeric() and str(snum).isnumeric():
    print(fnum*snum)
else:
    print("error ....")


# ## Part 02 

# Q1 : Ask the user to enter his name.

# In[25]:


#uname = input("enter your name : ")
uname = "monem"


# Q2 : Count the number of letters in the name he entered.

# In[26]:


print(len(uname))


# 3.Count the number of letters “o” in his name if exists and print the count.

# In[27]:


count = 0
for i in uname:
    if i == 'o':
        count+=1
if count:
    print(count)
else:
    print("No occurrence of o found")


# Q4 : Print the character at index 6 of the name if it exists if not, the print message says that there
# is no character at index 6

# In[29]:


#num_index = int(input("number of index : "))
num_index = 2
if len(uname) < num_index:
    print('Username must be at least', str(num_index), 'characters long.')
else:
    print(uname[num_index])


# Q5 : Ask the user to enter the radius of a circle

# In[30]:


#radius_circle = int(input("enter number of radius_circle"))
radius_circle = 5


# Q6 : Calculate the circumference and the area of the circle.

# In[32]:


import numpy as np
pi = np.pi
print("circumference  = {}".format(2*pi*radius_circle))


# Q7 : Ask the user to enter the length and the height of a rectangle and calculate the circumference and the area.

# In[35]:


#length = float(input("enter the length : "))
length = 5
#height = float(input("enter the height : "))
height = 10

circumference = (length+height)*2
print("the circumference of rectangle = {}".format(circumference))
print("the area of rectangle = {}".format(length*height))


# Q8 : Ask the user to enter his first name, and last name and print the full name using format
# string and concatenation

# In[36]:


firstname = "monem"
lastname = "elmongy"
print(firstname+ " " + lastname)
print("{} {}".format(firstname,lastname))


# jupyter nbconvert testnotebook.ipynb --to python

# In[ ]:


get_ipython().system('jupyter nbconvert --to script lab1.ipynb')

