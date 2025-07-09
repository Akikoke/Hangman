import random

# Dictionary of words with difficulty levels, dictionary can be expanded later
words = {
    'Easy':     ['pepper', 'salt'],
    'Normal':   ['rosemary', 'oregano'],
    'Hard':     ['coriander', 'cinnamon']
}

# Difficulty level as a number
level_map = {'1': 'Easy', '2': 'Normal', '3': 'Hard'}

# Tries allowed after incorrect guessed, tries allowed can be expanded later
tries_by_level = {'Easy': 5, 'Normal': 4, 'Hard': 3}

# Game Start
# Prompt the user to select a difficulty level using a number
print('Welcome to Hangman!\nGuess the word, Guacamole ingredients!')

while True:
    level_selection = input(
        f"Select a difficulty level (1-3)\n"
        '1. Easy\n'
        '2. Normal\n'
        '3. Hard\n'
        ': '
    ).strip()

    if level_selection in level_map:
        level = level_map[level_selection]
        print(f'You selected {level}. You have {tries_by_level[level]} tries.\n')
        break
    else:
        print("Invalid input. Please enter a number (1-3).")

# Select a random answer word from the dictionary
word = random.choice(words[level]).lower()
tries = tries_by_level[level]
guessed = ['_'] * len(word)
incorrect_letters = []

# Prompt the user to input a letter
while tries > 0 and '_' in guessed:
    print(f'Current Word: {" ".join(guessed)}')
    print(f'Incorrect guessed letters: {", ".join(incorrect_letters)}')
    guess = input('Guess a letter: ').lower()
    print(f'Incorrect guesses remaining: {tries}')

    # If the letter is invalid length and alphabet
    if len(guess) != 1 or not guess.isalpha():
        print('Input error, please input a alphabet.\n')
        continue

    # If the letter is already guessed
    if guess in guessed or guess in incorrect_letters:
        print('The letter is already guessed.\n')
        continue

    # If the letter is in the word
    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                # Change the first letter to uppercase
                guessed[i] = guess.upper() if i == 0 else guess
        print(f'Good job! "{guess}" is in the word.\n')
    # If the letter is not found in the word, add it to the incorrect letters list.
    # Reducing tries
    else:
        incorrect_letters.append(guess)
        tries -= 1
        print(f'Sorry, "{guess}" is not in the word.\n')

# End
if '_' not in guessed:
    print(f'Congratulations! You guessed the word: "{word.capitalize()}"')
else:
    print(f'Game over! The word was: "{word.capitalize()}"')