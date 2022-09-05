import pygame as pg
from utils import resource_path, step
from sounds.soundManager import playSound
from base64 import b64decode, b64encode, encode, decode


class Settings:
    def __init__(self, screen):
        self.screen = screen

        self.shopImage = pg.image.load(resource_path("textures/shop/shop.png"))
        self.fontBig = pg.font.Font(resource_path("textures/font/retro.ttf"), 32)

        self.X = pg.display.get_surface().get_width() - 30

        self.openedX = pg.display.get_surface().get_width() - 330
        self.closedX = pg.display.get_surface().get_width() - 30

        self.opened = False
        self.oldPressed = False
        self.oldPressed2 = -1
        self.menuAnimation = 0

        self.settingsMenu = pg.image.load(resource_path("textures/shop/menuButton/settingsMenu.png"))
        self.settingsMenu = pg.transform.scale(self.settingsMenu, (48, 48))
        self.settingsMenu.convert()

        self.shopMenuRect = self.settingsMenu.get_rect()
        self.shopMenuRect.topleft = (self.X, 30)

        self.shopImage = pg.transform.flip(self.shopImage, True, False)
        self.shopImage = pg.transform.scale(self.shopImage, (300, pg.display.get_surface().get_size()[1]))
        self.shopImage.convert()

        self.shopRect = self.shopImage.get_rect()
        self.shopRect.topright = (self.X - 30, 0)

        self.shopBg = []

        self.shopBg.append(pg.image.load(resource_path("textures/shop/buttonBg.png")))
        self.shopBg.append(pg.image.load(resource_path("textures/shop/buttonBgHover.png")))
        self.shopBg.append(pg.image.load(resource_path("textures/shop/buttonBgClicked.png")))

        for i in range(3):
            self.shopBg[i] = pg.transform.scale(self.shopBg[i], (270, 58))
            self.shopBg[i].convert()

        self.shopBgState = [0, 0]
        self.shopBgPressed = [0, 0]

        self.loadedCookies = 0
        self.loadedBoughtItems = []
        self.load = False

    def update(self, deltaTime, mousePos, mouseClicked, cookies, boughtItems):
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
            self.X = step(self.X, self.openedX, deltaTime * 500)
        else:
            self.X = step(self.X, self.closedX, deltaTime * 500)

        # Button Pressed

        for i in range(len(self.shopBgState)):
            buttonRect = self.shopBg[0].get_rect()
            buttonRect.topright = (self.X + 330 - 5, 5 + 60 * i)

            if buttonRect.collidepoint(mousePos):
                if mouseClicked:
                    if self.shopBgPressed[i] == 0:
                        self.shopBgPressed[i] = 1

                        if i == 0:
                            file = open("save.cc", 'wb')

                            saveString = str(cookies) + ";" + str(boughtItems)
                            encodedString = b64encode(saveString.encode('ascii'))
                            print(encodedString)
                            file.write(encodedString)
                            file.close()
                        elif i == 1:
                            file = open("save.cc", 'rb')

                            encStr = file.read()
                            byteStr = b64decode(encStr)

                            objects = byteStr.decode().split(";")

                            self.loadedCookies = float(objects[0])

                            stringObject = objects[1]
                            stringObject.replace('[', ' ')
                            stringObject.replace(']', ' ')
                            self.loadedBoughtItems = stringObject.split(" ")

                            for j in range(len(self.loadedBoughtItems)):
                                self.loadedBoughtItems[j] = self.loadedBoughtItems[j].replace(",", "")
                                self.loadedBoughtItems[j] = self.loadedBoughtItems[j].replace("[", "")
                                self.loadedBoughtItems[j] = self.loadedBoughtItems[j].replace("]", "")

                                self.loadedBoughtItems[j] = int(self.loadedBoughtItems[j])

                            self.load = True

                            file.close()

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

    def render(self):

        # MenuButton

        self.shopMenuRect.topright = (self.X + 20, 10)
        self.screen.blit(self.settingsMenu, self.shopMenuRect)

        if self.X != 30:
            # Menu

            self.shopRect.topright = (self.X + 330, 0)
            self.screen.blit(self.shopImage, self.shopRect)

            for i in range(len(self.shopBgState)):

                # Buttons

                buttonRect = self.shopBg[0].get_rect()
                buttonRect.topright = (self.X + 330 - 5, 5 + 60 * i)

                self.screen.blit(self.shopBg[self.shopBgState[i]], buttonRect)

                # Text

                text = None
                if i == 0:
                    text = self.fontBig.render("Save", False, (255, 255, 255))
                elif i == 1:
                    text = self.fontBig.render("Load", False, (255, 255, 255))

                textRect = text.get_rect()
                textRect.topright = (self.X + 330 - buttonRect.width / 2 + textRect.width / 2, 15 + 60 * i)

                self.screen.blit(text, textRect)
