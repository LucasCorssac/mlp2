import pygame

class Tower:
    def __init__(self, display):
        self._display = display
        self._start_pos = (70, 700)
        self._pos = self._start_pos
        self._image = pygame.image.load("img/tower.png")
        self._print(self, display)

    def _print(self, display):
        display.blit(self.get_image(), self.get_pos())

    def get_image(self):
        return self._image

    def get_pos(self):
        return self._pos

    def set_pos(self, x, y):
        self._pos = (x, y)
