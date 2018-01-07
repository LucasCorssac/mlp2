import pygame
import config

class Player:
    def __init__(self):
        self._life = config.Config.PLAYER_START_HEALTH
        self._gold = config.Config.PLAYER_START_GOLD

    def get_life(self):
        return self._life

    def set_life(self, life):
        self._life = life

    def get_gold(self):
        return self._gold

    def set_gold(self, gold):
        self._gold = gold

    def hit(self):
        self._life -= 1