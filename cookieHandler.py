import threading
from random import randint


class cookieHandler:
    def __init__(self):
        self.cookies = 0
        self.randOffset = randint(0, 100)
        self.tempCookies = self.randOffset  # tempCookies is for detecting Cheat Engine(it is always cookies + Offset)
        self.cps = 0  # Cookie Per Second
        self.cpc = 1  # Cookie Per Click

        self.pressed = False
        self.running = True

    def update(self, cps, cpp, cookiePressed):

        # Set cps and cpc variables

        self.cps = cps
        self.cpc = cpp

        # Add CPC to Cookies when Cookie is pressed

        if cookiePressed and not self.pressed:
            self.pressed = True
            self.cookies += self.cpc
            self.tempCookies += self.cpc
        elif not cookiePressed:
            self.pressed = False

        # Cheat Engine detection

        if self.tempCookies - self.randOffset != self.cookies:
            self.cookies = 0

    def updateCookies(self):

        # Add Cps Variable every Second

        if self.running:
            threading.Timer(1.0, self.updateCookies).start()
            self.cookies += self.cps
            self.tempCookies += self.cps

    def quit(self):

        # Stop Thread

        self.running = False
