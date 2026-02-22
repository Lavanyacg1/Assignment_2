import random

# Function to play the guessing game
def play_game(best_score):
    secret_number = random.randint(1, 100)
    attempts = 7

    print("\nI have selected a number between 1 and 100.")
    print("You have 7 attempts to guess it.")

    for attempt in range(1, attempts + 1):
        try:
            guess = int(input(f"\nAttempt {attempt} - Enter your guess: "))

            if guess < 1 or guess > 100:
                print("Please guess a number between 1 and 100.")
                continue

            if guess == secret_number:
                print(f" Congratulations! You guessed the number in {attempt} attempts.")

                if best_score is None or attempt < best_score:
                    best_score = attempt
                    print(" New Best Score!")

                return best_score

            elif guess > secret_number:
                print("Too HIGH!")
            else:
                print("Too LOW!")

            # Bonus hint: close guess
            if abs(guess - secret_number) <= 5:
                print(" Hint: You are VERY close!")

            print(f"Attempts remaining: {attempts - attempt}")

        except ValueError:
            print("Invalid input! Please enter an integer.")

    # If all attempts are used
    print(f"\n You've used all attempts. The number was {secret_number}.")
    return best_score


# Main program
def main():
    best_score = None

    while True:
        best_score = play_game(best_score)

        if best_score:
            print(f" Best Score so far: {best_score} attempts")

        choice = input("\nDo you want to play again? (yes/no): ").lower()
        if choice != "yes":
            print("Thanks for playing! ")
            break


# Run the game
main()