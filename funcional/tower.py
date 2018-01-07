import pygame
import math
from lists import *

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
        self._is_poisoned = 0  # 0 ou 1
        self._damage = 0.5 + self._up_factor*200 + self._is_poisoned*5*self._up_factor
        self._price = 50 + self._up_factor*50
        self._upgrade_price = 200 + self._up_factor*100
        self._rect = pygame.Rect(self._pos,self._image.get_size())



    def _attack(self, _enemy):
        if _enemy._status2 == _enemy.POISONED:
            self._is_poisoned = 1
        else:
            self._is_poisoned = 0
        _enemy._health -= self._damage

    def attack_enemies(self, _enemie_list):
        self._attack_list = []
        self.attacking(_enemie_list)

    #FUNCT
    def attacking(self,_enemie_list):
        if len(_enemie_list) > 0:
            _enemy = first(_enemie_list)
            #ONLY ATTACK IF THE ENEMY IS IN RANGE AND THERE ARE ATTACKS LEFT (MAX ATTACKS = LEVEL OF TOWER)
            if self._distance_to(_enemy) <= self._range and len(self._attack_list) < self._level and _enemy.is_active():
                self._attack(_enemy)
                self._attack_list.append(_enemy._pos)
            self.attacking(rest(_enemie_list))

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
        self.draw_attack(self._attack_list,x,y)

    #FUNCT
    def draw_attack(self,list,x,y):
        if len(list)>0:
            pygame.draw.line(self._display, (255, 125, 0), (x + 26, y + 10), first(list), 4)
            self.draw_attack(rest(list),x,y)

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


class PoisonTower(Tower):
    def __init__(self, display, level):
        super(PoisonTower, self).__init__(display, level)
        self._image = pygame.image.load("img/poisontower1.png")
        self._level = level
        self._damage = 2 + self._up_factor*5 + self._is_poisoned*5*self._up_factor
        self._range = 50 + self._up_factor*10
        self._price = 60 + self._up_factor*20
        self._upgrade_price = 250 + self._up_factor*150
        self._is_poisoned = 1


    def _attack(self,enemy):
        enemy._status2 = enemy.POISONED
        enemy._poison_init = enemy._spawn
        enemy._health -= self._damage

    def draw(self):
        self._display.blit(self._image, self.get_pos())
        #(x, y) = self.get_pos()
        for attack in self._attack_list:
            #pygame.draw.line(self._display, (0, 125, 255), (x+26, y+10), attack, 4)
            pygame.draw.circle(self._display, pygame.Color(0, 125, 255, 255), self._pos, self._range, 1)

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
        self._damage = 2 + self._up_factor*12 + self._is_poisoned*5*self._up_factor
        self._range = 50 + self._up_factor*5
        self._price = 70 + self._up_factor*15
        self._upgrade_price = 300 + self._up_factor*180
        self._fire_damage = 1 + self._up_factor*1

    def attack_enemies(self, _enemie_list):
        self._attack_list = []
        for _enemy in _enemie_list:
            #ONLY ATTACK IF THE ENEMY IS IN RANGE AND THERE ARE ATTACKS LEFT (MAX ATTACKS = LEVEL OF TOWER)
            if self._distance_to(_enemy) <= self._range and _enemy.is_active() and _enemy._status != _enemy.BURNING:
                self._attack(_enemy)
                self._attack_list.append(_enemy._pos)

    def _attack(self, enemy):
        enemy._status = enemy.BURNING
        if enemy._status2 == enemy.POISONED:
            self._is_poisoned = 1
        else:
            self._is_poisoned = 0
        enemy._fire_damage = self._fire_damage
        enemy._fire_init = enemy._spawn

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
