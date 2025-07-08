import random

# Prerequisites
# Defining the dictionary of words with difficulty levels, dictionary can be expanded later
words = {
    'Easy':     ['Lime', 'Salt'],
    'Normal':   ['Avocado', 'Onion', 'Tomato', 'Lemon'],
    'Hard':     ['Coriander', 'Garlic']
}

# Defining each difficulty level as a number
level_map = {'1': 'Easy', '2': 'Normal', '3': 'Hard'}

# Defining the tries allowed after incorrect guessed, tries allowed can be expanded later
tries_by_level = {'Easy': 5, 'Normal': 4, 'Hard': 3}

# Start
# Prompting the user for input, selecting a difficulty level by a number
print('\033[95mWelcome to Hangman!\nGuess the word, Guacamole ingredients!\033[0m\n')

while True:
    level_selection = input(
        f"Select a difficulty level (1-3)\n"
        "1. Easy\n"
        "2. Normal\n"
        "3. Hard\n"
        ": "
    ).strip()

    if level_selection in level_map:
        level = level_map[level_selection]
        print(f'You selected {level}. You have {tries_by_level[level]} tries.\n')
        break
    else:
        print("Invalid input. Please enter a number (1-3).")

# Randomly selecting the answer word from the dictionary based on the level selected by the user
word = random.choice(words[level]).lower()
tries = tries_by_level[level]
guessed = ['_'] * len(word)
incorrect_letters = []

# Prompting the user for input, selecting a letter of the word
while tries > 0 and '_' in guessed:
    print(f'\n\033[96mCurrent Word:\033[0m {" ".join(guessed)}')
    print(f'Incorrect guessed letters: {", ".join(incorrect_letters)}')
    guess = input('\033[96mGuess a letter: \033[0m').lower()
    print(f'Incorrect guesses remaining: {tries}')

    # Checking if the letter is invalid length and alphabet
    if len(guess) != 1 or not guess.isalpha():
        print('Input error, please input a alphabet.\n')
        continue

    # Checking if the letter is already guessed
    if guess in guessed or guess in incorrect_letters:
        print('The letter is already guessed.\n')
        continue

    # Checking if the letter is in the word
    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                # Change the first letter to uppercase
                guessed[i] = guess.upper() if i == 0 else guess
        print(f'Good job! "{guess}" is in the word.\n')
    # Checking if the letter is NOT in the word and add it to incorrect letters
    # Reducing tries
    else:
        incorrect_letters.append(guess)
        tries -= 1
        print(f'Sorry, "{guess}" is not in the word.\n')

# End
if '_' not in guessed:
    print(f'\033[95mCongratulations! You guessed the word: "{word.capitalize()}"\033[0m')
else:
    print(f'\033[91mGame over! The word was: "{word.capitalize()}"\033[0m')