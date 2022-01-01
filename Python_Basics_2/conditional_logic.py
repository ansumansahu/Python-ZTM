#conditional logic
#mostly implemented based on boolean logic
#if else elif

age=int(input("Enter your age:"))
if age>18:
  print('good to drive')
elif age==18:
  print('take test buddy')
else:
  print('wait till age')

if age>=18 and age<24:
  print('hooray teenager')
else:
  print('child or adult')

#carefull of identations in python as interpreter rely's on those