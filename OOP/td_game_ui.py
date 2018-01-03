import pygame
import player
from config import Colors


class UI:
    def __init__(self, rect, text):
        self._rect = rect
        self._text = text

    def get_rect(self):
        return self._rect

    def set_rect(self, rect):
        self._rect = rect

    def get_text(self):
        return self._text

    def set_text(self, text):
        self._text = text

class Button(UI):

    def text_objects(self, font):
        text_surface = font.render(self._text, True, (0,0,0,0))
        return text_surface, text_surface.get_rect()

    def draw(self, display):
        pygame.draw.rect(display, Colors.BRIGHT_GREEN, self._rect)
        text_font = pygame.font.SysFont("comicsansms", 20)
        text_surf, text_rect = self.text_objects(text_font)
        
        x = self._rect.left
        y = self._rect.top

        w = self._rect.width
        h = self._rect.height

        text_rect.center = ((x + (w / 2)), (y + (h / 2)))
        display.blit(text_surf, text_rect)
        #pygame.draw.rect(display, Colors.GREEN, self.rect)

class Stats(UI):

    def text_objects(self, font):
        text_surface = font.render(self._text, True, (0,0,0,0))
        return text_surface, text_surface.get_rect()

    def draw(self, display):
        #pygame.draw.rect(display, Colors.INVISIBLE, self.rect)
        text_font = pygame.font.SysFont("comicsansms", 15)
        text_surf, text_rect = self.text_objects(text_font)

        x = self._rect.left
        y = self._rect.top

        w = self._rect.width
        h = self._rect.height

        text_rect.center = ((x + (w / 2)), (y + (h / 2)))
        display.blit(text_surf, text_rect)
        # pygame.draw.rect(display, Colors.GREEN, self.rect)

