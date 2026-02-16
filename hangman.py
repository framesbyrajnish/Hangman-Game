import random

# simple word list
words = ["apple", "chair", "tiger", "bread", "plant"]

# random word choose karna
word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong = 6

print("Welcome to Hangman Game!")
print("You have 6 wrong chances.\n")

while wrong_guesses < max_wrong:
    display_word = ""
    
    # show guessed letters
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    
    print("Word:", display_word)
    
    # check win
    if "_" not in display_word:
        print("Congratulations! You guessed the word:", word)
        break
    
    guess = input("Enter a letter: ").lower()

if len(guess) != 1:
    print("Please enter only one letter.\n")
  

    
    if guess in guessed_letters:
        print("You already guessed that letter.\n")
    elif guess in word:
        print("Good guess!\n")
        guessed_letters.append(guess)
    else:
        print("Wrong guess!\n")
        wrong_guesses += 1
        guessed_letters.append(guess)
        print("Wrong attempts left:", max_wrong - wrong_guesses)
        print()

if wrong_guesses == max_wrong:
    print("Game Over! The word was:", word)
