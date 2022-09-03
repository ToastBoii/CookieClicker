import pygame as pg
from sounds.soundManager import playSound
from utils import resource_path, step, numberize

class Shop:
    def __init__(self, screen):
        self.screen = screen

        self.boughtItems = [0, 0, 0, 0]
        self.itemPrice = [10, 100, 1000, 15000]
        self.cpsPerItem = [0.1, 1, 7, 45]

        self.calcItemPrice = [10, 100, 1000, 15000]

        self.itemNames = ["AutoClicker", "Cook", "Farm", "Mine"]
        self.itemImages = []

        for i in range(len(self.itemNames)):
            self.itemImages.append(pg.image.load(resource_path("textures/shop/itemIcons/item" + str(i + 1) + ".png")))
            self.itemImages[i] = pg.transform.scale(self.itemImages[i], (48, 48))
            self.itemImages[i].convert()

        self.fontSmall = pg.font.Font(resource_path("textures/font/retro.ttf"), 16)
        self.fontBig = pg.font.Font(resource_path("textures/font/retro.ttf"), 32)

        self.cpsFromItems = 0

        self.opened = False

        self.oldPressed = False
        self.oldPressed2 = -1
        self.menuAnimation = 0

        self.X = 30

        self.openedX = 330  # 240
        self.closedX = 30

        self.shopBg = []

        self.shopBg.append(pg.image.load(resource_path("textures/shop/buttonBg.png")))
        self.shopBg.append(pg.image.load(resource_path("textures/shop/buttonBgHover.png")))
        self.shopBg.append(pg.image.load(resource_path("textures/shop/buttonBgClicked.png")))

        for i in range(3):
            self.shopBg[i] = pg.transform.scale(self.shopBg[i], (270, 58))
            self.shopBg[i].convert()

        self.shopBgState = [0, 0, 0, 0]
        self.shopBgPressed = [0, 0, 0, 0]

        self.debt = 0

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

    def update(self, deltaTime, mousePos, mouseClicked, cookies):
        # Shop open and close animation

        if self.shopMenuRect.collidepoint(mousePos) and mouseClicked:
            if not self.oldPressed:
                playSound(resource_path("sounds/click.wav"))
                self.opened = not self.opened
                self.oldPressed = True
        else:
            if not mouseClicked:
                if self.oldPressed:
                    playSound(resource_path("sounds/unclick.wav"))
                self.oldPressed = False

        if self.opened:
            if self.menuAnimation < 6:
                self.menuAnimation += deltaTime * 12
            if self.menuAnimation > 6:
                self.menuAnimation = 6

            self.X = step(self.X, self.openedX, deltaTime * 500)
        else:
            if self.menuAnimation > 0:
                self.menuAnimation -= deltaTime * 12
                if self.menuAnimation < 0:
                    self.menuAnimation = 0

            self.X = step(self.X, self.closedX,  deltaTime * 500)

        # Calculate Price of Items

        for i in range(len(self.calcItemPrice)):
            # Formula for Calculating cost for the buildings: Base Cost * 1.15 ** N(number of items)
            self.calcItemPrice[i] = self.itemPrice[i] * 1.15 ** self.boughtItems[i]

        # Button Pressed

        for i in range(len(self.itemPrice)):
            buttonRect = self.shopBg[0].get_rect()
            buttonRect.topright = (self.X - 60 + 5, 5 + 60 * i)

            if buttonRect.collidepoint(mousePos):
                if mouseClicked:
                    if self.shopBgPressed[i] == 0:
                        self.shopBgPressed[i] = 1
                        if cookies >= self.calcItemPrice[i]:
                            self.boughtItems[i] += 1
                            self.debt += self.calcItemPrice[i]

                    self.shopBgState[i] = 2
                    if self.oldPressed2 == -1:
                        playSound(resource_path("sounds/click.wav"))
                        self.oldPressed2 = i
                else:
                    if self.oldPressed2 == i:
                        self.oldPressed2 = -1
                        playSound(resource_path("sounds/unclick.wav"))

                    self.shopBgPressed[i] = 0
                    self.shopBgState[i] = 1
            else:
                if self.oldPressed2 == i:
                    self.oldPressed2 = -1
                    playSound(resource_path("sounds/unclick.wav"))

                self.shopBgPressed[i] = 0
                self.shopBgState[i] = 0

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
            if self.X != 30:
                # Images
                bgRect = self.shopBg[0].get_rect()
                bgRect.topleft = (self.shopRect.topleft[0] + 5, 5 + 60 * i)

                itemRect = self.itemImages[i].get_rect()
                itemRect.topleft = (self.shopRect.topleft[0] + 10, 10 + 60 * i)

                self.screen.blit(self.shopBg[self.shopBgState[i]], bgRect)
                self.screen.blit(self.itemImages[i], itemRect)

                # Text
                name = self.fontSmall.render(self.itemNames[i], False, (255, 255, 255))
                cps = self.fontSmall.render("CPS: " + str(self.cpsPerItem[i]), False, (255, 255, 255))
                cost = self.fontSmall.render(numberize(self.calcItemPrice[i]) + " Cookies", False, (255, 255, 255))
                count = self.fontBig.render(str(self.boughtItems[i]), False, (255, 255, 255))

                nameRect = name.get_rect()
                cpsRect = cps.get_rect()
                costRect = cost.get_rect()
                countRect = count.get_rect()
                nameRect.topleft = (self.shopRect.topleft[0] + 65, 10 + 60 * i)
                cpsRect.topleft = (self.shopRect.topleft[0] + 65, 25 + 60 * i)
                costRect.topleft = (self.shopRect.topleft[0] + 65, 40 + 60 * i)
                countRect.topright = (self.shopRect.topright[0] - 30, 15 + 60 * i)

                self.screen.blit(name, nameRect)
                self.screen.blit(cps, cpsRect)
                self.screen.blit(cost, costRect)
                self.screen.blit(count, countRect)
