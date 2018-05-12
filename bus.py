# bus.py

import pygame
from random import randint

class Bus(pygame.sprite.Sprite):
    def __init__(self, boss, id, line):
        self.boss = boss
        # pygame
        pygame.sprite.Sprite.__init__(self, boss.all_bus)
        self.font_name = pygame.font.match_font("arial")
        self.font = pygame.font.Font(self.font_name, 20)
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
        try: print(self.last_update)
        except: return
        if now - self.last_update > 20:
            self.last_update = now
            print(self.moving)
            if self.moving:
                self.moving = self.travel.update()
            else:
                current_stop = self.boss.map[self.line[self.current_stop]]
                self.current_stop = (self.current_stop + 1) % len(self.line)
                next_stop = self.boss.map[self.line[self.current_stop]]
                self.travel = Travel(current_stop, next_stop, 5)
                screen = self.boss.map.screen
                func = pygame.draw.line
                func(screen, (200,100,50), current_stop, next_stop)
                
                self.moving = True

            self.rect.center = self.travel.pos

    def draw(self, surface):
        surface.blit(self.image,self.rect)
        text_surface = self.font.render(self.id, True, (0,0,255))
        text_rect = text_surface.get_rect()
        text_rect.midtop = self.rect.center
        surface.blit(text_surface, text_rect)

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

        if abs(self.sx-self.ex) <= self.speed:
            self.sx = self.ex
        if abs(self.sy-self.ey) <= self.speed:
            self.sy = self.ey
        if self.sx == self.ex and self.sy == self.ey:
            return False
        else: return True
