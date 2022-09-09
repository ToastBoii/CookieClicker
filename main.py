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
from classes.cheatCode import CheatCode

# Side Menus
from classes.shop import Shop
from classes.settings import Settings

# Setup Window

pg.init()

pg.display.set_caption(resource_path("Cookie Clicker"))
pg.display.set_icon(pg.image.load(resource_path("textures/icon/icon.png")))

screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
running = True

# Setup Variables

FPS = 60
clock = pg.time.Clock()

# Setup Classes

cookie = Cookie(screen)
golden = GoldenCookie(screen)
particle = CookieParticle(screen)
display = CookieDisplay(screen)
handler = CookieHandler()
frame = GoldenCookieFrame(screen)

shop = Shop(screen)
setting = Settings(screen)

cheat = CheatCode()

# Textures

fontSmall = pg.font.Font(resource_path("textures/font/retro.ttf"), 16)

framer = 1


# Game Loop


def render():
    # Fill Screen for any unfilled Areas

    screen.fill((110, 100, 255))

    # Cover Background in Texture

    for i in range(120):
        if i % 2 == 0:
            color = (91, 110, 225)
        else:
            color = (99, 155, 255)

        pg.draw.rect(screen, color, pg.Rect(screen.get_width() / 120 * i, 0, screen.get_width() / 120,
                                            screen.get_height()))

    # Render Classes

    particle.render(deltaTime)

    display.render(handler.cookies, handler.tempCps)
    cookie.render(handler.cpc, deltaTime, cheat.active)

    shop.render()
    setting.render()

    frame.render(golden.active, golden.cookieEffect, golden.timer)
    golden.render()


def update():
    global running
    mousePos = pg.mouse.get_pos()
    mousePressed = pg.mouse.get_pressed()[0]

    # Update Classes

    setting.update(deltaTime, mousePos, mousePressed, handler.cookies, shop.boughtItems)
    if setting.load:
        handler.cookies = setting.loadedCookies
        handler.cheatCookies = setting.loadedCookies + handler.randOffset
        for i in range(len(shop.boughtItems)):
            shop.boughtItems[i] = setting.loadedBoughtItems[i]
        setting.load = False
    if setting.quit:
        running = False

    shop.update(deltaTime, mousePos, mousePressed, handler.cookies)
    if shop.debt != 0:
        handler.cookies -= shop.debt
        handler.cheatCookies -= shop.debt
        shop.debt = 0

    particle.update(cookie.checkCookiePressed(mousePos, mousePressed), deltaTime, handler.cps)
    golden.update(deltaTime, mousePos, mousePressed)

    if shop.cpsFromItems * 0.1 <= 1:
        handler.update(shop.cpsFromItems, 1, cookie.checkCookiePressed(mousePos, mousePressed),
                       golden.active, golden.cookieEffect)
    else:
        handler.update(shop.cpsFromItems, shop.cpsFromItems * 0.1, cookie.checkCookiePressed(mousePos, mousePressed),
                       golden.active, golden.cookieEffect)
    cookie.update(mousePos, mousePressed, handler.cpc)

    updateParameters(handler.cookies, deltaTime)


getTicksLastFrame = pg.time.get_ticks()
handler.updateCookies()

while running:

    # Calculate DeltaTime

    t = pg.time.get_ticks()
    deltaTime = (t - getTicksLastFrame) / 1000.0
    getTicksLastFrame = t

    # Events

    for e in pg.event.get():
        if e.type == pg.QUIT:
            disconectRPC()
            handler.quit()
            pg.quit()
            sys.exit()
        if e.type == pg.KEYDOWN:
            cheat.update(e.key)
        """if e.type == pg.MOUSEWHEEL:
            if not shop.opened:
                break
            shop.scrollOffset += e.y * 2000 * deltaTime"""

    if pg.key.get_pressed()[pg.K_ESCAPE] == 1:
        running = False

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
