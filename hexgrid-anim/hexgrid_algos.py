"""Utility functions to construct and manipulate hexagonal grids.

Largely inspired by: https://www.redblobgames.com/grids/hexagons/
"""

import numpy as np


def pixel_to_pointy_hex(pixel, hexbin_size):
    """Gets hexbin coordinates from pixel position."""

    x, y = pixel
    q = (np.sqrt(3) / 3 * x - 1.0 / 3 * y) / hexbin_size
    r = (2.0 / 3 * y) / hexbin_size
    return axial_to_evenr(axial_round((q, r)))

def pixel_to_flat_hex(pixel, hexbin_size):
    """Gets hexbin coordinates from pixel position."""

    x, y = pixel
    q = (2./3 * x) / hexbin_size
    r = (-1./3 * x + np.sqrt(3) / 3 * y) / hexbin_size

    return axial_to_oddr(axial_round((q, r)))


def axial_to_evenr(hex_axial):
    """Converts axial to even-r coordinates."""

    q, r = hex_axial
    q = int(q)
    r = int(r)
    col = q + (r + (r & 1)) / 2
    row = r
    return (col, row)


def axial_to_oddr(hex_axial):
    """Converts axial to even-r coordinates."""

    q, r = hex_axial
    q = int(q)
    r = int(r)
    col = q + (r - (r & 1)) / 2
    row = r
    return (col, row)

def axial_to_oddq(hex_axial):
    """Converts axial to even-r coordinates."""

    q, r = hex_axial
    q = int(q)
    r = int(r)
    col = q
    row = r + (q - (q & 1)) / 2
    return (col, row)


def cube_round(frac):
    """Rounds the cube coordinates."""

    frac_q, frac_r, frac_s = frac
    q = np.round(frac_q)
    r = np.round(frac_r)
    s = np.round(frac_s)

    q_diff = abs(q - frac_q)
    r_diff = abs(r - frac_r)
    s_diff = abs(s - frac_s)

    if q_diff > r_diff and q_diff > s_diff:
        q = -r - s
    elif r_diff > s_diff:
        r = -q - s
    else:
        s = -q - r

    return (q, r, s)


def cube_to_axial(hex_cube):
    """Converts cube to axial coordinates."""

    q, r, _ = hex_cube
    return (q, r)


def axial_to_cube(hex_axial):
    """Converts axial to cube coordinates."""

    q, r = hex_axial
    s = -q - r
    return (q, r, s)


def axial_round(hex_axial):
    """Rounds the axial coordinates."""

    return cube_to_axial(cube_round(axial_to_cube(hex_axial)))


def evenr_offset_to_pixel(hex, size):
    """Gets the pixel position from the even-r offset coordinates."""

    col, row = hex
    x = size * np.sqrt(3) * (col - 0.5 * (row & 1))
    y = size * 3 / 2 * row
    return (x, y)
