# Define the custom exception
class ValueTooHighError(Exception):
    """Exception raised when the input value is greater than 100."""
    pass


def check_number():
    try:
        num = float(input("Enter a number: "))
        if num > 100:
            raise ValueTooHighError("The value is too high! It must be 100 or less.")
        print(f"You entered: {num}")

    except ValueTooHighError as e:
        print(f"Error: {e}")

    except ValueError:
        print("Invalid input! Please enter a numeric value.")


# Run the program
check_number()
