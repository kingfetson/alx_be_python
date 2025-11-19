# arithmetic_operations.py

def perform_operation(num1: float, num2: float, operation: str):
    """
    Perform basic arithmetic operations.

    Parameters:
    - num1 (float): First number
    - num2 (float): Second number
    - operation (str): 'add', 'subtract', 'multiply', 'divide'

    Returns:
    - float: Result of the operation
    - str: Message if division by zero occurs or invalid operation
    """
    operation = operation.strip().lower()

    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Cannot divide by zero"
        return num1 / num2
    else:
        return "Invalid operation"
