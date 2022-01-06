#abstraction - hiding of unneccessary informations and only
#providing access to required information for the user/machine. Everything
#else is kept hidden underneath

class PubgAcount:
    def __init__(self, acc_name, rank):
        self.acc_name= acc_name
        self.rank= rank

    def royalpass(self):
        pass

    def chat_intro(self):
        print(f'Yahallo, My name is {self.acc_name} and I\'m a {self.rank} player')

player=PubgAcount('DSxScorpio', 'AceIII')
player.chat_intro()

player.acc_name='Omen'
player.chat_intro= 'Hmmm'
print(player.acc_name)
print(player.chat_intro)