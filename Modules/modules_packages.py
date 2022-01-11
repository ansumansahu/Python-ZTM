#whenever we use import cache file is generated and saved as pycache folder
#(cache makes program run faster as it stores the compiled version of program)

from utility import divide,multiply
#from utility import * #imports all funtions
print(divide(10,5))
print(multiply(2,9))

#importing module
import utility 
print(utility.divide(20,5))

#importing module from package
import testing.shopping_cart
print(testing.shopping_cart.buy('Apple'))

#importing particular function from package
from testing.shopping_cart import buy
print(buy('Mobile'))
