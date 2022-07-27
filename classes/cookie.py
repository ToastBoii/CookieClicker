import pygame as pg
from utils import resource_path, step


class Cookie:
    def __init__(self, screen):
        self.screen = screen

        self.cookieScale = 6

        self.cookieScaleIdle = 6
        self.cookieScaleHover = 5.5
        self.cookieScaleClicked = 5.9

        self.cookieImgBase = pg.image.load(resource_path("textures/cookie.png"))
        self.cookieImg = pg.transform.scale(self.cookieImgBase, (
            int(pg.display.get_surface().get_width() / self.cookieScale),
            int(pg.display.get_surface().get_width() / self.cookieScale)))
        self.cookieImg.convert()

        self.cookieRect = self.cookieImg.get_rect()
        self.cookieRect.center = (int(self.screen.get_width() / 2), int(self.screen.get_height() / 2))

    def update(self, mousePos, mouseClicked):

        # Animate Cookie

        if self.cookieRect.collidepoint(mousePos):
            if mouseClicked:
                self.cookieScale = step(self.cookieScale, self.cookieScaleClicked, 0.1)
            else:
                self.cookieScale = step(self.cookieScale, self.cookieScaleHover, 0.1)
        else:
            self.cookieScale = step(self.cookieScale, self.cookieScaleIdle, 0.1)

    def checkCookiePressed(self, mousePos, mouseClicked):

        # Check Mouse Collision

        if self.cookieRect.collidepoint(mousePos) and mouseClicked:
            return True
        else:
            return False

    def render(self):

        # Scale Image

        self.cookieImg = pg.transform.scale(self.cookieImgBase, (
            int(pg.display.get_surface().get_width() / self.cookieScale),
            int(pg.display.get_surface().get_width() / self.cookieScale)))
        self.cookieImg.convert()

        # Render and Position Image

        self.cookieRect = self.cookieImg.get_rect()
        self.cookieRect.center = (int(self.screen.get_width() / 2), int(self.screen.get_height() / 2))

        self.screen.blit(self.cookieImg, self.cookieRect)
