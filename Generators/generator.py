#range is a generatot

# list(range(10))
# range(10)

def make_list(num):
    result=[]
    for i in range(num):
        result.append(i*2)
    return result

my_list=make_list(10)
print(my_list)

#list creates a gaint list and stores in memory 
#range, a decorator on the other hand, never creates list and doesn't use memory
#it passes numbers 0 to 99 one by one iterating in the for loop

def generator_function(num):
    for i in range(10):
        yield i
for i in generator_function(10):
    print(i)