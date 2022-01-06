#OOP Part2
#attributes and methods
class PlayerCharacter:
    spells=True
    #class object attribute- not a dynamic attr
    #fixed for the class and doesn't change irrespective of the object
    def __init__(self, name, age):
        self.name= name
        self.age= age #attributes

player1=PlayerCharacter('Scorpio',23)
player2=PlayerCharacter('Scorpio2',24)
print(player1.spells)
print(player2.spells)