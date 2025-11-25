"""
Program to store marks of student one by one
after taking inputs from the user.

"""
student = {}

subject1 = input("Enter subject1 : ")
marks1 = int(input("Enter marks of subject1 : "))
student.update({
    "subject1" : marks1
})

subject2 = input("Enter subject2 : ")
marks2 = int(input("Enter marks of subject2 : "))
student.update({
    "subject2" : marks2
})

subject3 = input("Enter subject3 : ")
marks3 = int(input("Enter marks of subject3 : "))
student.update({
    "subject3" : marks3
})

print(student)