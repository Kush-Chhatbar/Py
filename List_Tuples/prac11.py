"""
Methods related to List Datatype

"""

#append() method
list = [2,4,6]
list.append(8)
print(list)

#sort() method
list1 = [2,5,8,1]
list1.sort()
list.sort(reverse=True)   #descending order.
print(list1, list)

#reverse() method
list2 = ['a', 'c', 'd', 'b']
list2.reverse()
print(list2)

#insert() method
list2.insert(3, 'e')
list2.insert(1, 'f')
print(list2)

#remove() method
list3 = ['a', 'b', 'a', 'c', 'b']
list3.remove('a')
print(list3)

#pop() method
list3.pop(2)
print(list3)