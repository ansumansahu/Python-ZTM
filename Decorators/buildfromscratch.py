#building own decorator - to test how fast our code runs
from time import time

def performance(func):
    def wrap_func(*args,**kwargs):
        t1=time()
        result=func(*args,**kwargs)
        t2=time()
        print(f'took {t2-t1}s')
        return result
    return wrap_func

@performance
def time_taken():
    for i in range(1000000):
        i*5

time_taken()
