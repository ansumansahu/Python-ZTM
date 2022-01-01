#arguments *args and keywaord arguments **kwargs
def func(*args, **kwargs):
  print(args) #args:tuple
  print(kwargs) #keyword args:dictionary
  total=0
  for items in kwargs.values():
    total+=items
  return sum(args)

print(func(1,2,3,4,5,num1=5,num2=10)) #multiple parameters

#Order for parameters: params, *args, default params, **kwargs 


#walrus operator :=
#this part is simply present to remind us to check what's new in python .check documentation to stay up-to-date. this time around walrus operator is newly added

a='ansumansahu'
while (l:=len(a)) >7:
  print(f'too long {l} letters')
  a=a[:-1]

print(a)
