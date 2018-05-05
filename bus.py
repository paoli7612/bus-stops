# bus.py

import pygame
from random import randint

class Bus(pygame.sprite.Sprite):
    def __init__(self, boss, id, line):
        self.boss = boss
        # pygame
        pygame.sprite.Sprite.__init__(self, boss.all_bus)
        self.image = pygame.Surface(boss.opt.BUS_SIZE)
        self.image.fill(boss.opt.BUS_COLOR)
        self.rect = self.image.get_rect()
        self.last_update = 0
        self.speed = 0
        # bus stop
        self.moving = False
        self.id = id
        self.line = line
        self.current_stop = 0



    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.speed:
            self.speed = randint(100,150)
            self.rect.center = self.boss.map[self.line[self.current_stop]]
            self.last_update = now
            self.current_stop = (self.current_stop + 1) % len(self.line)
