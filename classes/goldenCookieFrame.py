import pygame as pg
from utils import resource_path


class GoldenCookieFrame:
    def __init__(self, screen):
        self.screen = screen

        self.framePaths = ["textures/goldenCookies/frenzy.png", "textures/goldenCookies/clickBoost.png"]
        self.frame = pg.image.load(resource_path("textures/goldenCookies/frame.png"))

    def render(self, active, cookieEffect):
        if active:

            # Render the Active Effect

            image = pg.image.load(resource_path(self.framePaths[cookieEffect]))
            image = pg.transform.scale(image, (
                int(pg.display.get_surface().get_width() / 20),
                int(pg.display.get_surface().get_width() / 20)))

            imageRect = image.get_rect()
            imageRect.topright = (pg.display.get_surface().get_width() - 10, 10)

            self.frame = pg.transform.scale(self.frame, (
                int(pg.display.get_surface().get_width() / 20),
                int(pg.display.get_surface().get_width() / 20)))

            frameRect = self.frame.get_rect()
            frameRect.topright = (pg.display.get_surface().get_width() - 10, 10)

            self.screen.blit(image, imageRect)
            self.screen.blit(self.frame, frameRect)
