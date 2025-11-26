from robust_division_calculator import safe_divide

def main():
    print("Welcome to the Safe Division Calculator")

    numerator = input("Enter the numerator: ")
    denominator = input("Enter the denominator: ")

    result = safe_divide(numerator, denominator)
    print("Result:", result)

if __name__ == "__main__":
    main()
