import pygame as pg


class CheatCode:
    def __init__(self):
        self.CODE = [pg.K_UP, pg.K_UP, pg.K_DOWN, pg.K_DOWN, pg.K_LEFT, pg.K_RIGHT, pg.K_LEFT, pg.K_RIGHT, pg.K_b,
                     pg.K_a, pg.K_RETURN]
        self.code = []
        self.index = 0

        self.active = False

    def update(self, eventKey):
        self.index = min(len(self.CODE) - 1, max(self.index, 0))

        if eventKey == self.CODE[self.index]:
            self.code.append(eventKey)
            self.index += 1
            if self.code == self.CODE:
                self.index = 0
                self.code = []
                self.active = not self.active
