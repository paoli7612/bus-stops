import pygame
from threading import Thread

from bus import Bus
from map import Map
from data import get_table

class Simulation:
    def __init__(self):
        self.table = get_table("Trento")
        self.map = Map(self.table)
        self.new_bus("1")
        self.new_bus("4/")
        self.show_line("1")
        #self.show_line("1/")
        #self.show_line("4")
        self.show_line("4/")
        self.map.window.loop()

    def new_bus(self, id):
        line = self.table[id]
        b = Bus(id, line)
        self.map.window.add_bus(b)

    def show_line(self, id):
        if id in self.map.window.legend.all_line:
            self.map.del_line(id)
        else: self.map.show_line(id)

    def stop(self):
        self.map.window.running = False

    def __str__(self):
        return str(self.table)

s = Simulation()
