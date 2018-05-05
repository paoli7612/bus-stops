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
        if now - self.last_update > 10:
            self.last_update = now
            print(self.moving)
            if self.moving:
                self.moving = self.travel.update()
            else:
                current_stop = self.boss.map[self.line[self.current_stop]]
                self.current_stop = (self.current_stop + 1) % len(self.line)
                next_stop = self.boss.map[self.line[self.current_stop]]
                self.travel = Travel(current_stop, next_stop, 1)
                self.moving = True

            self.rect.center = self.travel.pos

class Travel:
    def __init__(self, start, end, speed):
        self.sx, self.sy = start
        self.ex, self.ey = end
        self.pos = start
        self.speed = speed

    def update(self):
        if self.sx < self.ex:
            self.sx += self.speed
        elif self.sx > self.ex:
            self.sx -= self.speed
        if self.sy < self.ey:
            self.sy += self.speed
        elif self.sy > self.ey:
            self.sy -= self.speed

        self.pos = (self.sx, self.sy)

        if self.sx == self.ex and self.sy == self.ey:
            return False
        else: return True
