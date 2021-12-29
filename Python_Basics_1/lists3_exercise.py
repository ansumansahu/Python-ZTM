# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 19:39:29 2021

@author: Ansh
"""

#Exercise :list3 (lecture 47)
#fix this code so that it prints a sorted list of all of our friends (alphabetical).
friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu']
new_friend = ['Stanley']
friends.extend(new_friend)
print(sorted(friends))

