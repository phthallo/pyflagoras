"""
Assorted utilities.
"""
import math

def rgb_hex(rgb: tuple) -> str: 
    return "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])
