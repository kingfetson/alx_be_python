import random

def play_game():
    print("\n🎲 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 10. Can you guess it?\n")

    secret_number = random.randint(1, 10)
    guess_count = 0
    guess = 0

    while guess != secret_number:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("❌ Please enter a valid number!")
            continue

        guess_count += 1

        # Match-case for hints
        match guess:
            case _ if guess == secret_number:
                print(f"🎉 Correct! You guessed the number in {guess_count} tries!")
            case _ if guess > secret_number:
                print("📈 Too high! Try again.")
            case _ if guess < secret_number:
                print("📉 Too low! Try again.")

    # Ask to play again
    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again in ["yes", "y"]:
        play_game()
    else:
        print("\nThanks for playing! 👋 Goodbye!")

# Start the game
play_game()
