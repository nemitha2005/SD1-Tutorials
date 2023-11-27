secret = 'water'
turns = 6
guesses = ''

space=len(secret)
print("Let's play Guess the Word")
print(f'You have 6 turns to guess the word!')
print(" _ " * space)


while turns >0:
    guess=input("Guess a Letter ")
    turns -=1
    

    for letter in secret:
        if letter in guess:
            print('', letter, '', end='')
        else:
            print(' _ ', end='')

