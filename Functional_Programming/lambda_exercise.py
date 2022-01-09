#Task1: Square
mylist=[5,4,3]
#Return square of each item 
print(list(map(lambda item: item*item,mylist)))

#Task-2: List Sorting
a=[(0,9),(4,3),(9,9),(10,-1)]
#Sort the list based on the second value of each tuple 
a.sort(key=lambda item :item[1])
print(a)
