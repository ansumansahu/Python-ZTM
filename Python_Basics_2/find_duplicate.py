#Exercise: find duplicate
#check duplicates in a list and print only those items
some_list=['a','b','c','b','d','m','n','n']
duplicate_list=[]
while some_list!=[] :
  check=str(some_list.pop(0))
  for i in some_list:
    if check==i:
      duplicate_list.append(check)
      break
print(duplicate_list)

#simpler solution
some_list=['a','b','c','b','d','m','n','n']
duplicates=[]
for char in some_list:
  if some_list.count(char)>1:
    if char not in duplicates:
      duplicates.append(char)
print(duplicates)