import random


def play_game():
    words = ['apple', 'banana', 'cherry', 'orange', 'pear']
    secret_word = random.choice(words)
    guessed_letters = []
    attempts = 5

    print("Welcome to the Word Guessing Game!")
    print("Guess the letters to reveal the secret word.")

    while attempts > 0:
        print("\nSecret word: " +
              ''.join([letter if letter in guessed_letters else '_' for letter in secret_word]))
        print("Attempts left: " + str(attempts))

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("Correct guess!")
            if all(letter in guessed_letters for letter in secret_word):
                print("Congratulations! You guessed the word: " + secret_word)
                return
        else:
            print("Wrong guess!")
            attempts -= 1

    print("Game over! You ran out of attempts. The secret word was: " + secret_word)


play_game()
