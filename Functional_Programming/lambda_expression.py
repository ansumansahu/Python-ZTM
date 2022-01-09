#lambda expression
#it is really useful when we have a function which is only used once
#and they are anonymous function

from functools import reduce
mylist=[1,2,3]
def mulby2(items):
    return items*2

print(list(map(mulby2,mylist)))

print(list(map(lambda item: item*2,mylist)))
#lambda expression is a one time expression which the intrepreter
#performs according to the action asked for and then it forgets it
print(mylist)

print(list(filter(lambda item: item%2==1,mylist)))
print(reduce(lambda acc,item:acc+item,mylist))