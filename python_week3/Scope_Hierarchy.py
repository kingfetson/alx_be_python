# Global variable
var = "Global variable"

def outer_function():
    # Enclosing variable (enclosing scope)
    var = "Enclosing variable"

    def inner_function():
        # Declare we want to use the enclosing variable
        nonlocal var
        print("Inside inner_function, enclosing var before change:", var)

        # Modify the enclosing variable
        var = "Modified enclosing variable"
        print("Inside inner_function, enclosing var after change:", var)

        # Access the global variable
        print("Inside inner_function, global var:", globals()['var'])

    inner_function()

    # Print enclosing variable after modification by inner_function
    print("Inside outer_function, enclosing var:", var)

# Print global variable before calling functions
print("Global var before function calls:", var)

# Call outer_function
outer_function()

# Print global variable after function calls
print("Global var after function calls:", var)

"""
Explanation (LEGB rule):
- L (Local): Variables defined inside inner_function (none in this case)
- E (Enclosing): 'var' in outer_function
- G (Global): 'var' defined in global scope
- B (Built-in): Not used in this example
"""
