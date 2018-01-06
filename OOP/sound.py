from pygame import *
import config


class Sound:
    def __init__(self):
        mixer.init()


    def play_game_bgm(self, audio):
        mixer.music.load(audio)
        mixer.music.play(-1)

    def play_menu_bgm(self, audio):

        mixer.music.load(audio)
        mixer.music.play(-1)

    def stop_bgm(self):
        mixer.music.stop()

    def play_sound(self):
        mixer.Sound