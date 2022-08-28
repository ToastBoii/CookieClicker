import threading
from random import randint
from sounds.soundManager import playSound


class cookieHandler:
    def __init__(self):
        self.cookies = 0
        self.randOffset = randint(0, 100)
        self.cheatCookies = self.randOffset  # cheatCookies is for detecting Cheat Engine(it is always cookies + Offset)
        self.cps = 0  # Cookie Per Second
        self.tempCps = 0
        self.cpc = 1  # Cookie Per Click

        self.active = False
        self.cookieEffect = 0

        self.pressed = False
        self.running = True

    def update(self, cps, cpp, cookiePressed, active, cookieEffect):

        # Set cps and cpc variables

        self.cps = cps
        self.cpc = cpp

        # Update Golden Cookie Effects

        self.active = active
        self.cookieEffect = cookieEffect

        # Check if first Golden Cookie Effect is active

        tempCookies = self.cpc

        if self.active and self.cookieEffect == 1:
            tempCookies = self.cpc * 5

        # Add CPC to Cookies when Cookie is pressed

        if cookiePressed and not self.pressed:
            playSound('sounds/click.wav')
            self.pressed = True
            self.cookies += tempCookies
            self.cheatCookies += tempCookies
        elif not cookiePressed:
            if self.pressed:
                playSound('sounds/unclick.wav')
            self.pressed = False

        # Cheat Engine detection

        if self.cheatCookies - self.randOffset != self.cookies:
            self.cookies = 0

    def updateCookies(self):

        # Check if first Golden Cookie Effect is active

        if self.active and self.cookieEffect == 0:
            self.tempCps = self.cps * 8
        else:
            self.tempCps = self.cps

        # Add Cps Variable every Second

        if self.running:
            threading.Timer(1.0, self.updateCookies).start()
            self.cookies += self.tempCps
            self.cheatCookies += self.tempCps

    def quit(self):

        # Stop Thread

        self.running = False
