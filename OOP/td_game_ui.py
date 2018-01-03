import pygame
from config import Colors


class UI:
    def __init__(self, rect, text):
        self.rect = rect
        self.text = text

class Button(UI):

    def text_objects(self, font):
        text_surface = font.render(self.text, True, (0,0,0,0))
        return text_surface, text_surface.get_rect()

    def draw(self, display):
        pygame.draw.rect(display, Colors.BRIGHT_GREEN, self.rect)
        text_font = pygame.font.SysFont("comicsansms", 20)
        text_surf, text_rect = self.text_objects(text_font)
        
        x = self.rect.left
        y = self.rect.top

        w = self.rect.width
        h = self.rect.height

        text_rect.center = ((x + (w / 2)), (y + (h / 2)))
        display.blit(text_surf, text_rect)
        #pygame.draw.rect(display, Colors.GREEN, self.rect)

