from pygame import *
import config


class Sound:
    def __init__(self):
        mixer.init()


    def play_BGM(self, audio):
        mixer.music.load(audio)
        mixer.music.play(-1)

    def stop_BGM(self):
        mixer.music.stop()

    def play_Sound(self):
        mixer.Sound