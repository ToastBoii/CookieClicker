# Import

import pygame as pg
import sys

from utils import resource_path
from classes.discordRPC import updateParameters, disconectRPC

# Base Game
from classes.cookie import Cookie
from classes.goldenCookie import GoldenCookie
from classes.goldenCookieFrame import GoldenCookieFrame
from classes.cookieParticle import CookieParticle
from classes.cookieDisplay import CookieDisplay
from classes.cookieHandler import CookieHandler

# Shop
from classes.shop import Shop

# Setup Window

pg.init()

pg.display.set_caption(resource_path("Cookie Clicker"))
pg.display.set_icon(pg.image.load(resource_path("textures/icon/icon.png")))

screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
running = True

# Setup Variables

FPS = 60
clock = pg.time.Clock()

quitTimer = 3

# Setup Classes

cookie = Cookie(screen)
golden = GoldenCookie(screen)
particle = CookieParticle(screen)
display = CookieDisplay(screen)
handler = CookieHandler()
frame = GoldenCookieFrame(screen)

shop = Shop(screen)

# Textures

fontSmall = pg.font.Font(resource_path("textures/font/retro.ttf"), 16)

framer = 1
# Game Loop


def render():
    # Fill Screen for any unfilled Areas

    screen.fill((110, 100, 255))

    # Cover Background in Texture

    for i in range(120):
        if i%2 == 0:
            color = (91, 110, 225)
        else:
            color = (99, 155, 255)

        pg.draw.rect(screen, color, pg.Rect(screen.get_width() / 120 * i, 0, screen.get_width() / 120, screen.get_height()))

    # Render Classes

    particle.render(deltaTime)

    display.render(handler.cookies, handler.tempCps)
    cookie.render()

    shop.render()

    frame.render(golden.active, golden.cookieEffect, golden.timer)
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
    mousePos = pg.mouse.get_pos()
    mousePressed = pg.mouse.get_pressed()[0]

    # Update Classes

    shop.update(deltaTime, mousePos, mousePressed, handler.cookies)
    if shop.debt != 0:
        handler.cookies -= shop.debt
        handler.cheatCookies -= shop.debt
        shop.debt = 0

    particle.update(cookie.checkCookiePressed(mousePos, mousePressed), deltaTime, handler.cps)
    golden.update(deltaTime, mousePos, mousePressed)
    handler.update(shop.cpsFromItems, 1, cookie.checkCookiePressed(mousePos, mousePressed), golden.active,
                   golden.cookieEffect)
    cookie.update(mousePos, mousePressed)

    updateParameters(handler.cookies, deltaTime)


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
            disconectRPC()
            handler.quit()
            pg.quit()
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
    clock.tick(FPS)
    framer += 1
    if framer % 50 == 0:
        print(clock.get_fps())

# Shut down Game

disconectRPC()
handler.quit()
pg.quit()
