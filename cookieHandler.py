import threading


class cookieHandler:
    def __init__(self):
        self.cookies = 0
        self.cps = 0  # Cookie Per Second
        self.cpc = 1  # Cookie Per Click

        self.pressed = False
        self.running = True

    def update(self, cps, cpp, cookiePressed):
        self.cps = cps
        self.cpc = cpp

        # Add CPC to Cookies when Cookie is pressed

        if cookiePressed and not self.pressed:
            self.pressed = True
            self.cookies += self.cpc
        elif not cookiePressed:
            self.pressed = False

    def updateCookies(self):

        # Add Cps Variable every Second

        if self.running:
            threading.Timer(1.0, self.updateCookies).start()
            self.cookies += self.cps

    def quit(self):

        # Stop Thread

        self.running = False
