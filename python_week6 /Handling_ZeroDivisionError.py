def divide_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        result = num1 / num2
        print(f"Result: {result}")

    except ZeroDivisionError:
        print("Error: You cannot divide a number by zero.")

    except ValueError:
        print("Error: Please enter valid numbers.")


# Run the function
divide_numbers()
