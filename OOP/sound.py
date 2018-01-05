from pygame import *

class Sound:
    def __init__(self):
        mixer.init()

    def play_game_bgm(self):
        game_BGM = "game.ogg"
        mixer.music.load(game_BGM)
        mixer.music.play(-1)

    def play_menu_bgm(self):
        menu_BGM = "menu.ogg"
        mixer.music.load(menu_BGM)
        mixer.music.play(-1)

    def stop_bgm(self):
        mixer.music.stop()