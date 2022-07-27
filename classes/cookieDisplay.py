import pygame as pg
from classes.utils import resource_path, draw_rect_alpha, numberize


class cookieDisplay:
    def __init__(self, screen):
        self.screen = screen
        self.fontLarge = pg.font.Font(resource_path("textures/font/retro.ttf"), 32)
        self.fontSmall = pg.font.Font(resource_path("textures/font/retro.ttf"), 16)

        self.cookieText = self.fontLarge.render("0 Cookies", False, (255, 255, 255))
        self.cpsText = self.fontSmall.render("0 Cps", False, (255, 255, 255))

        self.cookieTextRect = self.cookieText.get_rect()
        self.cpsTextRect = self.cpsText.get_rect()

        self.cookies = 0
        self.cps = 0

    def update(self, cookies, cps):
        # Get Cookies and Cookies Per Second

        self.cookies = cookies
        self.cps = cps

    def render(self):

        # Draw Transparent Background

        draw_rect_alpha(self.screen, (0, 0, 0, 150), (0, self.screen.get_height() / 2 - 320, self.screen.get_width(), 60
                                                      ))

        # Set Text Lables

        self.cookieText = self.fontLarge.render(str(numberize(self.cookies)) + " Cookies", False, (255, 255, 255))
        self.cpsText = self.fontSmall.render(str(numberize(self.cps)) + " Cps", False, (255, 255, 255))

        # Render and Position Labels

        self.cookieTextRect = self.cookieText.get_rect()
        self.cpsTextRect = self.cpsText.get_rect()

        self.cookieTextRect.center = (int(self.screen.get_width() / 2), int(self.screen.get_height() / 2 - 300))
        self.cpsTextRect.center = (int(self.screen.get_width() / 2), int(self.screen.get_height() / 2 - 275))

        self.screen.blit(self.cookieText, self.cookieTextRect)
        self.screen.blit(self.cpsText, self.cpsTextRect)
