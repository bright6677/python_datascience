#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Write a Python function that takes a single argument and returns its square.
def square(a):
    return a*a
a=square(5)
a


# In[6]:


#Create a Python function named 'greet' that takes a name as an argument and prints "Hello, [name]!"If no name is provided, it should print "Hello, World!".
def greet(name="World"):
    print("Hello,",name + "!")
greet("Kristi don") 
greet()       



# In[8]:


#Define a Python function called 'calculate_total' that calculates the total cost of items in a shopping cart. The function should take item prices as optional arguments and return the total cost. If no prices are provided, the function should return 0.
def calculate_total(*prices):
    total_cost = sum(prices)
    return total_cost
a = calculate_total(10, 20, 30)
print("Total cost with provided prices:", a)
b= calculate_total()
print("Total cost with no prices provided:", b) 


# In[11]:


#Implement two Python functions: one named 'print_info' which only takes one argument (name) and prints "Name: [name]", and another function named 'print_details' which takes both 'name' and 'age' as keyword arguments and prints "Name: [name], Age: [age]".
def print_info(name):
    print("Name:", name)
def print_details(name, age):
    print("Name:", name + ",", "Age:", age)
print_info("Kristi")
print_details(name="Naam kina chaiyo", age=16)


# In[13]:


#Write a Python function called 'calculate_discounted_price' that calculates the discounted price of a product. The function should take the original price as a single argument and apply a default discount of 10%.
def calculate_discounted_price(original_price, discount=0.1):
    discounted_price = original_price * (1 - discount)
    return discounted_price
discounted_price = calculate_discounted_price(100)
print("Discounted price with default discount:", discounted_price)  # Output: 90.0
custom_discounted_price = calculate_discounted_price(100, discount=0.2)
print("Discounted price with custom discount:", custom_discounted_price)  # Output: 80.0


# In[15]:


#Create a Python function named 'print_items' that accepts any number of arguments and prints each item on a new line.
def print_items(*arguments):
    for item in arguments:
        print(item)
print_items("c.momo", "vegmomo", "jholmomo")
print_items(1, 2, 3, 4, 5)
print_items("dogs", "abc", "bird")


# In[16]:


#Define a Python function called 'create_person' that accepts keyword arguments such as 'name', 'age', and 'gender', and returns a dictionary containing these details.
def create_person(**a):
    return a
b=create_person(name="Sabin", age=30, gender="Female")
c=create_person(name="Laxmi", age=25)
d=create_person(name="Ganga", gender="Female")
print(b)
print(c)
print(d)



# In[18]:


#Write a Python function named 'calculate_area' that calculates the area of a rectangle. It should accept the dimensions as either positional arguments (length and width) or as keyword arguments (length=, width=).
def calculate_area(length, width):
    return length * width
a=calculate_area(5, 4)
print("Area with positional arguments:", a)
b=calculate_area(length=6, width=3)
print("Area with keyword arguments:",b) 


# In[22]:


#Implement a Python function named 'send_email' that accepts keyword arguments such as 'recipient', 'subject', and 'message', and simulates sending an email using these details.
def send_email(**a):
    recipient = a.get('recipient', 'Recipient')
    subject = a.get('subject', 'No subject')
    message = a.get('message', '')
    print("Sending email to:", recipient)
    print("Subject:", subject)
    print("Message:", message)
send_email(recipient='janqueen@gmail.com', subject='Hello', message='Hello, World!')
Sending email to: janqueen@gmail.com
Subject: Hello
Message: Hello, World!



# In[25]:


#Create a Python function called 'average' that accepts any number of arguments and returns their average.
def average(*args):
    if not args:
        return 0
    return sum(args) / len(args)
print(average(7))


# In[ ]:





# In[ ]:




