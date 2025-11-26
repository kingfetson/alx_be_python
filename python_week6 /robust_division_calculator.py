def safe_divide(numerator, denominator):
    """
    Safely divide numerator by denominator with error handling.
    
    Parameters:
    numerator (str or float): The numerator value.
    denominator (str or float): The denominator value.

    Returns:
    str: Result of division or an error message.
    """
    try:
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    try:
        result = num / den
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    return f"The result of the division is {result}"
