# sum_numbers_game.py
# Interactive program to calculate the sum of numbers with replay option

def play_sum_game():
    print("\nWelcome! Let's calculate the sum of your numbers.")

    # Step 1: Ask user for input
    user_input = input("Enter numbers separated by spaces (e.g., 1 5 3 9): ")

    # Step 2: Convert the input string into a list of integers
    try:
        numbers = [int(num) for num in user_input.split()]
    except ValueError:
        print("❌ Please enter only numbers separated by spaces.")
        return  # Exit current round

    # Step 3: Initialize total
    total = 0

    # Step 4: Use a for loop to calculate the sum
    for num in numbers:
        total += num

    # Step 5: Print the result
    print("✅ The sum of all numbers you entered is:", total)


# Main loop to play again
while True:
    play_sum_game()

    # Ask if user wants to play again
    replay = input("\nDo you want to calculate another sum? (yes/no): ").strip().lower()
    if replay not in ["yes", "y"]:
        print("\nThanks for playing! Goodbye! 👋")
        break
