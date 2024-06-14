# Factorial calculation using recursion

def factorial(n):
    """
    Calculate the factorial of a number using recursion.
    
    Parameters:
    n (int): The number to calculate the factorial of. Must be a non-negative integer.
    
    Returns:
    int: The factorial of the number.
    """
    # Base case: if n is 0 or 1, the factorial is 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case: n! = n * (n-1)!
        return n * factorial(n - 1)

# Input: number to calculate the factorial of
number = 5

# Ensure the input number is non-negative
if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    # Calculate the factorial
    result = factorial(number)
    
    # Output the result
    print(f"The factorial of {number} is {result}")

# Example with a different input
number2 = 7

# Ensure the input number is non-negative
if number2 < 0:
    print("Factorial is not defined for negative numbers.")
else:
    # Calculate the factorial
    result2 = factorial(number2)
    
    # Output the result
    print(f"The factorial of {number2} is {result2}")

# Calculate factorial for a list of numbers
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Create an empty dictionary to store the results
factorials = {}

# Loop through each number in the list
for num in numbers:
    # Ensure the number is non-negative
    if num < 0:
        print(f"Factorial is not defined for negative numbers: {num}")
    else:
        # Calculate the factorial and store in the dictionary
        factorials[num] = factorial(num)

# Output the results
for num, fact in factorials.items():
    print(f"The factorial of {num} is {fact}")
