# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 19:46:44 2021

@author: Ansh
"""

#sets: unordered collection of unique objects
#as it is unordered, it doesn't support indexing
my_set={1,'a',2,'b',3,'a',4}
my_set.add(5)
print(my_set) #repeated objects are not printed
print(len(my_set))
print('c' in my_set)

list1=[1,2,3,4,5,5]
print(set(list1))

#set methods
s1={1,2,3,4,5}
s2={4,5,6,7,8,9}
s3={6,9}
#imagine venn diagram while performing operations on set
print(s2.difference(s1))
s1.discard(1)
print(s1)
print(s1.intersection(s2))
print(s1.isdisjoint(s2)) #checks if intersection is null
print(s2.issuperset(s3)) #s2 has all s3 items i.e superset
print(s3.issubset(s2))
print(s1.union(s2))