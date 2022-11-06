class Die:
    """Class Die with one attribute called sides"""
    def __init__(self, sides = 6):
        self.sides = sides

    def roll_die(self):
        self.sides = 6
        from random import randint
        num = 10
        for x in range(num):
            print (randint(1,6))

    def roll_die_10(self):
        self.sides = 10
        from random import randint
        num = 10
        for x in range(num):
            print (randint(1,10))
    
    def roll_die_20(self):
        self.sides = 20
        from random import randint
        num = 10
        for x in range(num):
            print (randint(1,20))

die_1 = Die()
die_1.roll_die()

die_2 = Die(10)
die_2.roll_die_10()

die_3 = Die(20) 
die_3.roll_die_20()



