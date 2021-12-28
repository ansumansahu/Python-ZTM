# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 19:35:25 2021

@author: Ansh
"""

#boolean - most useful for conditioning (in functions)

#do it yourself within lecture 38
birthyear = input('what year were you born :')
print(type(birthyear)) #checking datatype for birthyear
current_year=2021
age=current_year-int(birthyear)
print(f'you are {age} years old')

#exercise for lecture 40: password checker
username=input('type your username :')
password=input('type your password :')
pass_length= len(password)
x='*'*pass_length
print(f'hey {username}, your {x} is {pass_length} letters long')