#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 1 Instantiate the Cat object with 3 cats
cat1=Cat('c1',12)
cat2=Cat('c2',13)
cat3=Cat('c3',14)
# 2 Create a function that finds the oldest cat

def oldest(*age):
    return max(age)

# 3 Print out: "The oldest cat is x years old."
# x will be the oldest cat age by using the function in #2
oldest_cat=oldest(cat1.age,cat2.age,cat3.age)
print(f'The oldest cat age is {oldest_cat} years old')