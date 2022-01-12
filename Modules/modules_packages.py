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

print(__name__)
#this part will execute only because this is main file
if __name__=='__main__': #something which we will see often
    import utility 
    print(utility.divide(20,5))
    from testing.shopping_cart import buy
    print(buy('Laptop'))

#notice how it shows class is created in utility
from utility import Test
t1=Test()
print(type(t1))

#because utility is not main file Game function won't execute
#and hence this part will error out
from utility import Game
print(Game(5))