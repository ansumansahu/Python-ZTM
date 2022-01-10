def my_decorator(func):
    def wrap_func(*args,**kwargs):
        print('--------')
        func(*args,**kwargs)
        print('--------')
    return wrap_func

@my_decorator
def hello(greet):
    print(greet)

hello('Yahallo')

#a=my_decorator(hello)
#a('Yahallo') 
#this returns the same output as the above code 

@my_decorator
def hi(greet,emoji):
    print(greet,emoji)

hi('Ohayo',':p')


        # Hence below is the default/basic decorator syntax
        # def my_decorator(func):
        #     def wrap_func(*args,**kwargs):
        #         func(*args,**kwargs)
        #     return wrap_func