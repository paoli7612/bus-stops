# map.py

import pygame
from random import randint

class Map:
    def __init__(self, boss):
        self.boss = boss
        self.screen = pygame.Surface(boss.opt.SIZE)
        self.screen.fill(boss.opt.BGCOLOR)
        self.reset_points_dict()
        self.reset_screen()

    def __getitem__(self, key): return self.point_dict[key]

    def reset_points_dict(self):
        self.point_dict = dict()
        used = list()
        for id, line in self.boss.lines.items():
            for stop_name in line:
                x = randint(50, self.boss.opt.WIDTH-50)
                y = randint(50, self.boss.opt.HEIGHT-50)
                if not stop_name in used:
                    self.point_dict[stop_name] = (x,y)
                    used.append(stop_name)
        del used

    def reset_screen(self):
        for stop, pos in self.point_dict.items():
            pygame.draw.circle(self.screen, self.boss.opt.STOP_COLOR,pos, self.boss.opt.STOP_RADIUS,0)
