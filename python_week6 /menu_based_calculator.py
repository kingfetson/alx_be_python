from robust_division_calculator import safe_divide

def main():
    while True:
        print("\n====== SAFE CALCULATOR MENU ======")
        print("1. Add two numbers")
        print("2. Subtract two numbers")
        print("3. Multiply two numbers")
        print("4. Divide two numbers (safe)")
        print("5. Exit")
        print("==================================")

        choice = input("Enter your choice (1–5): ")

        # --- Exit ---
        if choice == "5":
            print("Goodbye!")
            break

        # --- Validate menu selection ---
        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice. Please select 1–5.")
            continue

        # --- Get numbers ---
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")

        # Convert numbers for operations 1–3
        try:
            a = float(num1)
            b = float(num2)
        except ValueError:
            print("Error: Please enter numeric values only.")
            continue

        # -----------------------------
        # Operation Handling
        # -----------------------------

        if choice == "1":  # Add
            result = a + b

        elif choice == "2":  # Subtract
            result = a - b

        elif choice == "3":  # Multiply
            result = a * b

        elif choice == "4":  # Divide using safe_divide()
            result = safe_divide(num1, num2)   # keep using string input here
        # -----------------------------

        # Your formatting block EXACTLY as requested
        if isinstance(result, float):
            print("Result:", f"{result:.2f}")
        else:
            print("Result:", result)


if __name__ == "__main__":
    main()
