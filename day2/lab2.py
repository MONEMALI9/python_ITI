#!/usr/bin/env python
# coding: utf-8

#  # lab2

# 1. write a program that count up the number of vowles[a,e,i,o,u] contained in string

# In[7]:


#name =  input("enter your name : ")
name  = "monem"
v = ['a','e','i','o','u']
count = 0 
for i in name:
    if i in v:
        count+=1
print(f"the number of vowles[a,e,i,o,u] contained in string = {count}")


# 2. fill an array of 5 elements from user sort it in descending order and ascending order then display output 

# In[9]:


n = 5
num_list = list(int(num) for num in input("Enter the list items separated by space ").strip().split())[:n]

num_list.sort()
print(num_list)
num_list.sort(reverse=True)
print(num_list)


# 3. write a program that print the number of times the string 'iti' occurs in any thing

# In[7]:


s = input("enter your string : ").strip().split()
print(s)
print(type(s))
counter = 0
for i in s:
    if i == 'iti':
        counter+=1
        
print(f"the number of times the string 'iti' occurs =  {counter}")


# 4. write a program to remove all vowels from string

# In[11]:


#name =  input("enter your name : ")
name  = "monem"
v = ['a','e','i','o','u']
new_word = ""
for i in name:
    if i in v:
        continue
    else:
      new_word = new_word + i
print(f"the new_word after remove all vowels from string : {new_word}")


# 5. write a program that print the loactions of 'i' char in word

# In[12]:


word =  input("enter your name : ")
l = []
for i in range(len(word)):
    if word[i] == 'i':
        l.append(i)
print(f"the loactions of 'i' char in word: {l}")


# 6. write a programe that generate a multiplication  table from 1 to number based

# In[10]:


def multiplication_table(num):
    for i in range(1, num + 1):
        print(f"Multiplication table for {i}:")
        for j in range(1, 13):
            result = i * j
            print(f"{i} x {j} = {result}")
        print()

if __name__ == "__main__":
    try:
        num = int(input("Enter a number to generate the multiplication table: "))
        multiplication_table(num)
    except ValueError:
        print("Please enter a valid integer.")


# write a program to build a mario pyramid

# In[1]:


mp = int(input("enter the number : "))

for i in range(mp):
   print(" "*(mp-i)+"*"*(i+1))


# !jupyter nbconvert --to script lab1.ipynb

# In[11]:


get_ipython().system('jupyter nbconvert --to script lab2.ipynb')

