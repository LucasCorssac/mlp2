import pygame
import config
import player

# Arquivo para testar como fazer a wave de cobras
# A ideia é ir fazendo aqui e dps dar um jeito de colocar no projeto

class Enemie:
    def __init__(self, display):
        self._display = display
        self._endgame = False
        self._start_pos = (70, 20)
        self._pos = self._start_pos
        self._image = pygame.image.load("img/snake.png")
        # lista com os passos da cobra, percorrendo a lista conforme ela anda e somando conforme os elementos da lista
        # meio gambiarra mas era o jeito mais facil pra testar
        self._move_list_x = list([0]*80 + [1]*480 + [0]*240 + [-1]*120 + [0]*120 +
                                 [-1]*360 + [0]*120 + [1]*280 + [0]*120 + [-1]*280 + [0]*80 +
                                 [1]*360 + [0]*120 + [1]*80 + [0]*160 + [1]*80)
        self._move_list_y = list([1]*80 + [0]*480 + [1]*240 + [0]*120 + [-1]*120 +
                                 [0]*360 + [1]*120 + [0]*280 + [1]*120 + [0]*280 + [1]*80 +
                                 [0]*360 + [-1]*120 + [0]*80 + [1]*160 + [0]*80)
        self._speed = 20
        self._spawn = 0 - self._speed
        self._health_scale = 1
        self._health = config.Config.ENEMIE_START_HEALTH*self._health_scale
        self._active = False
        self._level = 1
        self._reward = 50
        self._attacking = 0

    def logic(self):
            if self._spawn >= 3019 and self.is_active():
                self._spawn = 0 - self._speed
                self._level += 1
                self._pos = self._start_pos
                self._active = False
                self._attacking += 1
            else:
                self._spawn = self._spawn + int(1*self._speed)
                self._move(self._spawn)

    def draw(self):
        self._print(self._display)
        self._draw_enemie_health()

    def _print(self, display):
        display.blit(self.get_image(), self.get_pos())

    def get_image(self):
        return self._image

    def get_pos(self):
        return self._pos

    def get_reward(self):
        return self._reward

    def get_attacking(self):
        return self._attacking

    def go_to_start_pos(self):
        self._pos = self._start_pos
        self._spawn = 0 - self._speed
        self._level += 1
        self.set_full_health()

    def _move(self, init):
        x, y = self.get_pos()
        if self._move_list_x[init] < 0:
            self._image = pygame.image.load("img/snake_inv.png")
        else:
            self._image = pygame.image.load("img/snake.png")
        self.set_pos(x + int(self._move_list_x[init]*self._speed), y + int(self._move_list_y[init]*self._speed))

    def set_pos(self, x, y):
        self._pos = (x, y)

    def is_active(self):
        return self._active

    def get_level(self):
        return self._level

    def set_active(self):
        self._active = True

    def set_full_health(self):
        self._health = config.Config.ENEMIE_START_HEALTH * self._health_scale

    def set_not_active(self):
        self._active = False

    def _draw_enemie_health(self):
        x, y = self.get_pos()
        if self._health > 90*self._health_scale:
            pygame.draw.rect(self._display, (0, 255, 0, 255), (x+10, y-10, 40, 5))
        elif self._health > 80*self._health_scale:
            pygame.draw.rect(self._display, (0, 200, 0, 255), (x+10, y-10, 36, 5))
        elif self._health > 70*self._health_scale:
            pygame.draw.rect(self._display, (0, 150, 0, 255), (x+10, y-10, 32, 5))
        elif self._health > 60*self._health_scale:
            pygame.draw.rect(self._display, (0, 100, 0, 255), (x+10, y-10, 28, 5))
        elif self._health > 50*self._health_scale:
            pygame.draw.rect(self._display, (230, 180, 31, 255), (x+10, y-10, 24, 5))
        elif self._health > 40*self._health_scale:
            pygame.draw.rect(self._display, (222, 120, 40, 255), (x+10, y-10, 20, 5))
        elif self._health > 30*self._health_scale:
            pygame.draw.rect(self._display, (255, 0, 0, 255), (x+10, y-10, 16, 5))
        elif self._health > 20*self._health_scale:
            pygame.draw.rect(self._display, (200, 0, 0, 255), (x+10, y-10, 12, 5))
        elif self._health > 10*self._health_scale:
            pygame.draw.rect(self._display, (150, 0, 0, 255), (x+10, y-10, 8, 5))
        elif self._health > 0*self._health_scale:
            pygame.draw.rect(self._display, (100, 0, 0, 255), (x+10, y-10, 4, 5))


