import pygame
import config
import player

# Arquivo para testar como fazer a wave de cobras
# A ideia é ir fazendo aqui e dps dar um jeito de colocar no projeto



class Enemie:

    #STATUS
    NORMAL = 0
    POISONED = 1
    BURNING = 2

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
        self._level = 1

        self._health_scale = self._level - 1
        self._health = config.Config.ENEMIE_START_HEALTH + 50*self._health_scale


        self._active = False

        self._status = self.NORMAL
        self._status2 = self.NORMAL
        
        self._speed = 20
        self._spawn = 0 - self._speed
        self._reward = 50
        self._attacking = 0
        self._fire_damage = 1
        self._poison_damage = 0.5
        self._fire_init = None
        self._poison_init = None

    def logic(self):
            if self._spawn >= 3019 and self.is_active():
                self._spawn = 0 - self._speed
                #self._level += 1
                self._pos = self._start_pos
                self._active = False
                self._attacking += 1
            else:
                self._spawn = self._spawn + int(1*self._speed)
                self.is_on_fire()
                self.is_poisoned()
                if self._fire_init != None and self._status2 == self.NORMAL and self._spawn - self._fire_init >= 30*self._speed:
                    self._status = self.NORMAL
                if self._poison_init != None and (self._spawn - self._poison_init >= 50*self._speed):
                    self._status2 = self.NORMAL
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
        self._status = self.NORMAL
        self._status2 = self.NORMAL
        self._image = pygame.image.load("img/snake.png")
        self.upgrade_enemie()
        self.set_full_health()


    def _move(self, init):
        x, y = self.get_pos()
        if self._move_list_x[init] < 0:
            if self._status == self.NORMAL:
                self._image = pygame.image.load("img/snake_inv.png")
            if self._status == self.BURNING:
                self._image = pygame.image.load("img/burning_snake_inv.png")
            if self._status == self.NORMAL and self._status2 == self.POISONED:
                self._image = pygame.image.load("img/poisoned_snake_inv.png")
        else:
            if self._status == self.NORMAL:
                self._image = pygame.image.load("img/snake.png")
            if self._status == self.BURNING:
                self._image = pygame.image.load("img/burning_snake.png")
            if self._status == self.NORMAL and self._status2 == self.POISONED:
                self._image = pygame.image.load("img/poisoned_snake.png")
        self.set_pos(x + int(self._move_list_x[init]*self._speed), y + int(self._move_list_y[init]*self._speed))

    def set_pos(self, x, y):
        self._pos = (x, y)

    def is_active(self):
        return self._active

    def get_level(self):
        return self._level

    def get_speed(self):
        return self._speed

    def set_active(self):
        self._active = True

    def set_full_health(self):
        self._health = config.Config.ENEMIE_START_HEALTH + 50*self._health_scale

    def set_not_active(self):
        self._active = False

    def upgrade_enemie(self):
        self._level += 1
        self._speed += 1
        self._health_scale += 1

    def is_on_fire(self):
        if self._status == self.BURNING:
            self._health -= self._fire_damage
            self._image = pygame.image.load("img/burning_snake.png")

    def is_poisoned(self):
        if self._status2 == self.POISONED:
            self._image = pygame.image.load("img/poisoned_snake.png")

    def _draw_enemie_health(self):
        x, y = self.get_pos()
        if self._health > 0.90*(config.Config.ENEMIE_START_HEALTH + 50*self._health_scale):
            pygame.draw.rect(self._display, (0, 255, 0, 255), (x+10, y-10, 40, 5))
        elif self._health > 0.80*(config.Config.ENEMIE_START_HEALTH + 50*self._health_scale):
            pygame.draw.rect(self._display, (0, 200, 0, 255), (x+10, y-10, 36, 5))
        elif self._health > 0.70*(config.Config.ENEMIE_START_HEALTH + 50*self._health_scale):
            pygame.draw.rect(self._display, (0, 150, 0, 255), (x+10, y-10, 32, 5))
        elif self._health > 0.60*(config.Config.ENEMIE_START_HEALTH + 50*self._health_scale):
            pygame.draw.rect(self._display, (0, 100, 0, 255), (x+10, y-10, 28, 5))
        elif self._health > 0.50*(config.Config.ENEMIE_START_HEALTH + 50*self._health_scale):
            pygame.draw.rect(self._display, (230, 180, 31, 255), (x+10, y-10, 24, 5))
        elif self._health > 0.40*(config.Config.ENEMIE_START_HEALTH + 50*self._health_scale):
            pygame.draw.rect(self._display, (222, 120, 40, 255), (x+10, y-10, 20, 5))
        elif self._health > 0.30*(config.Config.ENEMIE_START_HEALTH + 50*self._health_scale):
            pygame.draw.rect(self._display, (255, 0, 0, 255), (x+10, y-10, 16, 5))
        elif self._health > 0.20*(config.Config.ENEMIE_START_HEALTH + 50*self._health_scale):
            pygame.draw.rect(self._display, (200, 0, 0, 255), (x+10, y-10, 12, 5))
        elif self._health > 0.10*(config.Config.ENEMIE_START_HEALTH + 50*self._health_scale):
            pygame.draw.rect(self._display, (150, 0, 0, 255), (x+10, y-10, 8, 5))
        elif self._health > 0*(config.Config.ENEMIE_START_HEALTH + 50*self._health_scale):
            pygame.draw.rect(self._display, (100, 0, 0, 255), (x+10, y-10, 4, 5))


