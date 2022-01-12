import random
# help(random) #displays what the package does
# print(dir(random)) #gives all the methods available in package 

print(random.random())
print(random.randint(1,100))
print(random.choice([5,6,7,8,9]))

li=[1,2,3,4,5]
random.shuffle(li)
print(li)

#giving an alias
import random as ansh
print(ansh.randint(1,100))

import sys
print(sys)
#really useful package (sys.argv)