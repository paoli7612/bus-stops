import pygame, setting, os
from threading import Thread
from time import sleep
from archive import get_lines
from bus import Bus
from map import Map

class Boss:
    def __init__(self):
        self.city = "Trento"
        self.opt = setting
        # pygame
        pygame.init()
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

        self.th_loop = Thread(target=self.loop)
        self.th_station = Thread(target=self.station)
        self.th_station.start()
        sleep(1)
        self.th_loop.start()

    def station(self):
        for i in range(60):
            for id, line in self.lines.items():
                bus = Bus(self, id, line)
                sleep(0.8)

    def loop(self):
        self.running = True
        while self.running:
            try:
                self.clock.tick(120)
                # event
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                # update
                self.all_bus.update()
                # draw
                self.screen.blit(self.map.screen,(0,0))
                for bus in self.all_bus:
                    bus.draw(self.screen)
                pygame.display.flip()
            except: pass


b = Boss()
