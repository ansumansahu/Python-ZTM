# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 19:38:59 2021

@author: Ansh
"""

#Exercise : list2 (lecture 45)
# using this list, 
basket = ["Banana", "Apples", "Oranges", "Blueberries"];

# 1. Remove the Banana from the list
basket.pop(0)
# 2. Remove "Blueberries" from the list.
basket.pop()
# 3. Put "Kiwi" at the end of the list.
basket.append("Kiwi")
# 4. Add "Apples" at the beginning of the list
basket.insert(0,'Apples')
# 5. Count how many apples in the basket
print(basket.count('Apples'))
# 6. empty the basket
basket.clear()
print(basket) 