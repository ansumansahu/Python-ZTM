#zip
my_list=[1,2,3]
your_list=(10,20,30)
etxra_list={
    'a':4,
    'b':5,
    'c':6
}

print(list(zip(my_list,your_list,etxra_list)))
#takes multiple iterables and adds them together to a tuple
#iterables can be of any type

#reduce
from functools import reduce
def accumulator(acc,item):
    print(acc,item)
    return acc+item

print((reduce(accumulator,my_list,0)))
