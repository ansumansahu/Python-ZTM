#list/sets/dictionary comprehensions
my_list=[]
for char in 'Scorpio':
    my_list.append(char)
print(my_list)

#using list comprehension for the same output
#list=[param for param in iterable]
my_list=[char for char in 'Scorpio']
print(my_list)

my_list2=[num*2 for num in range(1,10)]
print(my_list2)

#we can extend it even more 
#suppose we want to print only even numbers after square of numbers from 1 to 10
my_list3=[num**2 for num in range(1,10) if num%2==0]
print(my_list3)

#sets
my_set={num for num in range(5)}
print(my_set)

#dictionary
sample_dict={
    'a':1,
    'b':2
}
my_dict={key:value**2 for key,value in sample_dict.items() if value%2==0}
print(my_dict)

#small exercise 
my_dict2={num:num*2 for num in [1,2,3]}
print(my_dict2)