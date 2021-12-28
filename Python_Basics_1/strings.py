# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 19:31:08 2021

@author: Ansh
"""

#strings (datatype)

#1.longstring 
longstring='''
woah 
hey there
how you doin? ;P
'''

#2. string concatenation
print(longstring + '\nyup doing great')

#3. type conversion
print(str(101))
print(type(str(101))) #checking

#weather= 'It's sunny ?? how to solve
#4. use escape sequence
weather='It\'s \'kind of\' sunny'
print(weather)

#5. formatted strings (new python3 feature)
name='Ansuman'
age=23
print('hi '+name+', you are '+str(age)+' years old')
#instead of all these complications, use formatted strings for simplicity
print(f'hi {name}, you are {age} years old')

#can also use dot format which was used before format
print('hi {}, you are {} years old'.format(name,age))
print('hi {new_name}, you are {age} years old'.format(new_name='Ansh',age=22))

#6. string indexes
a='anshsahu'
  #01234567 - indexes of the string
print(a[0])
print(a[0:4]) #[start:stop] this is called slicing
print(a[0]+a[2])
print(a[0:8:2]) #[start:stop:stepover] 
print(a[::-1])

#7. built-in string functions and methods
print(len('hey')) #function
print('oy oy'.upper()) #method
print('what\'s up'.replace('up','popping'))