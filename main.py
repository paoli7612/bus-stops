import pygame, setting, os
from archive import get_lines


class Boss:
    def __init__(self):
        self.city = "Trento"
        self.opt = setting
        self.screen = pygame.display.set_mode(self.opt.SIZE)
        self.dir = os.path.dirname(__file__)
        self.path_city = os.path.join(self.dir, "data", self.city + self.opt.XML_FORMAT)

        self.lines = get_lines(self.path_city)



b = Boss()
