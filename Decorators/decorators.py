#functions in python act just like variables do
#we can also pass functions inside of arguments    
def hello(func):
    func()

def greet():
    print('still here!')

a=hello(greet)
#function greet is used as a argument here
print(a)

#higher order function HOC:
def greet():
    def func():
        return 5
    return func()
#func which accepts another func inside it's parameters/func which returns another func

#Decorator:
def decorator(func):
    def wrap_func():
        print('--------')
        func()
        print('--------')
    return wrap_func

@decorator
def hello():
    print('hello')

@decorator
def bye():
    print('bu-bye')

hello()
bye()