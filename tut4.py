
#For loops (Exercises 4 to 7) 
#Exersice 4

'''
total=0
for i in range(5):
    try:
        num=int(input(f"Input a number to add{i+1}:\n"))
        total=total+num
    except ValueError:
        print("Please enter a valid number")
print(f"Total is {total}")
'''

#Exercise 5

'''
for i in range (1,21):
    if i % 2 == 1:
        print(i)
'''

#Exercise 6
'''
num_of_stars=0

num_of_stars=int(input("Input number of stars to print"))

for num_of_stars in range(num_of_stars):
    print('*', end='')
'''

#Exercise 7

'''
import random

total_rounds=100
double_counts=0

for _ in range(total_rounds):
    die1=random.randint(1,6)
    die2=random.randint(1,6)

    if die1==die2:
        double_counts+=1

print(f"Out of {total_rounds} you rolled {double_counts} doubles")

'''


#Nested for loop (loop within a loop)
#Exercise 8

#A)
'''
for number in range(3) :
    print("-------------------------------------------")
    print("Outer loop iteration" + str(number))
    # inner loop
    for another_number in range(4):
        print("****************************")
        print("In inner loop iteration" + str(another_number))
'''

#B)
'''
for x in range(1,4):
    for y in range(1,4):    
        print('*', end='')
    print()
'''
#C)
'''
for x in range(1,4):
    print('*' * x)
'''

#Additional/Challenge Exercises
#Menu
#Exercise 9
'''
while True:
    print("Menu options")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Option 3")
    print("4. Quit")

    try:
        choice = int(input("Enter your choice (1/2/3/4): "))
        
        if choice == 1:
            print("1 selected")
        elif choice == 2:
            print("2 selected")
        elif choice == 3:
            print("3 selected")
        elif choice == 4:
            print("Quit selected")
            break
        else:
            print("Option not recognized")
    except ValueError:
        print("Enter integer")

'''  
#Guess the number (5 Guesses) 
#Exercise 10
'''
import random

hidden = random.randint(1,20)

guesses_Taken=0
max_guesses=5

print("Guess the number between 1 and 20")

while guesses_Taken<max_guesses:
    try:
        guess = int(input(f"Attempt {guesses_Taken+1} / {max_guesses}: Enter your guess: "))

        if guess < 1 or guess > 20:
            print("Please enter a number between 1 and 20")
            continue

        if guess == hidden:
            print(f"Congrats! You guessed the number {hidden} in {guesses_Taken+1} attempts!")
            break
        elif guess < hidden:
            print("Your guess is too low")
        else:
            print("Your guess is too higher")

        guesses_Taken+=1

    except ValueError:
        print("Invalid input, input again")
if guesses_Taken == max_guesses:
    print(f"sorry, ran out of attempts, The hidden number is {hidden}")
        
'''
