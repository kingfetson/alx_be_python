def counting_function():
    count = 10  # local variable in counting_function
    print("Inside counting_function, count =", count)

def logging_function():
    count = 5  # local variable in logging_function
    print("Inside logging_function, count =", count)

# Call both functions
counting_function()
logging_function()
