"""
Count number of students with grade A in the tuple.

"""

tup1 = ("C", "D", "A", "A", "B", "B", "A")
gradeCount = tup1.count("A")
print("Number of students with grade A : ", gradeCount)

"""
Store the above tuple in a list and sort them in ascending order.

"""

list1  = list(tup1)
list1.sort()
print(list1)