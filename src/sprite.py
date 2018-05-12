import pygame

from travel import Travel
from setting import SIZE_BUS, TILE_BUS

class Bus(pygame.sprite.Sprite):
    def __init__(self, bus):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(SIZE_BUS)
        self.image.fill((255,200,50))
        self.rect = self.image.get_rect()
        self.bus = bus
        self.moving = False
        self.last_update = 0
        self.speed = 10

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.speed:
            self.move()
            self.last_update = now

    def move(self):
        if self.moving:
            self.moving = self.travel.update()
        else:
            spos = self.bus.current_stop().pos
            epos = self.bus.next_stop().pos
            self.travel = Travel(spos, epos)
            self.moving = True

        self.rect.center = self.travel.s.get_pos()
