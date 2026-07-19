# python functions
# what is a function?
"""a function is a block of code that performs a specific task. It can take inputs, 
process them, and return an output.
Functions help in organizing code, making it reusable, and improving readability."""

#my_function is a simple function that takes two numbers as input and returns their sum.
def my_function(num1, num2):
    """This function takes two numbers as input and returns their sum."""
    return num1 + num2      
#"This line will not be executed because it is after the return statement.
my_function(8, 3)  # Calling the function with arguments 8 and 3
print(my_function(8, 3))  # Output: 11

#betterprint is a function that takes a string as input and prints it in a formatted way.
def betterprint(string):
    print(f"Formatted output: {string}")

betterprint("Hello, World!")  # Output: Formatted output: Hello, World!
print(betterprint("Hello, World!"))  # Output: Formatted output: Hello, World! and None