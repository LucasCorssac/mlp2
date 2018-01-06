from pygame import *
import config


class Sound:
    def __init__(self):
        mixer.init()


    def play_BGM(self, audio):
        mixer.music.load(audio)
<<<<<<< HEAD
        mixer.music.set_volume(0.05)
=======
        mixer.music.set_volume(0)
>>>>>>> 24c8b3bdb9c308a4538a00d47754a180e85841df
        mixer.music.play(-1)

    def stop_BGM(self):
        mixer.music.stop()

    def play_Sound(self, audio):
        effect = mixer.Sound(audio)
        effect.set_volume(0.05)
        mixer.Sound.play(effect)