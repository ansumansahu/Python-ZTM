# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 19:40:16 2021

@author: Ansh
"""

#list: an ordered sequence of objects which can be of any datatype . also list is a data structure

list1=['a','name',28,True,65,69,420,'xy',False,6.9]
print(list1[3])
print(list1[::2])
#unlike strings, lists are muttable
#but list slicing doesn't change the list, we copy 
list1[0]='alpha'
print(list1)

my_list = [1,2,3]
bonus = my_list + [5]
my_list[0] = 'z'
print(my_list) #'z',2,3
print(bonus) #1,2,3,5

#matrix (list within list)
m=[[1,5,1],
   [0,1,0],
   [1,0,1]]

m[0][1]=0
print(m)


#list methods
#adding
m=[6,23,7,2,78,24,7,89]
m.append(69) 
# if we try to append [69,79] something like this it'll add list inside the pre-existing list and not those two integers to the list (try for yourself)
m.insert(0,10)
print(m)
m.extend([12,24]) 
#here it'll add both integers to the existing list
print(m)

#removing
m.pop() #removes last index
m.pop(0) #removes specific index
m.remove(69) #removes specific value from list
print(m)
print(m.pop()) #gives back the popped off value
print(m)

#sorting
m.sort()
print(m)

#indexing
print(m.index(7))
print(89 in m) #in is a keyword here to check if 89 is present in the list or not and returns a boolean result
print(m.count(7))


#join -combines list to a string
sentence='y '.join(['a','b','c'])
print(sentence)

#list unpacking
a,b,*others,c=[1,2,3,4,5,6,7,8,9]
print(a,b,others,c)