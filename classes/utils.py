import pygame as pg
from decimal import Decimal
import sys
import os

# Modified Version of Numerize Package


def round_num(n, decimals):
    return n.to_integral() if n == n.to_integral() else round(n.normalize(), decimals)


def drop_zero(n):
    n = str(n)
    return n.rstrip('0').rstrip('.') if '.' in n else n


def numberize(n, decimals=2, formating=None):
    if formating is None:
        formating = ["k", "m", "b", "t", "q", "Q", "s", "S", "o", "n", "d", "ud", "dd", "td", "qd", "Qd", "sd",
                     "Sd", "od", "nd", "v", "uv", "dv", "tv", "qv", "Qv", "sv", "Sv", "ov", "nv", "T", "uT", "dT",
                     "googol"]

    is_negative_string = ""
    if n < 0:
        is_negative_string = "-"
    n = abs(Decimal(n))

    if n < 1000:
        return is_negative_string + str(drop_zero(round_num(n, decimals)))

    for i in range(0, len(formating)):
        if 10 ** ((i + 1) * 3) <= n < 10 ** ((i + 2) * 3):
            return is_negative_string + str(drop_zero(round_num(n / (10 ** ((i + 1) * 3)), decimals))) + formating[i]

    if 10 ** (len(formating) * 3) <= n:
        return is_negative_string + "Infinity"

    return is_negative_string + str(n)


def resource_path(relative_path):

    # Credit: Max(https://stackoverflow.com/users/1889973/max)

    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath("..")

    return os.path.join(base_path, relative_path)


def draw_rect_alpha(surface, color, rect):

    # Draw Transparent Rectangle

    shape_surf = pg.Surface(pg.Rect(rect).size, pg.SRCALPHA)
    pg.draw.rect(shape_surf, color, shape_surf.get_rect())
    surface.blit(shape_surf, rect)


def step(pos, end, stepSize):

    # Step from the Current Position to End Position for Animations

    if pos < end:
        if stepSize < end - pos:
            return pos + stepSize
        else:
            return pos + (end - pos)
    else:
        pos = 1 - pos
        end = 1 - end

        if stepSize < end - pos:
            return 1 - (pos + stepSize)
        else:
            return 1 - (pos + (end - pos))
