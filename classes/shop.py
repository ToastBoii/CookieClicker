import pygame as pg
from utils import resource_path, step


class Shop:
    def __init__(self, screen):
        self.screen = screen

        self.boughtItems = [10, 0, 0, 0]
        self.itemPrice = [10, 100, 1000, 15000]
        self.cpsPerItem = [0.1, 1, 7, 45]

        # Formula for Calculating cost for the buildings: Base Cost * 1.15 ** N(number of items)

        self.itemNames = ["AutoClicker", "Cook", "Farm", "Mine"]
        self.itemImages = []

        for i in range(len(self.itemNames)):
            self.itemImages.append(pg.image.load(resource_path("textures/shop/itemIcons/item" + str(i+1) + ".png")))
            self.itemImages[i] = pg.transform.scale(self.itemImages[i], (48, 48))
            self.itemImages[i].convert()

        self.fontSmall = pg.font.Font(resource_path("textures/font/retro.ttf"), 16)

        self.cpsFromItems = 0

        self.opened = False

        self.oldPressed = False
        self.menuAnimation = 0

        self.X = 30

        self.openedX = 330 # 240
        self.closedX = 30

        self.shopMenuImages = []
        self.shopMenu = []

        for i in range(0, 7):
            self.shopMenuImages.append(pg.image.load(resource_path("textures/shop/menuButton/menu" + str(i) + ".png")))

            self.shopMenu.append(pg.transform.scale(self.shopMenuImages[i], (48, 48)))
            self.shopMenu[i].convert()

        self.shopMenuRect = self.shopMenu[0].get_rect()
        self.shopMenuRect.topleft = (self.X, 30)

        self.shopBase = pg.image.load(resource_path("textures/shop/shop.png"))

        self.shopImage = pg.transform.scale(self.shopBase, (300, pg.display.get_surface().get_size()[1]))
        self.shopImage.convert()

        self.shopRect = self.shopImage.get_rect()
        self.shopRect.topright = (self.X - 30, 0)

    def update(self, deltaTime, mousePos, mouseClicked):
        # Shop open and close animation

        if self.shopMenuRect.collidepoint(mousePos) and mouseClicked:
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

            self.X = step(self.X, self.openedX, 20)
        else:
            if self.menuAnimation > 0:
                self.menuAnimation -= deltaTime * 12
                if self.menuAnimation < 0:
                    self.menuAnimation = 0

            self.X = step(self.X, self.closedX, 20)

        # Calculate Cps gained from bought items

        self.cpsFromItems = 0

        for i in range(len(self.boughtItems)):
            self.cpsFromItems += self.boughtItems[i] * self.cpsPerItem[i]

    def render(self):

        # MenuButton

        self.shopMenuRect.topleft = (self.X, 30)
        self.screen.blit(self.shopMenu[round(self.menuAnimation)], self.shopMenuRect)

        # Menu

        self.shopRect.topright = (self.X - 30, 0)
        self.screen.blit(self.shopImage, self.shopRect)

        # Shop Items

        for i in range(len(self.itemImages)):
            # Images
            itemRect = self.itemImages[i].get_rect()
            itemRect.topleft = (self.shopRect.topleft[0] + 10, 10 + 60 * i)

            self.screen.blit(self.itemImages[i], itemRect)

            # Text
            if self.X != 30:
                name = self.fontSmall.render(self.itemNames[i], False, (255, 255, 255))
                cps = self.fontSmall.render("CPS: " + str(self.cpsPerItem[i]), False, (255, 255, 255))

                nameRect = name.get_rect()
                cpsRect = cps.get_rect()
                nameRect.topleft = (self.shopRect.topleft[0] + 65, 10 + 60 * i)
                cpsRect.topleft = (self.shopRect.topleft[0] + 65, 30 + 60 * i)

                self.screen.blit(name, nameRect)
                self.screen.blit(cps, cpsRect)
