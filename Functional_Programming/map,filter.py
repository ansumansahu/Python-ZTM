#map
my_list=[1,2,3]
def mul_by2(item):
    return item*2

print(list(map(mul_by2,[10,20,30])))
#calls the function and implements it on the iterables
print(list(map(mul_by2,my_list)))
print(my_list)
#it doesn't change my_list, it's a pure function

#filter
def only_odd(item):
    return item%2==1
#this will evaluate into a boolean expression
#filter will keep/remove item based on boolean
print(list(filter(only_odd,my_list)))  
