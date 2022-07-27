import pygame as pg
from utils import resource_path, draw_rect_alpha, numberize


class cookieDisplay:
    def __init__(self, screen):
        self.screen = screen
        self.fontLarge = pg.font.Font(resource_path("textures/font/retro.ttf"), 32)
        self.fontSmall = pg.font.Font(resource_path("textures/font/retro.ttf"), 16)

        self.cookieText = self.fontLarge.render("0 Cookies", False, (255, 255, 255))
        self.cpsText = self.fontSmall.render("0 Cps", False, (255, 255, 255))

        self.cookieTextRect = self.cookieText.get_rect()
        self.cpsTextRect = self.cpsText.get_rect()

    def render(self, cookies, cps):

        # Draw Transparent Background

        draw_rect_alpha(self.screen, (0, 0, 0, 150), (0, self.screen.get_height() / 2 - 320, self.screen.get_width(), 60
                                                      ))

        # Set Text Lables

        self.cookieText = self.fontLarge.render(str(numberize(cookies)) + " Cookies", False, (255, 255, 255))
        self.cpsText = self.fontSmall.render(str(numberize(cps)) + " Cps", False, (255, 255, 255))

        # Render and Position Labels

        self.cookieTextRect = self.cookieText.get_rect()
        self.cpsTextRect = self.cpsText.get_rect()

        self.cookieTextRect.center = (int(self.screen.get_width() / 2), int(self.screen.get_height() / 2 - 300))
        self.cpsTextRect.center = (int(self.screen.get_width() / 2), int(self.screen.get_height() / 2 - 275))

        self.screen.blit(self.cookieText, self.cookieTextRect)
        self.screen.blit(self.cpsText, self.cpsTextRect)
