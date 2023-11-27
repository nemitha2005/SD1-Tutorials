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
    guesses += guess

    for letter in secret:
        if letter in guesses:
            print('', letter, '', end='')
        else:
            print(' _ ', end='')


    if all(letter in guesses for letter in secret):
        print("\nCongratulations! You guessed the word!")
        break

    if turns == 0:
        print("\nSorry, you've run out of turns. The correct word was:", secret)
        break
            
