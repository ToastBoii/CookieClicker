import pygame as pg
from sounds.soundManager import playSound
from utils import resource_path, step
from random import randint
from time import sleep
from math import sin
import threading


class GoldenCookie:
    def __init__(self, screen):
        self.screen = screen

        self.angle = 0
        self.angleTemp = 0
        self.minWaitTime = 50
        self.maxWaitTime = 150
        self.waitTime = randint(self.minWaitTime, self.maxWaitTime)
        self.hideTime = 5
        self.visible = False

        self.active = False
        self.cookieEffect = 0
        self.thread = None

        self.scale = 23

        self.scaleIdle = 23
        self.scaleHover = 26

        self.goldenCookieBase = pg.image.load(resource_path("textures/goldenCookies/goldenCookie.png"))
        self.goldenCookie = pg.transform.scale(self.goldenCookieBase, (
            int(pg.display.get_surface().get_width() / self.scale),
            int(pg.display.get_surface().get_width() / self.scale)))
        self.goldenCookie.convert()

        self.goldenCookieRect = self.goldenCookie.get_rect()
        self.cookieRotated = pg.transform.rotate(self.goldenCookie, self.angle)

        self.randX = randint(self.goldenCookie.get_width(), pg.display.get_surface().get_width() -
                             self.goldenCookie.get_width() * 2)
        self.randY = randint(self.goldenCookie.get_height(), pg.display.get_surface().get_height() -
                             self.goldenCookie.get_height() * 2)

    def update(self, deltaTime, mousePos, mouseClicked):

        # Generate when to show up next

        if self.waitTime <= 0:
            self.visible = True

            self.waitTime = randint(self.minWaitTime, self.maxWaitTime)
        else:
            self.waitTime -= 1 * deltaTime

        # Update Angle in a Sin Wave

        if self.angleTemp >= 360:
            self.angleTemp = 0
        else:
            self.angleTemp += 0.2

        self.angle = int(sin(self.angleTemp) * 10)

        # Calculate When to Hide

        if self.visible:
            self.hideTime -= 1 * deltaTime

        if self.hideTime <= 0:
            self.hideTime = 5
            self.visible = False

        # Generate New Position on Click
        # Update Active Variable
        # Handle Scale Animations

        if self.goldenCookieRect.collidepoint(mousePos) and self.visible:
            self.scale = step(self.scale, self.scaleHover, 0.8)
            if mouseClicked:
                playSound(resource_path("sounds/click.wav"))
                self.randX = randint(self.goldenCookie.get_width(), pg.display.get_surface().get_width() -
                                     self.goldenCookie.get_width() * 2)
                self.randY = randint(self.goldenCookie.get_height(), pg.display.get_surface().get_height() -
                                     self.goldenCookie.get_height() * 2)
                self.visible = False
                self.cookieEffect = randint(0, 1)  # Change after adding another Effect
                self.thread = threading.Thread(target=self.effectCountdown)
                self.thread.start()
        else:
            self.scale = step(self.scale, self.scaleIdle, 0.8)

        # Update Scale and Rotation

        self.goldenCookie = pg.transform.scale(self.goldenCookieBase, (
            int(pg.display.get_surface().get_width() / self.scale),
            int(pg.display.get_surface().get_width() / self.scale)))
        self.goldenCookie.convert()

        self.cookieRotated = pg.transform.rotate(self.goldenCookie, self.angle)

    def effectCountdown(self):
        self.active = True
        sleep(20)
        self.active = False

    def render(self):
        if self.visible:
            # Render and Position Golden Cookie

            self.goldenCookieRect.center = (self.randX, self.randY)

            rotatedImage = pg.transform.rotate(self.goldenCookie, self.angle)
            rotatedRect = rotatedImage.get_rect(center=self.goldenCookie.get_rect(
                center=self.goldenCookieRect.center).center)

            self.screen.blit(rotatedImage, rotatedRect)
