#example 1

""" summary
loops(for, while)
comprehensions(lists, dictionary comprehensions)
"""
# if, elif, else
age = 24
if age < 18:
    print("you are a child")
    
elif age > 65:
    print("you are a senior citizen")
    
else:
    print("you are a youth")
    
#example 2
#90, above is excellent, Equal 80 and above is very good, if 70, good, otherwise, not good.

grade = 88
if grade >= 90:
    print("excellent")
    
elif grade >= 80:
    print("very good")
    
elif grade >= 70:
    print("good")
    
else:
    print("not good")
    

#exercise

    """_summary_line
    write a python script to determine the price 
    of a movie based on age
    condition;
    children under 13 get discount for price = shs1000
    
    """

# Take age input from the user
age = int(input("Enter your age: "))

# Determine the price based on the age
if age < 13:
    print("price = shs1000")
elif 13 <= age < 18:
    print("price = shs1500")
elif 18 <= age < 65:
    print("price = shs2000")
else:
    print("price = shs5000")


# for loop (for, while)
    """_summary_
    for loop iterates over a sequence (lists, tuple, dictionary, set, string)
    the while loop repeats as long as a condition is true
    """
    # Example 3
    cars = ["Tesla", "Audi", "BMW", "Jeep", "RangeRover"]
    for car in cars:
        print(car)


#exercise
    """_summary_
    1. create your own list of favorite colors usinf for loop
    2. create a reverse of the input 12345 to be 54321 using a while loop
    """
    
    # List to store favorite colors
favorite_colors = []

# List of colors to choose from
colors = ['red', 'blue', 'green', 'yellow', 'purple']

# Loop through the list of colors and add them to the favorite colors list
for color in colors:
    favorite_colors.append(color)

print("My favorite colors are:", favorite_colors)