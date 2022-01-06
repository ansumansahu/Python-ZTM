#OOP
print(type(None))
a=set()
print(type(a))
print(type(()))

#OOP exercise
print(type(None)) #class none
print(type(True)) #class bool
print(type(5)) #class int
print(type(5.5)) #class float
print(type('hi')) #class str
print(type([])) #class list
print(type(())) #class tuple
print(type({})) #class dict

#creating a new class
class BigObject:
    pass

print(type(BigObject))
#we get class type cause we have only created  
#a class and not it's objects
obj1= BigObject()
# instantiating - calling a class to create an object 
print(type(obj1))

#creating own objects
class PlayerCharacter:
    def __init__(self, name, age):
        self.name= name
        self.age= age #attributes
#attributes are properties which the objects have
    def run(self):
        return ('run')


player1=PlayerCharacter('Scorpio',23)
print(player1.name)
print(player1.age)
print(player1.run())
