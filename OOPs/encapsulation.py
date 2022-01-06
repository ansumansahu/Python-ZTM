#encapsulation - binding of data and functions that manipulates that
#data and we encapsulate into one big object which users,machines can
#interact. The data and functions are nothing but attributes and
#methods used for objects in the class

class PubgAcount:
    def __init__(self, acc_name, rank):
        self.acc_name= acc_name
        self.rank= rank

    def chat_intro(self):
        print(f'Yahallo, My name is {self.acc_name} and I\'m a {self.rank} player')

player=PubgAcount('DSxScorpio', 'AceIII')
player.chat_intro()