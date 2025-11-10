import random

def play_game():
    print("\n🎲 Welcome to the Number Guessing Game!")
    print("Choose your difficulty level:")
    print("1. Easy (1–10)")
    print("2. Medium (1–50)")
    print("3. Hard (1–100)")

    # Get difficulty level
    while True:
        level = input("Enter 1, 2, or 3: ").strip()
        match level:
            case "1":
                low, high = 1, 10
                level_name = "Easy"
                break
            case "2":
                low, high = 1, 50
                level_name = "Medium"
                break
            case "3":
                low, high = 1, 100
                level_name = "Hard"
                break
            case _:
                print("❌ Invalid choice! Please enter 1, 2, or 3.")

    print(f"\nYou selected {level_name} mode! I'm thinking of a number between {low} and {high}.\n")

    secret_number = random.randint(low, high)
    attempts = 0  # Number of guesses

    # Game loop
    while True:
        try:
            guess = int(input(f"Enter your guess ({low}–{high}): "))
        except ValueError:
            print("⚠️ Please enter a valid number!")
            continue

        # Increment attempt counter
        attempts += 1

        # Match-case comparison
        match guess:
            case _ if guess == secret_number:
                print(f"🎉 Correct! You guessed the number in {attempts} attempts!")
                break
            case _ if guess > secret_number:
                print("📈 Too high! Try again.")
            case _ if guess < secret_number:
                print("📉 Too low! Try again.")

    # Ask to play again
    play_again = input("\nWould you like to play again? (yes/no): ").strip().lower()
    if play_again in ["yes", "y"]:
        play_game()
    else:
        print("\nThanks for playing! 👋 See you next time!")

# Start the game
play_game()
