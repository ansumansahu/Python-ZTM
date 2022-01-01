#functions : not predefined ones, we can create

def greet(name):
  for i in name:
    print('hey '+ i)

greet(['adam','eve'])
#parameter and arguments
#arguments are actual values which we provide

def say_hello(name='ansh',age='23'): #default parameter
  print('hey '+name+ f' of {age} age')

#positional arguments
say_hello('kiddo',18)
#keyword arguments
say_hello(age='unknown', name='blank')

say_hello()
say_hello(age='X')

#return
def sum(a,b):
  return a+b  
print(sum(4,5))

#nested use of return
def sum(num1,num2):
  def another_sum(n1,n2):
    return n1+n2
  return num1+num2

total=sum(10,20)
print(total)

#docstrings 
#allows you to comment inside a function which is reflected in the editor when we use it later 

def test(a):
  '''
  Info: prints the parameter
  '''
  print(a)
#type test() and editor will show the info for it
test('!!!!')