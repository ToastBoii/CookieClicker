from pygame import mixer

sfxVolume = 0.3


def playSound(file):
    sound = mixer.Sound(file)
    sound.set_volume(sfxVolume)
    sound.play()