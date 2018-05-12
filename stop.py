from random import randint
from setting import WIDTH, HEIGHT, WIDTH_LEGGEND


class Stop:
    def __init__(self, name):
        self.name = name
        x = randint(WIDTH_LEGGEND+10,WIDTH-10)
        y = randint(10,HEIGHT-10)
        self.pos = (x,y)

    def __str__(self):
        return str(self.name) + " (%d - %d)" %self.pos
