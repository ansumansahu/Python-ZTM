class Troop:
    def __init__(self, name):
        self.name= name

    def game_troops(self):
        print('Available')

class Wizard(Troop):
    def __init__(self,type,hitpoints,name):
        super().__init__(name)
        #super here refers to upper class (in our case Troop)
        #when we instantiate wiz1 inside Wizard we call name from troop
        self.type= type
        self.hitpoints= hitpoints

    def info(self):
        print(f'{self.type}Wizard || Ground Attack || {self.hitpoints} Hitpoints')

wiz1=Wizard('Electro',1200,'Scorpio')
print(wiz1.name)
#if we try to print the above without super keyword we get error as 
#wizard doesn't have any attribute called name.(troop does though) 


