import random

def play_game():
    print("\n🎲 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 10. Can you guess it?\n")

    # Generate a random number
    secret_number = random.randint(1, 10)
    attempts = 0  # Counter for number of guesses

    while True:
        try:
            guess = int(input("Enter your guess (1–10): "))
        except ValueError:
            print("❌ Please enter a valid number!")
            continue

        # Increase attempt counter
        attempts += 1

        # Match case logic (Python 3.10+)
        match guess:
            case _ if guess == secret_number:
                print(f"🎉 Congratulations, you guessed it in {attempts} tries!")
                break
            case _ if guess > secret_number:
                print("📈 Oops, your guess is a bit high. Try again!")
            case _ if guess < secret_number:
                print("📉 Nope, your guess is a bit low. Give it another shot!")

    # Offer to play again
    play_again = input("\nPlay again? (yes/no): ").strip().lower()
    if play_again in ["yes", "y"]:
        play_game()
    else:
        print("\nThanks for playing! 👋 Goodbye!")

# Start the game
play_game()
