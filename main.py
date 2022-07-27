# Import

import pygame as pg
import itertools
import sys

from classes.utils import resource_path
from classes.cookie import Cookie
from classes.goldenCookie import GoldenCookie
from classes.cookieParticle import CookieParticle
from classes.cookieDisplay import cookieDisplay
from classes.cookieHandler import cookieHandler

# Setup Window

pg.init()

pg.display.set_caption(resource_path("Cookie Clicker"))
pg.display.set_icon(pg.image.load(resource_path("textures/icon/icon.png")))

screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
running = True

# Setup Variables

FPS = 60
Clock = pg.time.Clock()

quitTimer = 3

# Setup Classes

cookie = Cookie(screen)
golden = GoldenCookie(screen)
particle = CookieParticle(screen)
display = cookieDisplay(screen)
handler = cookieHandler()

# Textures

bg = pg.image.load(resource_path("textures/bg.png"))
bg = pg.transform.scale(bg, (64, 64))
bg.convert()

vignette = pg.image.load(resource_path("textures/vignette.png"))
vignette = pg.transform.scale(vignette, (screen.get_width(), screen.get_height()))
vignette.convert_alpha()

goldenVignette = pg.image.load(resource_path("textures/goldenCookies/goldenVignette.png"))
goldenVignette = pg.transform.scale(goldenVignette, (screen.get_width(), screen.get_height()))
goldenVignette.convert_alpha()

fontSmall = pg.font.Font(resource_path("textures/font/retro.ttf"), 16)

# Game Loop


def render():

    # Fill Screen for any unfilled Areas

    screen.fill((110, 100, 255))

    # Cover Background in Texture

    for x, y in itertools.product(range(0, screen.get_width() + 1, bg.get_rect().width),
                                  range(0, screen.get_height() + 1, bg.get_rect().height)):
        screen.blit(bg, (x, y))

    if not golden.active:
        screen.blit(vignette, (0, 0))
    else:
        screen.blit(goldenVignette, (0, 0))

    # Render Classes

    particle.render(deltaTime)

    display.render()
    cookie.render()

    golden.render()

    # Render Quitting Animation

    if quitTimer <= 1:
        text = fontSmall.render("Quitting...", False, (255, 255, 255))
        textRect = text.get_rect()
        textRect.topleft = (5, 5)
        screen.blit(text, textRect)
    elif quitTimer <= 2:
        text = fontSmall.render("Quitting..", False, (255, 255, 255))
        textRect = text.get_rect()
        textRect.topleft = (5, 5)
        screen.blit(text, textRect)
    elif quitTimer < 3:
        text = fontSmall.render("Quitting.", False, (255, 255, 255))
        textRect = text.get_rect()
        textRect.topleft = (5, 5)
        screen.blit(text, textRect)


def update():

    # Update Classes

    particle.update(cookie.checkCookiePressed(pg.mouse.get_pos(), pg.mouse.get_pressed()[0]), deltaTime, handler.cps)
    golden.update(deltaTime, pg.mouse.get_pos(), pg.mouse.get_pressed()[0])
    handler.update(0, 10, cookie.checkCookiePressed(pg.mouse.get_pos(), pg.mouse.get_pressed()[0])
                   )
    cookie.update(pg.mouse.get_pos(), pg.mouse.get_pressed()[0])
    display.update(handler.cookies, handler.cps)


getTicksLastFrame = pg.time.get_ticks()
handler.updateCookies()

while running:

    # Calculate DeltaTime

    t = pg.time.get_ticks()
    deltaTime = (t - getTicksLastFrame) / 1000.0
    getTicksLastFrame = t

    # Events

    for event in pg.event.get():
        if event.type == pg.QUIT:
            handler.quit()
            sys.exit()

    if pg.key.get_pressed()[pg.K_ESCAPE] == 1:
        quitTimer -= deltaTime

        if quitTimer <= 3:  # Change to 0 when building
            running = False
    else:
        quitTimer = 3

    # Update Game Elements

    update()

    # Render Screen

    render()

    # End Frame

    pg.display.flip()
    Clock.tick(FPS)

# Shut down Game

handler.quit()
pg.quit()
