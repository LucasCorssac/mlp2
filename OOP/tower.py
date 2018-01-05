import pygame
import math


class Tower:
    def __init__(self, display, level):
        self._display = display
        self._start_pos = (0, 0)
        self._pos = self._start_pos
        self._image = pygame.image.load("img/tower1.png")
        self._level = level
        self._up_factor = self._level - 1
        self._id = 0
        self._range = 100 + self._up_factor*10
        self._attack_list = []
        self._damage = 0.5 + self._up_factor*200
        self._price = 50 + self._up_factor*50
        self._upgrade_price = 200 + self._up_factor*100


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

    def get_price(self):
        return self._price

    def get_upgrade_price(self):
        return self._upgrade_price

    def get_range(self):
        return self._range

    def get_damage(self):
        return self._damage

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
        p2x, p2y = enemy.get_pos()
        x = p1x - p2x
        y = p1y - p2y
        result = math.sqrt(math.pow(x,2) + math.pow(y,2))
        return result

    def get_level(self):
        return self._level

    def set_level(self, l):
        self._level = l

    def upgrade_level(self):
        self.set_level(self.get_next_level())
        self._damage = self.get_next_damage()
        self._range = self.get_next_range()
        self._price = self.get_next_price()
        self._upgrade_price = self.get_next_upgrade_price()

    def draw(self):
        self._display.blit(self._image, self.get_pos())
        (x, y) = self.get_pos()
        for attack in self._attack_list:
            pygame.draw.line(self._display, (255, 125, 0), (x+26, y+10), attack, 4)

    def get_pos(self):
        x, y = self._pos
        return x-26, y -30

    def set_pos(self, x, y):
        self._pos = (x, y)

    #GET NEXT LEVEL ATTRIBUTES
    def get_next_level(self):
        return self._level + 1

    def get_next_damage(self):
        return self._damage + (self._level*10)

    def get_next_range(self):
        return self._range + (self._level*10)

    def get_next_price(self):
        return self._price + (self._level*50)

    def get_next_upgrade_price(self):
        return self._upgrade_price + (self._level*100)


class IceTower(Tower):
    def __init__(self, display, level):
        super(IceTower, self).__init__(display, level)
        self._image = pygame.image.load("img/icetower1.png")
        self._level = level
        self._damage = 20 + self._up_factor*5
        self._range = 50 + self._up_factor*10
        self._price = 60 + self._up_factor*20
        self._upgrade_price = 250 + self._up_factor*150

    # GET NEXT LEVEL ATTRIBUTES
    def get_next_level(self):
        return self._level + 1

    def get_next_damage(self):
        return self._damage + (self._level * 5)

    def get_next_range(self):
        return self._range + (self._level * 10)

    def get_next_price(self):
        return self._price + (self._level * 20)

    def get_next_upgrade_price(self):
        return self._upgrade_price + (self._level * 150)

class FireTower(Tower):
    def __init__(self, display, level):
        super(FireTower, self).__init__(display, level)
        self._image = pygame.image.load("img/firetower1.png")
        self._level = level
        self._damage = 2 + self._up_factor*12
        self._range = 50 + self._up_factor*5
        self._price = 70 + self._up_factor*15
        self._upgrade_price = 300 + self._up_factor*180

    def get_next_level(self):
        return self._level + 1

    def get_next_damage(self):
        return self._damage + (self._level * 12)

    def get_next_range(self):
        return self._range + (self._level * 5)

    def get_next_price(self):
        return self._price + (self._level * 15)

    def get_next_upgrade_price(self):
        return self._upgrade_price + (self._level * 180)
