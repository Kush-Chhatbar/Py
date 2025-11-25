"""
Methods related to Dictionary Datatype.

"""

student = {
    "name" : "Kush Chhatbar",
    "subjects" : {
        "physics" : 56,
        "chemistry" : 45,
        "mathematics" : 39
    },
    "age" : 22,
}

print(student.keys())
print(student.values())
print(student.items())
print(student.get("name"))

student.update({"city" : "Ahmedabad"})
print(student)