import math

from stop_list import StopList
from setting import SPEED_BUS


class Pos:
    def __init__(self, xy):
        x,y = xy
        self.x = x
        self.y = y

    def get_pos(self):
        return(self.x, self.y)

    def __str__(self):
        return "%d & %d" %self.get_pos()

class Travel:
    def __init__(self, spos, epos):
        self.s = Pos(spos)
        self.e = Pos(epos)
        dx = abs(self.s.x - self.e.x)
        dy = abs(self.s.y - self.e.y)
        if dx == 0:
            self.spx = 0
            self.spy = SPEED_BUS
        else:
            m = dy/dx
            rad = math.atan(m)
            self.spx = math.cos(rad) * SPEED_BUS
            self.spy = math.sin(rad) * SPEED_BUS

    def update(self):
        s,e = self.s, self.e

        if s.x < e.x: s.x += self.spx
        else: s.x -= self.spx
        if s.y < e.y: s.y += self.spy
        else: s.y -= self.spy

        if abs(s.x-e.x) < SPEED_BUS: s.x = e.x
        if abs(s.y-e.y) < SPEED_BUS: s.y = e.y
        if s.x == e.x and s.y == e.y:
            return False
        else: return True
