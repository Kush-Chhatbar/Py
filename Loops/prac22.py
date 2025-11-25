"""
While loop practice questions.

"""

"""
Print numbers from 1 to 100.

"""
# count = 1
# while count <= 100:
#     print(count)
#     count += 1

"""
Print numbers from 100 to 1.

"""
# count = 100
# while count >= 1:
#     print(count)
#     count -= 1

"""
Print multiplication table of a number n.

"""

# count = 1
# num = int(input("Enter a number to write a table : "))
# while count <= 10:
#     print(num , "X", count, "=", num*count)
#     count +=1


"""
Print the elements of a list using a loop.

"""

numbers = [1,4,9,16,25,36,49,64,81,100]

# count = 1
# while count <= len(numbers):
#     print(numbers[count-1])
#     count += 1

"""
Search for a number x in the tuple using loop.

"""

value = int(input("Enter a number to search for : "))
count = 0
while count < len(numbers):
    if(numbers[count] == value):
        print("Found at index", count)
        break
    else:
        print("finding..")
    count += 1
print("End of loop.")