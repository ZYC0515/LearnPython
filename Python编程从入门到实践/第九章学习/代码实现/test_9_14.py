from random import randint
class Die():
    def __init__(self,sides):
        self.sides = sides
    def roll_die(self,times,faces):
        for i in range(1,times):
            x = randint(1, faces)
            print(str(x))

die = Die(6)
die.roll_die(10,10)

