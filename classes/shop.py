import pygame as pg
from utils import resource_path


class Shop:
    def __init__(self, screen):
        self.screen = screen

        self.menuAnimation = 0

        self.shopMenuImages = []
        self.shopMenu = []

        for i in range(0, 10):
            self.shopMenuImages.append(pg.image.load(resource_path("textures/shop/menuButton/menu" + str(i) + ".png")))

            self.shopMenu.append(pg.transform.scale(self.shopMenuImages[i], (48, 48)))
            self.shopMenu[i].convert()

        self.shopMenuRect = self.shopMenuImages[0].get_rect()

    def update(self, deltaTime):
        self.menuAnimation += deltaTime * 9

        if self.menuAnimation >= 9:
            self.menuAnimation = 0

    def render(self):
        self.shopMenuRect.topleft = (30, 30)

        self.screen.blit(self.shopMenu[round(self.menuAnimation)], self.shopMenuRect)
