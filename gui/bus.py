import pygame

class Bus(pygame.sprite.Sprite):
    def __init__(self, id):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20,20))
        self.rect = image.get_rect()
        self.travelling = False

    def update(self):
        if self.travelling:
            self.travelling = self.travel.update()
        else:
            self.travel = Travel(self.start, self.end, self.speed)
            self.travelling = True
