# Simple Number Guessing Game

secret_number = 7
guess_count = 0
guess = 0

print("Welcome to the Number Guessing Game!")
print("Try to guess the secret number between 1 and 10.\n")

while guess != secret_number:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("❌ Please enter a valid number!")
        continue

    guess_count += 1

    if guess < secret_number:
        print("📉 Too low! Try again.")
    elif guess > secret_number:
        print("📈 Too high! Try again.")

print(f"🎉 You guessed it in {guess_count} tries!")
