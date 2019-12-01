from random import randint
from copy import copy

from window import Window

class Map:
    def __init__(self, table):
        self.table = table
        self.window = Window(table.stop_list)
        self.lines = list()

    def del_line(self, id):
        self.window.set_screen()
        for p,(line,c) in enumerate(self.lines):
            if line.id == id:
                del self.lines[p]
        for line,c in self.lines:
            self.draw_line(line,c)
        self.window.legend.del_line(id)

    def draw_line(self, line, c):
        l = len(line)
        for p in range(l):
            p1 = line[p].pos
            p2 = line[(p+1)%l].pos
            self.window.draw_line(p1,p2,c)

    def show_line(self, id):
        line = self.table[id]
        c = self.random_color()
        self.lines.append((copy(line),c))
        self.draw_line(line,c)
        self.window.legend.add_line(id,c)


    def random_color(self):
        r = randint(0,250)
        g = randint(0,250)
        b = randint(0,250)
        return (r,g,b)
