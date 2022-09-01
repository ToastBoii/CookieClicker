from pygame import mixer

sfxVolume = 0.3

mixer.init()


def playSound(file):
    sound = mixer.Sound(file)
    sound.set_volume(sfxVolume)
    sound.play()