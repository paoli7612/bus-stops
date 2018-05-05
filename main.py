import pygame, setting, os
from archive import get_lines
from bus import Bus
from map import Map

class Boss:
    def __init__(self):
        self.city = "Trento"
        self.opt = setting
        # pygame
        self.screen = pygame.display.set_mode(self.opt.SIZE)
        self.clock = pygame.time.Clock()
        # path
        self.dir = os.path.dirname(__file__)
        self.path_city = os.path.join(self.dir, "data", self.city + self.opt.XML_FORMAT)
        # bus stop
        self.lines = get_lines(self.path_city)

        # my classes
        self.map = Map(self)
        self.all_bus = pygame.sprite.Group()

        for id, line in self.lines.items():
            bus = Bus(self, id, line)
        self.loop()


    def loop(self):
        self.running = True
        while self.running:
            self.clock.tick(50)
            # event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            # update
            self.all_bus.update()
            # draw
            self.screen.blit(self.map.screen,(0,0))
            self.all_bus.draw(self.screen)
            pygame.display.flip()


b = Boss()
