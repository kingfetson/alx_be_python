import random

# Generate a list of 10 random numbers between 1 and 10
random_numbers = [random.randint(1, 10) for _ in range(10)]

# Convert the list to a set to remove duplicates
unique_numbers = set(random_numbers)

# Display the unique numbers
print("Random numbers:", random_numbers)
print("Unique numbers:", unique_numbers)
