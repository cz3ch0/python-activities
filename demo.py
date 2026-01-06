#This is my first python program, notes for myself 
print("I like Pizza Hut!")
print("It's Really Good!")

#Variable = A container for a value ( String, Integer, float, Boolean)
# A variable behaves as if it was the value it contains
#this are string, a series of characters
first_name = "Bro"
food = "Pizza"
email= "bro@gmail.com"

print(f"Hello {first_name} my favorite food is {food} and my email is {email}")

# integers
age = 25
quantity = 3.5
num_of_students = 30

print(f"You are {age} years old")
print(f"you are buying {quantity} items")
print(f"your class has {num_of_students} students")

# float 
price = 10.99
gpa = 2.55
distance = 5.5

print(f"the price is ${price}")
print(f"your gpa {gpa}")
print (f"you ran {distance}km")

# boolean is either true or false 

is_student = True
for_sale = True
is_online = True
print(f"are you a student{is_student}")

if is_student:
    print("You are a student")
else:
    print("You are not a student")
    
if for_sale:
    print(f"You can buy it @ a price of {price}")
else:
    print("This is not for Sale")
    
    if is_online:
        print("You are Online")
    else:
        print("Youre offline")

# first activity personal information about me

name = "Bro F. Liefe"
age = 28
birthday = "07/22/1992"
email = "brofliefe@gmail.com"
is_graduate = False
is_student = True
school = "Batangas State University"

print(f"My name is {name} I am {age} years old, my birtyday is on {birthday}, my email is {email}")
if is_graduate:
    print(f"Welcome to the Real World {name}")
else:
    print(f"Dont Stop Believing that you will Graduate{name} @ {school}")
    
    # Activity2
    #Create my own variables
    
full_name = "Jericho Santos Castro"
year_level = 4
gwa = 2.00
has_internship = True

print("name:", full_name)
print("year_level:", year_level)
print("GWA:", gwa)
print("Has intership:", has_internship)

# Typecasting = the process of converting a variable from one data type to another str(). int(). Float(). Bool()


name = "jec"
age = 25 
gpa = 3.2
is_student = True

name = is_student
print(name)

#user input input() = a function that prompts the user to enter data Returns the entered data as string
name = input("What is your name?:")
age = int(input("How old are you?:"))

age = age + 1
print(f"Hello {name}")
print(f"HAPPY BIRTHDAY!")
print(f"you are {age} years old")

# solve the area of a rectangle Area = l * w

length = float(input("Enter the length:"))
width = float(input("Enter the width:"))

area = length * width 

print("The area of the rectangle is",  area, "ᶜᵐ²") 
