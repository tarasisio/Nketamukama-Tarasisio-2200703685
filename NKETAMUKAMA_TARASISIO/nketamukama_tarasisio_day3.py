""" Summary
multiplication
Exponentaition
division
addition
subtraction
"""

"""
#example of python logical operators
    _summary_
    Name of the operator         example
    and                         and &&
    or                          or
    not                         not 
    
    #Examole of membership operators
    Name          Symbol with example
    not in       x not in y
    in            x in y
    
    #examples of bitwise operators
    Name             Symbol with example
    AND              &
    OR               |
    XOR              ^
    NOT              ~
    
    #python cases
    Name            Symbol with example
    lower case      lower_case
    upper case      UPPER_CASE
    camel case      camelCase
    pascal case     PascalCase
    snake case      snake_case
    kebab case      kebab-case
    """
    #comprehensions (lists, dictionary comprehensions)
"""_summary_
    comprehensions provide a concise way to create lists and dictionaries
    what is the symbol for 
    lists              [] square brackets  
    dictionaries       {} curly brackets  used to store data values in key value pairs
    """
    #Example 1 Basic List Comprehension
    #create a list of numbers from 1 to 10
list_of_squares=[x**2 for x in range(10)]
print(list_of_squares)

#exercise
#create a list of even squares in the range of 20

even_squares = [x**2 for x in range(21) if x % 2 == 0]
print(even_squares)



#example 2 Dictionary Comprehension
# create a dictionary for favorite cars and count the lengths of characters

favorite_cars = ["BMW", "Jeep","Mercedes","fordrapter"]
car_length={car:len(car) for car in favorite_cars}
print(car_length)

#exercise2: create a list of tuple where each tuple contains a number and its cube in the range of 1 to 10 using a dictionary comprehension
cube_tuples = [(x, x**3) for x in range(1, 11)]
print(cube_tuples)
