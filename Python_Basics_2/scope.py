
#scope- what variables do i have access to 
#variables created outside a function can be globally accessed i.e can be used anywhere.
#variables created inside function is restricted to that function itself
total=100
def func():
  tot=100

print(total)
# print(tot) -this will give not defined error

#lecture-91 let's guess scope exercise
a=1
def confusion():
  a=5
  return a
print(a) #1
print(confusion()) #5

a=1
def confusion():
  return a
print(a) #1
print(confusion()) #1

a=1
def more_confusion():
  a=10
  def confusion():
    return a
  return confusion()
print(a) #1
print(more_confusion()) #10

a=1
def more_confusion():
  a=10
  def confusion():
    return sum
  return confusion()
print(a) #1
print(more_confusion()) #function sum

#Rules:
#1. check for local variable
#2. check if there is a parent local (in 3rd case a is not defined in local (confusion) but parent variable a is present (a in more_confusion))
#3. go global (like that of 2nd case)
#4. built in python functions (checks if it is some sort of predefined function or variable) (4th case)

#nonlocal: new keyword which says that the variable used is not local obiously but no global either but present in parent function
def outer():
  x="local"
  def inner():
    nonlocal x
    x="nonlocal" #grabs parent x and changes it 
    print("inner:", x)
  
  inner()
  print("outer:", x)

outer()