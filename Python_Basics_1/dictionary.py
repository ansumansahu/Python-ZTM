# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 19:45:10 2021

@author: Ansh
"""

#datatype-Dictionary (dict)(other language - hashtable/map)
#dict is also a datastructure which has a key and a value assigned to the key

dictionary={
  'a':[1,2,3],
  2:'hola',
  'c':True,
  'a':124
}
print(dictionary['a'])
my_list=[{'a':[1,2,3],'b':'hola','c':True},{'d':4},'this_is_index2']
print(my_list[2])
print(my_list[0]['a'][1])

#dictionary_methods

user={
  'name':'ansh',
  'age':23,
  'role':'student'
}
print(user.get('gender')) #method to check if key is present in the dictionary .if yes it gives the value
#we can assign value there itself
print(user.get('gender','male'))
#another way 
print('age' in user.keys()) #checks keys
print(23 in user.values()) #checks values
print(user.items()) #grabs all items it's a tuple
user1=user.copy()
print(user1)
print(user.clear())
print(user1)
print(user1.pop('age'))
print(user1)
print(user1.update({'name':'ansu'}))
print(user1)

#alternate syntax for dictionary (not common)
user2=dict(name='ansh',age=23)
print(user2)