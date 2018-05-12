import pygame

from setting import HEIGHT, WIDTH, WIDTH_LEGGEND, SIZE_LEGEND

class Legend:
    def __init__(self):
        self.font_name = pygame.font.match_font("arial")
        self.font = pygame.font.Font(self.font_name, 20)
        self.screen = pygame.Surface(SIZE_LEGEND)
        self.all_line = list()
        self.line_colors = list()

        self.reset()

    def reset(self):
        self.screen.fill((50,50,50))
        self.write("Line", 10, 10, (255,255,255))

    def draw_line(self, id, color):
        self.write("- %s"%id, 10, 10 + 50 + self.all_line.index(id)*50, color)

    def add_line(self, id, color):
        self.all_line.append(id)
        self.line_colors.append(color)
        self.draw_line(id, color)

    def del_line(self, id):
        self.reset()
        p = self.all_line.index(id)
        del self.all_line[p]
        del self.line_colors[p]
        for n,line in enumerate(self.all_line):
            self.draw_line(line, self.line_colors[n])


    def write(self, text, x, y, color):
        text_surface = self.font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (x,y)
        self.screen.blit(text_surface, text_rect)

    def draw(self, surface):
        surface.blit(self.screen, (0,0))
