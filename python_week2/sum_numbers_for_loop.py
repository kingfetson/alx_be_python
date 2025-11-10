# sum_numbers.py
# Program to calculate the sum of all numbers in a list

# Step 1: Create a list of numbers
numbers = [1, 5, 3, 9]

# Step 2: Initialize the total variable
total = 0

# Step 3: Use a for loop to add each number to total
for num in numbers:
    total += num  # same as total = total + num

# Step 4: Print the final total
print("The sum of all numbers in the list is:", total)
