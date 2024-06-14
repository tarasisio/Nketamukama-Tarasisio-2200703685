Student_dict{
    "name": "Taras",
    "age": 24,
    "gender": "male",
    "country": "Uganda",
    "technology": "AI"
}
#Access values
#modify age and technology
# Access values
name = Student_dict["name"]
age = Student_dict["age"]
gender = Student_dict["gender"]
country = Student_dict["country"]
technology = Student_dict["technology"]

# Modify age and technology
Student_dict["age"] = 25  # Change age to 25
Student_dict["technology"] = "Machine Learning"  # Change technology to "Machine Learning"

# Print modified dictionary
print("\nModified dictionary:")
print(Student_dict)

#remove key-value












#use the get method to get the values
print(Student_dict.get("technology"))



# use update to change course and add a new key "whatsapp number" to the dictionary
