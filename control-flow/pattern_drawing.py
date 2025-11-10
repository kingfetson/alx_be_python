# pattern_drawing.py
# Draws a square pattern of asterisks (*) using a while loop and a nested for loop

# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop to iterate through each row
while row < size:
    # Use a for loop to print asterisks in each row
    for i in range(size):
        print("*", end="")
    print()  # Move to the next line after finishing one row
    row += 1
