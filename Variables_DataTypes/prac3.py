"""
Print average of 2 floating numbers.

"""

num1 = float(input("Enter num1 : "))
num2 = float(input("Enter num2 : "))

sum = num1 + num2
average = sum / 2

print("Average of ", num1, "and" , num2 , "is : ", round(average, 2))