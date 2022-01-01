#for loops
for i in {1,2}:
  for j in ('a','b'):
    print(i ,j)

#iterable: object/collection which can be looped over (list/set/tuple/string/dict) , int is not iterable as it's not a collection


#dict
user={
  'name':'ansh',
  'age':23,
  'gender':'male'
}
for i in user:
  print(user[i])
#another way 
for i in user.values(): #can also do same for .keys() and .items()
  print(i)
#for all items it gives a tuple and we can unpack it
for key,value in user.items():
  print(key,value)


#range()
for i in range(10):
  print(i)
for i in range(0,10,2): #stepover nothing new
  print(i)
print(list(range(1,11))) #good trick to know


#enumerate()
#useful if we want to get an index counter
for i,char in enumerate("ansh"):
  print(i,char)

#small exercise use enumerate to create a list of range 100 and print index of 50 in the list
for index,item in enumerate(list(range(100))):
  if item==50:
    print(f'The index of 50 is {index}')

