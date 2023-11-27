'''
n=int(input("Give me a number over 100: "))
if n<=100:
    print(n,"Is not over 100")
else:
    print(n,"Is over 100")
'''
'''
age=input("Pleaase enter your age: ")

try:
    age = int(age)
    if age>=18:
        print("You can Vote!")
    else:
        print("You can't Vote :(")

except ValueError as e:
    print(f"You need to enter a integer number for the age")

'''
'''
import random
chance=random.randint(0,1)

if chance == 0:
    print("it's zero")
else:
    print("It's one")
'''

#Part 1: if
#a)
'''
try:
    n=int(input('Give me a number over 100: '))
    if n <= 100:
        print(n,'is not over 100')
except ValueError:
    print("write an integer")
'''

#b)
'''
age=0
age=int(input("Enter Your age: "))
if age >= 18:
    print("Can Vote")
'''

#Part 2: if-else
#a)
'''
x=int(input('Give me a number: '))
if x < 0:
    print(x, "is negative")
else:
    print(x, "is positive")
'''

#b)
'''
mark=0
mark=int(input("Input mark: "))
if mark < 40:
    print("Fail")
else:
    print("Pass")
'''

#c)
'''
num=0

num=int(input("Enter a number: "))

if num%2==0:
    print("Even")
else:
    print("Odd")
'''

#Part 3: elif (chained conditional)
#a)
'''
print("Welcome to the temperature converter!")
print("Press 1 for convert C° to F°")
print("Press 2 for convert F° to C°")

choice=int(input("Enter a choice (1/2): "))
x=int(input("input temp: "))
output=0

if choice==1:
    output=(x*1.8)+32
    print(output)
elif choice==2:
    output=(x-32)/1.8
    print(output)
else:
    print("Invalid output")
'''

#b)

