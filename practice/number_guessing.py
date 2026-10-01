# practice/number_guessing.py

import random

def play_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    print("=== Number Guessing Game ===")
    print("I'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it!\n")

    while attempts < max_attempts:
        attempts += 1
        try:
            guess = int(input(f"Attempt {attempts}/{max_attempts} - Enter your guess: "))
        except ValueError:
            print("Please enter a valid integer.")
            attempts -= 1
            continue

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts!")
            return

    print(f"Game over! The correct number was {secret_number}.")

if __name__ == "__main__":
    play_game()