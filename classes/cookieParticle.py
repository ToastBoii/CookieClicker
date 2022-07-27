import pygame as pg
from classes.utils import resource_path
from random import randint


class CookieParticle:
    def __init__(self, screen):
        self.screen = screen

        self.spawnTime = 0.05
        self.cpsRanges = [10, 100, 500, 1000, 1000000, 1000000000, 1000000000000, 1000000000000000,
                          1000000000000000000, 1000000000000000000000]
        self.spawnIntervals = [5, 3, 2, 1, 0.8, 0.5, 0.3, 0.2, 0.1, 0.05]

        self.particles = []
        self.particleRect = []
        self.angles = []

        self.pressed = False

    def update(self, cookiePressed, deltaTime, cps):

        # Remove Unrenderd Particles

        for i in range(len(self.particles)):
            try:
                self.particleRect[i].topleft = (self.particleRect[i].x, self.particleRect[i].y + 10)

                if self.particleRect[i].y > pg.display.get_surface().get_height() + 20:
                    self.particles.pop(i)
                    self.particleRect.pop(i)
                    self.angles.pop(i)
            except Exception:
                pass

        # Add Particles on Click

        if cookiePressed and not self.pressed:
            self.particles.append(pg.image.load(resource_path("textures/particle.png")))
            self.particles[len(self.particles) - 1] = pg.transform.scale(self.particles[len(self.particles) - 1], (32,
                                                                                                                   32))
            self.particles[len(self.particles) - 1].convert()

            self.particleRect.append(self.particles[len(self.particles) - 1].get_rect())
            self.particleRect[len(self.particles) - 1].center = (randint(0, pg.display.get_surface().get_width()), 0)

            self.angles.append(randint(0, 360))

            self.pressed = True
        elif not cookiePressed:
            self.pressed = False

        # Add Particle from Cps

        if cps != 0:
            if self.spawnTime <= 0:
                self.particles.append(pg.image.load(resource_path("textures/particle.png")))
                self.particles[len(self.particles) - 1] = pg.transform.scale(self.particles[len(self.particles) - 1], (32,
                                                                                                                       32))
                self.particles[len(self.particles) - 1].convert()

                self.particleRect.append(self.particles[len(self.particles) - 1].get_rect())
                self.particleRect[len(self.particles) - 1].center = (randint(0, pg.display.get_surface().get_width()), 0)

                self.angles.append(randint(0, 360))

                for i in range(len(self.spawnIntervals)):
                    if cps <= self.cpsRanges[i]:
                        self.spawnTime = self.spawnIntervals[i]
                        break
            else:
                self.spawnTime -= deltaTime

    def render(self, deltaTime):
        for i in range(len(self.particles)):

            # Calculate Transparency

            transparentImage = self.particles[i].copy()
            transparentImage.convert()

            alpha = int(self.particleRect[i].y / pg.display.get_surface().get_height() * 255) * -1 + 255
            transparentImage.set_alpha(alpha)

            # Rotate Image

            rotatedImage = pg.transform.rotate(transparentImage, self.angles[i])
            rotatedRect = rotatedImage.get_rect(center=self.particles[i].get_rect(
                center=self.particleRect[i].center).center)

            if self.angles[i] + deltaTime * 20 >= 360:
                self.angles[i] = self.angles[i] + deltaTime * 20 - 360
            else:
                self.angles[i] += deltaTime * 20

            # Render Image

            self.screen.blit(rotatedImage, rotatedRect)
