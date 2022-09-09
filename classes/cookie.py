import pygame as pg
from utils import resource_path, step, numberize


class Cookie:
    def __init__(self, screen):
        self.screen = screen

        self.cookieScale = 6

        self.cookieScaleIdle = 6
        self.cookieScaleHover = 5.5
        self.cookieScaleClicked = 5.9

        self.fontSmall = pg.font.Font(resource_path("textures/font/retro.ttf"), 32)
        self.clicked = False
        self.cpcText = []

        self.cookieImgBase = pg.image.load(resource_path("textures/cookie.png"))
        self.cookieImg = pg.transform.scale(self.cookieImgBase, (
            int(pg.display.get_surface().get_width() / self.cookieScale),
            int(pg.display.get_surface().get_width() / self.cookieScale)))
        self.cookieImg.convert()

        self.goldenCookieImgBase = pg.image.load(resource_path("textures/goldenCookie.png"))
        self.goldenCookieImg = pg.transform.scale(self.goldenCookieImgBase, (
            int(pg.display.get_surface().get_width() / self.cookieScale),
            int(pg.display.get_surface().get_width() / self.cookieScale)))
        self.goldenCookieImg.convert()

        self.cookieRect = self.cookieImg.get_rect()
        self.cookieRect.center = (int(self.screen.get_width() / 2), int(self.screen.get_height() / 2))

    def update(self, mousePos, mouseClicked, cpc):

        # Animate Cookie

        if self.cookieRect.collidepoint(mousePos):
            if mouseClicked:
                self.cookieScale = step(self.cookieScale, self.cookieScaleClicked, 0.2)

                if not self.clicked:
                    self.clicked = True

                    self.cpcText.append([self.fontSmall.render("+" + numberize(cpc), False, (255, 255, 255)), 1,
                                         mousePos])
            else:
                self.cookieScale = step(self.cookieScale, self.cookieScaleHover, 0.1)
                self.clicked = False
        else:
            self.cookieScale = step(self.cookieScale, self.cookieScaleIdle, 0.1)

    def checkCookiePressed(self, mousePos, mouseClicked):

        # Check Mouse Collision

        if self.cookieRect.collidepoint(mousePos) and mouseClicked:
            return True
        else:
            return False

    def render(self, cpc, deltaTime, skin):

        # Scale Image

        if skin:
            self.goldenCookieImg = pg.transform.scale(self.goldenCookieImgBase, (
                int(pg.display.get_surface().get_width() / self.cookieScale),
                int(pg.display.get_surface().get_width() / self.cookieScale)))
            self.goldenCookieImg.convert()
        else:
            self.cookieImg = pg.transform.scale(self.cookieImgBase, (
                int(pg.display.get_surface().get_width() / self.cookieScale),
                int(pg.display.get_surface().get_width() / self.cookieScale)))
            self.cookieImg.convert()

        # Render and Position Image

        goldenCookieRect = self.goldenCookieImg.get_rect()
        goldenCookieRect.center = (int(self.screen.get_width() / 2), int(self.screen.get_height() / 2))

        self.cookieRect = self.cookieImg.get_rect()
        self.cookieRect.center = (int(self.screen.get_width() / 2), int(self.screen.get_height() / 2))

        if skin:
            self.screen.blit(self.goldenCookieImg, goldenCookieRect)
        else:
            self.screen.blit(self.cookieImg, self.cookieRect)

        # Cookies per Click Text

        for i in range(len(self.cpcText)):
            self.cpcText[i][1] -= deltaTime

            if self.cpcText[i][1] <= 0:
                self.cpcText.pop(i)
                break

        for i in range(len(self.cpcText)):
            textRect = self.cpcText[i][0].get_rect()
            self.cpcText[i][2] = (self.cpcText[i][2][0], self.cpcText[i][2][1] - deltaTime * 80)
            textRect.center = self.cpcText[i][2]

            transparentImage = self.cpcText[i][0].copy()
            transparentImage.convert()

            alpha = int(self.cpcText[i][1] * 255)
            transparentImage.set_alpha(alpha)

            self.screen.blit(transparentImage, textRect)
