def fib(number):
    a=0
    b=1
    for i in range(number):
        yield a
        sum=a+b
        a=b
        b=sum

for x in fib(10):
    print(x)