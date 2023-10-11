"""
Animation of an infinite nested hexgrid.

Run with:
    manim -pql hexgrid.py CreateHexGrid # Low resolution
    manim -p hexgrid.py CreateHexGrid # High resolution
"""

import numpy as np
from hexgrid_algos import *
from manim import *

config.pixel_height = 360 #720 #1080
config.pixel_width = 640 #1280 #1920


def get_hexgrid(hex, shape=(14,15), mode='flat'):
    """Returns a regular hexagonal grid."""

    nq, nr = shape

    hex = hex.copy()

    hexs = []
    for q in range(nq):
        for r in range(nr):

            if mode == 'flat':
                x = 1.5 * r
                y = np.sqrt(3) * q + (r % 2) * np.sqrt(3) / 2
            elif mode == 'pointy':
                x = np.sqrt(3) * r + (q % 2) * np.sqrt(3) / 2
                y = 1.5 * q

            hexs.append(hex.copy().shift([x, y, 0]))

    hexgrid = VGroup(*hexs)
    hexgrid.shift(- hexgrid.get_center())

    return hexgrid.copy()


def get_nested_hexgrid(hex, shape=(14,15), ratio=10, mode='flat'):
    """Returns a nested hexagonal grids into an larger hexagon."""

    nq, nr = shape

    hex = hex.copy()

    if mode == 'flat':
        x_max = 1.5 * (nr-1)
        y_max = np.sqrt(3) * (nq-1) + ((nr - 1) % 2) * np.sqrt(3) / 2
    elif mode == 'pointy':
        hex.rotate(3*np.pi/2)
        x_max = np.sqrt(3) * (nr-1) + ((nq - 1) % 2) * np.sqrt(3) / 2
        y_max = 1.5 * (nq-1)

    hexs = []
    for q in range(nq):
        for r in range(nr):

            if mode == 'flat':
                x = 1.5 * r
                y = np.sqrt(3) * q + (r % 2) * np.sqrt(3) / 2
                pixel_to_hex = pixel_to_pointy_hex
            elif mode == 'pointy':
                x = np.sqrt(3) * r + (q % 2) * np.sqrt(3) / 2
                y = 1.5 * q
                pixel_to_hex = pixel_to_flat_hex

            # Only draw hexagons that are located inside a virtual large hexagon
            if pixel_to_hex((x - x_max / 2, y - y_max / 2), ratio) == (0, 0):
                hexs.append(hex.copy().shift([x, y, 0]))

    hexgrid = VGroup(*hexs).scale(1/ratio)
    hexgrid.shift(- hexgrid.get_center())

    return hexgrid.copy()


class CreateHexGrid(Scene):
    """Regular hexagonal grid."""

    def construct(self):

        hex = RegularPolygon(6)
        hex.set_fill(BLACK, opacity=1)
        hex.set_stroke(color=YELLOW_D, width=1)

        hexgrid = get_hexgrid(hex, shape=(40,40), mode='flat')

        self.play(ScaleInPlace(hexgrid.scale(0.2), scale_factor=20).set_run_time(3))


class CreateInfiniteNestedHexGrid(Scene):
    """Infinite loop through nested hexagonal grids."""

    def construct(self):

        hex = RegularPolygon(6)
        hex.set_fill(BLACK, opacity=1)
        hex.set_stroke(color=YELLOW_D, width=4)

        hexgrid = get_nested_hexgrid(hex, shape=(14,15), ratio=10, mode='flat')
        hexgrid2 = get_nested_hexgrid(hex, shape=(15,14), ratio=10, mode='pointy')
        hexgrid3 = get_nested_hexgrid(hex, shape=(14,15), ratio=10, mode='flat')

        self.play(Animation(hexgrid.scale(10)).set_run_time(0.5))
        self.play(FadeIn(hexgrid2).set_run_time(2))

        self.play(
            ScaleInPlace(hexgrid, scale_factor=10).set_run_time(3),
            ScaleInPlace(hexgrid2, scale_factor=10).set_run_time(3),
        )

        self.play(FadeIn(hexgrid3, scale_factor=10).set_run_time(2))

        self.play(
            ScaleInPlace(hexgrid2, scale_factor=10).set_run_time(3),
            ScaleInPlace(hexgrid3, scale_factor=10).set_run_time(3),
        )