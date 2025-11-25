# Global variable
message = "Hello from the global scope!"

def show_message():
    # Local variable with the same name
    message = "Hello from the local scope!"
    print("Inside function:", message)

# Call the function
show_message()

# Print the global variable
print("Outside function:", message)
