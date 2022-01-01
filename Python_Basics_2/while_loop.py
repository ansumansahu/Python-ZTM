#while loops
i=0
while i<5:
  i+=1
  print(i)
  break

#when to use for and while: depends on complexity and programmer knowing the iterable count
#while has condition so it is more powerful but for is simple
#use while when not sure of the length for iteration : example given below

while True:
  print('this breaks when you say bye')
  response=input('say something :')
  if(response=='bye'): 
    break
