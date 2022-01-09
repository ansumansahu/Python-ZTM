class Troop: #parent class
    def game_troops(self):
        print('Available')

class Wizard(Troop): #child class
    def __init__(self,type,hitpoints):
        self.type= type
        self.hitpoints= hitpoints

class Dragon(Troop): #child class
    def __init__(self,type,hitpoints):
        self.type= type
        self.hitpoints= hitpoints

    def attack_type(self):
        print('Air Attack')

class Hybrid(Wizard,Dragon): #multiple inheritance hybrid class
    def __init__(self, type, hitpoints):
        Wizard.__init__(self,type,hitpoints)
        Dragon.__init__(self,type,hitpoints)

hybrid1=Hybrid('Mixy',20)
hybrid1.attack_type()