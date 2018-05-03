import pygame
from random import randint

class Gui:
    def __init__(self, program):
        pygame.init()
        self.program = program
        self.SIZE = self.WIDTH, self.HEIGHT = (1200,600)
        self.screen = pygame.display.set_mode(self.SIZE)
        self.font_name = pygame.font.match_font("arial")
        self.font = pygame.font.Font(self.font_name, 15)
        self.show_lines()

    def draw_text(self, text, x, y):
        text_surface = self.font.render(str(text), True, (255,0,0))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

    def draw_stop(self,element):
        name = element["name"]
        x,y = element["pos"]
        self.draw_text(name, x, y)
        pygame.draw.circle(self.screen, (0,255,0),(x,y), 5, 0)

    def stop_in_stops(self, stop):
        for in_stop in self.all_stops:
            if stop == in_stop["name"]:
                return True

    def set_poition_stops(self):
        self.all_stops = list()
        for id, bus_stops in self.program.ram.lines.items():
            for bus_stop in bus_stops:
                if not self.stop_in_stops(bus_stops):
                    x = randint(0,self.WIDTH)
                    y = randint(0,self.HEIGHT)
                    d = {"name": bus_stop, "pos": (x,y)}
                    self.all_stops.append(d)
        print(self.all_stops)
        pygame.display.flip()

    def show_lines(self):
        self.set_poition_stops()
        posx = 200
        for stop in self.all_stops:
            self.draw_stop(stop)

        pygame.display.flip()
