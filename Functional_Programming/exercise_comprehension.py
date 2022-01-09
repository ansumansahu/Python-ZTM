some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)

#above code find and return duplicates in a given list
#use comprehensions for the same

duplicates2={char for char in some_list if some_list.count(char)>1}
print(list(duplicates2))