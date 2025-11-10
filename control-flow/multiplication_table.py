# multiplication_table.py
# Generates a multiplication table for a given number using a for loop

# Prompt the user for a number
number = int(input("Enter a number to see its multiplication table: "))

# Generate and print the multiplication table from 1 to 10
for i in range(1, 11):
    print(f"{number} * {i} = {number * i}")
