"""
Assorted utilities.
"""
import math
import logging
from PIL import ImageColor 

def rgb_hex(rgb: tuple) -> str: 
    return "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])

def hex_rgb(hexa: str) -> tuple:
    """Convert a hex code to RGB. This assumes that the hex code begins with a '#'."""
    convert = ImageColor.getcolor(hexa, 'RGB')
    logging.info(f"Converting hex {hexa} to RGB tuple {convert}")
    return convert
