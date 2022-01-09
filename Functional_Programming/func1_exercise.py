from functools import reduce

def cap(items):
    return items.capitalize()
#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']
print(list(map(cap,my_pets)))

#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]
print(list(zip(my_strings,sorted(my_numbers))))

#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

def over50(i):
    return i>50
print(list(filter(over50,scores)))

#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
my_list=my_numbers+scores
def combine(temp,items):
    return temp+items
print(reduce(combine,my_list))