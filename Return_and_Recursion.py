#return data from a function
def add_numbers(x, y):
    """This function takes two numbers as input and returns their sum."""
    return x + y   
Sum=add_numbers(5, 3)  # Calling the function with arguments 5 and 3
print(Sum)  # Output: 8



#recursion
def factorial(n):
    """This function takes a number as input and returns its factorial using recursion."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120

#or you can use a for loop to calculate the factorial of a number
def factorial_iterative(n):
    """This function takes a number as input and returns its factorial using an iterative approach."""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result   
print(factorial_iterative(5))  # Output: 120

#or you can use a while loop to calculate the factorial of a number
def factorial_conditional(n):
    """This function takes a number as input and returns its factorial using a conditional approach."""
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

print(factorial_conditional(5))  # Output: 120

