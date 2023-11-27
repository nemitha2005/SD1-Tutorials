# Question 05....

'''line = ' more white space '
print(line)print(line.strip())
print(line)


# Finding a data on string....
guesses = 'abcde'
letter = 'z'
if letter in guesses:
     print("letter")
else: 
    print(' _ ')

#Traversing a string
name = "liz"
for char in name:
    print(char.upper()*3)


message = "Testing"
count = 0
for character in message:
    print(f'Index:{count}, Character:{character}')
    count += 1'''

'''secret_word='water'
turns=6
print(" Start of the guess the word game. ")
gueesing_word='_',*len(secret_word)
print(gueesing_word)

secret_word = 'water'
turns = 6
guessed_word = '_' * len(secret_word)

print("Start of the guess the word game.")
print(guessed_word, end=" ")'''

# Initialize the secret word, turns, and guessed letters
secret = 'water'
turns = 6
guesses = ''
guessed_word = '_' * len(secret)

# Display the introduction message
print("Let's play Guess the Word")
print(f'You have {turns} turns to guess the word!')
print(guessed_word)

# Game logic (to be continued)



