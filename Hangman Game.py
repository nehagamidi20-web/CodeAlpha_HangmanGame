# Import random module
import random
# List of words
words = ["apple","python","school","computer","program"]
# Select a random word
word = random.choice(words)
# Store guessed letters
guessed_letters = []
# Count wrong guesses
wrong_guesses = 0
# Maximum number of wrong guesses
max_guesses = 6
# Display welcome message
print("welcome to hangman!")
print("guess the word one letter at a time.")
# Main game loop
while wrong_guesses < max_guesses:
    # Create the word display
    display = ""
    # Check each letter in the word
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_"
    # Display current word
    print("\nword:",display)
    # Display wrong guesses
    print("wrong guesses:",wrong_guesses, "/",max_guesses)
    # Check whether the word is completely guessed
    if all(letter in guessed_letters for letter in word):
        print("congratulations! you guessed the word:",word)
        break
    # Get a letter from the user
    guess = input("enter a letter:").lower()
    if len(guess) !=1 or not guess.isalpha():
        print("please enter only one letter.")
        continue
    # Check whether the letter was already guessed
    if guess in guessed_letters:
        print("you already guessed that letter.")
        continue
    # Add the letter to guessed letters
    guessed_letters.append(guess)
    # Check whether the guess is correct
    if guess in word:
        print("correct guess!")
    else:
        print("wrong guess!")
        wrong_guesses +=1
# Display game-over messageS
else:
    print("\nGame over!")
    print("The word was:",word)
