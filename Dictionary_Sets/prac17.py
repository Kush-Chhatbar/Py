""" 
Methods related to Set Datatype.

"""

#add() method.
collection = set()
collection.add(1)
collection.add(2)
collection.add(2)
print(collection)

#remove() method.
collection.remove(2)
print(collection)

#clear() method.
collection.clear()
print(collection)

#pop() method.
collection.add("A")
collection.add("V")
collection.pop()
print(collection)

#union() method.
set1 = {1,2,3}
set2 = {2,3,4}

print(set1.union(set2))

#intersection() method.
print(set1.intersection(set2))