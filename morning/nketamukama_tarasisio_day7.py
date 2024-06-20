#Inheritance and polymorphism
"""

Inheritance and method overriding
polymorphism and method resolution
order
Abstract classes and interfaces

"""

#Inheritance and method overriding 
"""
--description
Inheritance and method overriding allows a class(child class) to 
inherit attributes from another class(parent class).

Key concepts
Base class(parent classes): class whose properties are inherited by another class.
Derived classes (child class): Class that inherits attributes and properties from parent class

"""
#example 1
class Animal:
    def speak(self):
        return "mweeeee"
    
class Dog(Animal):
    def speak(self):
       return "barks"
   
   
    
class Cat(Animal):
    def speak(self):
       return "meow"
   
   
def make_Animal_peak(animal):
    print (animal.speak())
    
make_Animal_peak(Cat())

#exercise create a simple application to manage different types of vehicles. implement 
#derived class to demonstrate inheritance and polymorphism.
"""
Requirements
1. base class to vehicle
attributes: make, model and year
method: display_info()

2. Derived classes
Car: inherit from Vehicle
attributes: number of doors
override method: display_info()

motorcycle: inherit from Vehicle
attributes: type of bike(cruiser, sport, touring)
override method: display_info()

#exercise 2

create a function that accepts a list of vehicle objects and call their display_info() method
to print the details of each vehicle.
"""

# Base class
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def display_info(self):
        print(f"Vehicle Info: {self.year} {self.make} {self.model}")

# Derived class Car
class Car(Vehicle):
    def __init__(self, make, model, year, number_of_doors):
        super().__init__(make, model, year)
        self.number_of_doors = number_of_doors
    
    def display_info(self):
        print(f"Car Info: {self.year} {self.make} {self.model}, Doors: {self.number_of_doors}")

# Derived class Motorcycle
class Motorcycle(Vehicle):
    def __init__(self, make, model, year, bike_type):
        super().__init__(make, model, year)
        self.bike_type = bike_type
    
    def display_info(self):
        print(f"Motorcycle Info: {self.year} {self.make} {self.model}, Type: {self.bike_type}")

# Function to display info of a list of vehicles
def display_vehicles_info(vehicles):
    for vehicle in vehicles:
        vehicle.display_info()

# Example usage
if __name__ == "__main__":
    car1 = Car("Toyota", "Camry", 2020, 4)
    car2 = Car("Honda", "Civic", 2018, 2)
    motorcycle1 = Motorcycle("Harley-Davidson", "Street 750", 2019, "Cruiser")
    motorcycle2 = Motorcycle("Yamaha", "YZF-R3", 2021, "Sport")

    vehicles = [car1, car2, motorcycle1, motorcycle2]
    display_vehicles_info(vehicles)
    
    
    # reading and writing files in python
    """
    
    """
    # 1. working with text files, open, read, write and close
    # note: python provides inbuilt functions to handle text files
    """
    opening file: open() function (r, w, a, r+)
    reading file: read() function
    writing file: write() function
    closing file: close() function
    """
    
    # example3; write a file and read a file
    
    with open("Taras.txt", "w") as file:
        file.write("I am Taras and i love python. \n")
        file.write("iI used python for automation")
        
        # Reading a text file
        with open ("Taras.txt", "r") as file:
            content = file.read()
            print(content)
            
        # Hanhling csv files
    """
    CSV (comma separated values) file widely for data exchange.
    key concept:
    Read csv file: using csv.reader()
    Write csv file: using csv.writer()
    Dictionary reader: using csv.DictReader()
    """
    # Example 4: writing and reading csv files
    
    import csv
    
    # Writing a CSV file
    with open("Taras.csv", "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Name", "position", "course"])
        writer.writerow(["Taras", "student", "BSSE"])
        writer.writerow(["Jeff", "Lecturer", "BSSE"])
        
        # Reading a CSV file
        with open ("Taras.csv", "r") as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                print(row)
                
# JSON and XML file processing
    """
    JSON (JavaScript Object Notation) andXML (Extensible Markup Language)are formats used to structure data.
    key concept:
    Read JSON file: using json.load()
    Write JSON file: using json.dump()
    loading JSON file: json.loads()
    parsing JSON Data: using json.loads() for handling JSON strings
    
    """
    
    # writing a JSON file
    import json
    Student_data = {
        "Name": "Taras",
        "Age": 22,
        "Course": "BSSE"
    }
    with open("Taras.json", "w") as json_file:
        json.dump(Student_data, json_file)
        
    # reading a JSON file
    with open("Taras.json", "r") as json_file:
        Student_data = json.load(json_file)
        print(Student_data)
        
    # Exercise2: write and read the XML file

    import xml.etree.ElementTree as ET

# Write XML file
root = ET.Element("root")
rectangle = ET.SubElement(root, "rectangle")
ET.SubElement(rectangle, "length").text = "5"
ET.SubElement(rectangle, "width").text = "3"

tree = ET.ElementTree(root)
tree.write("rectangle.xml")

# Read XML file
tree = ET.parse("rectangle.xml")
root = tree.getroot()
rectangle = root.find("rectangle")
length = rectangle.find("length").text
width = rectangle.find("width").text
print(length, width)  # Output: 5 3


# Exercise 3: using abstraction, calculate the area and perimeter of a rectangle
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Usage:
rect = Rectangle(5, 3)
print(rect.area())  # Output: 15
print(rect.perimeter())  # Output: 16