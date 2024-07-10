#Defining functions
# function syntax and parameters
#return values
# lambda function
# Functions in python are defined using a def keyword, followed by a function name
# parenthesis(), inside a parenthesis, you put a parameter name and a colon
# example
def multiply(a,b):
    return a*b
result=multiply(5,10)
print(result)

#example 2
def get_coordinates():
    return 10, 20

x, y = get_coordinates()
print(x, y)

# exercise 1; define a function greet with a parameter name set to guest and print a message 
#i am a software programmer
def greet(name="guest"):
    print(f"Hello, {name}! I am a software programmer.")

greet("Taras")

def greet(name="guest"):
    print(f"I am a software programmer., {name}")
greet()

#example 3 C
def get_name_and_position():
    name = "Taras"
    position = "i am a software programmer"
    return name, position

name, position = get_name_and_position()
print(name, position)

# Exercise; return multiple values of your name and age
def get_name_and_age():
    name = "Taras,"
    age = 23
    return name, age

name, age = get_name_and_age()
print(name, age)

""""_summary_"
    def: keyword to define a function
    function name: name of the function
    parameters: optional, arguments passed to the function
    docstring: optional, description of the function purpose
    return: optional, returns a value from the function
    """
    #syntax for defining a function
    # def function_name(parameters):
    #     docstring
    #     function body
    #     return value
    
    
    #Lambda functions
    #lambda function are small anonymous functions defined using the lambda keyword.\ 
    #they are restricted to a single expression
    
    #syntax for lambda function
    #lambda parameters: expression
    
    #example 5
def add(x, y):
        return x +y
    
print(add(2, 3))

    #example 6: use cases of lambda function for sorting
coordinates = [(1, 2), (2, 3), (3, 1), (5, 0)]
coordinates.sort(key=lambda coordinates: coordinates[1])
print(coordinates)


#map, filter and reduce
# example6: get the squares of 1 to five using map, filter and reduce

number_squares = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, number_squares))
print(squares)

#example 7; define a function to get user info that accepts arbitrary keyword arguments and print each key value pair
def get_user_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

get_user_info(name="Taras", age=23, occupation="software Engineer")
get_user_info(username="Taras official", email="tnketamukama@gmail.com", country="Uganda")


# Example 8: How to handle **kwargs in a function

def Taras(a, b, **kwargs):
    print(f"a: {a} + b: {b}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Example usage:
Taras(1, 2, username="Taras official", email="taras@gmail.com", country="Uganda")
