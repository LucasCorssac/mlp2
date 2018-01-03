import pygame
import math


class Tower:
    def __init__(self, display):
        self._display = display
        self._start_pos = (0, 0)
        self._pos = self._start_pos
        self._image = pygame.image.load("img/Tower.png")
        self._level = 1
        self._id = 0
        self._range = 50
        self._attack_list = []
        self._damage = 10

    def logic(self):
            if self._spawn >= 3019 and self.is_active():
                self._spawn = 0 - self._speed
                self._level += 1
                self._pos = self._start_pos
                self._active = False
            else:
                self._spawn = self._spawn + int(1 * self._speed)
                self._move(self._spawn)

    def update(self):
        self._print(self._display)
        self._draw_enemie_health()

    def _move(self, init):
        x, y = self.get_pos()
        if self._move_list_x[init] < 0:
            self._image = pygame.image.load("img/snake_inv.png")
        else:
            self._image = pygame.image.load("img/snake.png")
        self.set_pos(x + int(self._move_list_x[init] * self._speed),
                     y + int(self._move_list_y[init] * self._speed))

    def _distance_to(self, enemy):
        p1x, p1y = self._pos
        p2x, p2y = enemy._pos
        x = p1x - p2x
        y = p1y - p2y
        result = math.sqrt(math.pow(x,2) + math.pow(y,2))
        return result



    def draw(self):
        self._display.blit(self._image, self.get_pos())
        for attack in self._attack_list:
            pygame.draw.line(self._display, (255, 125, 0), self._pos, attack, 4)

    def get_pos(self):
        return self._pos

    def set_pos(self, x, y):
        self._pos = (x, y)
