from pygame import *
import config


class Sound:
    def __init__(self):
        mixer.init()


    def play_BGM(self, audio):
        mixer.music.load(audio)
        mixer.music.set_volume(0.05)
        mixer.music.play(-1)

    def stop_BGM(self):
        mixer.music.stop()

    def start_BGM(self):
        mixer.music.play()

    def play_Sound(self, audio):
        effect = mixer.Sound(audio)
        effect.set_volume(0.05)
        mixer.Sound.play(effect)