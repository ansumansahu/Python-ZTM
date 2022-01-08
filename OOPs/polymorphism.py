#polymorphism - many forms
#it refers to the way in which object classes can share same method name
#but those method names can act differently based on which object calls them

class Troop:
    def game_troops(self):
        print('Available')

class Wizard(Troop):
    def __init__(self,type,hitpoints):
        self.type= type
        self.hitpoints= hitpoints

    def info(self):
        print(f'{self.type}Wizard || Ground Attack || {self.hitpoints} Hitpoints')

class Dragon(Troop):
    def __init__(self,type,hitpoints):
        self.type= type
        self.hitpoints= hitpoints

    def info(self):
        print(f'{self.type}Dragon || Air Attack || {self.hitpoints} Hitpoints')

wiz1=Wizard('Fire',650)
drag1=Dragon('Ice',4300)

for troop in [wiz1,drag1]:
    troop.info()

#both wizard and dragon class has info attribute (same name) but gives
#different output when called due to polymorphism 