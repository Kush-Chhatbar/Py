"""
Check if the string contains palindorme of elements.

"""

str1 = [1,2,3,2,1]
str2 = str1.copy()
str2.reverse()

if(str1 == str2):
    print("provided string contains palindrome")
else:
    print("provided string does not contain palindrome")

str3 = [1, "abc", "abc", 1]
str4 = str3.copy()
str4.reverse()

if(str3 == str4):
    print("provided string contains palindrome")
else:
    print("provided string does not contain palindrome")
