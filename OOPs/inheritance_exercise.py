class Pets():
    animals = []
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'

#1 Add another Cat
class Sigma(Cat):
    def sing(self,sounds):
        return f'{sounds}'

#2 Create a list of all of the pets (create 3 cat instances from the above)
Simon1=Simon('Simon',12)
Sally1=Sally('Sally',13)
Sigma1=Sigma('Sigma',14)
my_cats = [Simon1,Sally1,Sigma1]

#3 Instantiate the Pet class with all your cats use variable my_pets
my_pets=Pets(my_cats)

#4 Output all of the cats walking using the my_pets instance
my_pets.walk()

#it's same as writing the below
# for cats in my_cats:
#     print(cats.walk())