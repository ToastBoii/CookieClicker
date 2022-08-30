import pygame as pg
from utils import resource_path


class Shop:
    def __init__(self, screen):
        self.screen = screen

        self.opened = False

        self.oldPressed = False
        self.menuAnimation = 0

        self.shopMenuImages = []
        self.shopMenu = []

        for i in range(0, 7):
            self.shopMenuImages.append(pg.image.load(resource_path("textures/shop/menuButton/menu" + str(i) + ".png")))

            self.shopMenu.append(pg.transform.scale(self.shopMenuImages[i], (48, 48)))
            self.shopMenu[i].convert()

        self.shopMenuRect = self.shopMenuImages[1].get_rect()
        self.shopMenuRect.topleft = (30, 30)

    def update(self, deltaTime, mousePos, mouseClicked):
        collider = self.shopMenu[1].get_rect()
        collider.topleft = (30, 30)
        if collider.collidepoint(mousePos) and mouseClicked:
            if not self.oldPressed:
                self.opened = not self.opened
                self.oldPressed = True
        else:
            self.oldPressed = False

        if self.opened:
            if self.menuAnimation < 6:
                self.menuAnimation += deltaTime * 12
            if self.menuAnimation > 6:
                self.menuAnimation = 6
        else:
            if self.menuAnimation > 0:
                self.menuAnimation -= deltaTime * 12
                if self.menuAnimation < 0:
                    self.menuAnimation = 0

    def render(self):
        self.shopMenuRect.topleft = (30, 30)

        self.screen.blit(self.shopMenu[round(self.menuAnimation)], self.shopMenuRect)
