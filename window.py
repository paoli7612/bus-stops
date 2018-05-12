import pygame

from setting import SIZE,RAD_STOP
from legend import Legend
import sprite

class Window:
    def __init__(self, stop_list):
        pygame.init()
        self.stop_list = stop_list
        self.screen = pygame.display.set_mode(SIZE)
        pygame.display.set_caption("bus-stop")
        self.set_screen()
        self.clock = pygame.time.Clock()
        self.all_bus = pygame.sprite.Group()
        self.legend = Legend()
        self.running = True

    def draw_stop(self, stop):
        pos = stop.pos
        pygame.draw.circle(self.bground, (200,0,20), pos, RAD_STOP)

    def draw_line(self, p1, p2, color):
        pygame.draw.line(self.bground, color, p1, p2)

    def add_bus(self, bus):
        b = sprite.Bus(bus)
        self.all_bus.add(b)

    def set_screen(self):
        self.screen.fill((0,0,0))
        self.bground = self.screen.copy()
        for stop in self.stop_list:
            self.draw_stop(stop)
        pygame.display.flip()

    def loop(self):
        while self.running:
            self.clock.tick(60)
            self.screen.blit(self.bground,(0,0))
            self.legend.draw(self.screen)
            self.all_bus.update()
            self.all_bus.draw(self.screen)
            pygame.display.flip()
