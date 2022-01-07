#inheritance - allows new objects to take on the properties of 
#existing objects or classes

#clash of clans troops
#they can be wizrds,archers,giants anything but they need to be 
#available troops for the game

#we can do it by inheritance
class Troop: #parent class
    def game_troops(self):
        print('Available')

class Wizard(Troop): #child/sub class
#wizard class inherited the sign_in functionality from the User class
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

wizard1=Wizard('Ice',700)
dragon1=Dragon('Electro',4000)
wizard1.game_troops()
wizard1.info()
dragon1.game_troops()
dragon1.info()

#check if an object is instance of a class
print(isinstance(dragon1,Dragon))
print(isinstance(dragon1,Troop))