#Exercise: function
#write a function to get highest even number from a list
def highest_even(li):
  result=0
  for item in li:
    if item%2==0 and item>result :
      result=item
  return result
print(highest_even([10,2,3,4,8,11]))

#my solution is simple enough so not gonna write the given solution for the exercise
