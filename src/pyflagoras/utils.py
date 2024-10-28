"""
Assorted utilities.
"""
import re
import json
import logging
from importlib.resources import files
from PIL import ImageColor 

def rgb_hex(rgb: tuple) -> str: 
    return "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])

def hex_rgb(hexa: str) -> tuple:
    """Convert a hex code to RGB. This assumes that the hex code begins with a '#'."""
    convert = ImageColor.getcolor(hexa, 'RGB')
    return convert


def svg_format(svg: str) -> str:
    """
    Standardises .svgs by: 
        - Making all hex codes six digits long
        - Adding #000000 where a fill is not specified
        - Swapping colour words (e.g purple, blue) with actual hex codes 
    """
    logging.info(f"Custom .svg file detected, standardising .svg")

    new_svg = svg
    def _convert_lengths(shortcode):
        logging.info(f"Short hex codes detected.")
        return rgb_hex(hex_rgb(shortcode.group(0)))

    def _specify_fill(fill_element):
        if "fill" in fill_element.group(0):
            return fill_element.group(0)
        logging.info(f"Missing fill attribute detected.")
        return fill_element.group(0)[:-1] + ' fill=\"#000000\">'

    # Hex code length
    new_svg = re.sub("#([0-9a-fA-F]){3}\b", _convert_lengths, new_svg, flags=re.IGNORECASE)
    
    # Unspecified fills
    new_svg = re.sub(
        r"<\s*(rect|path|circle|ellipse|line|polyline|polygon|g|defs|svg)(\s+[^>]*?)?\s*\/?>",
        _specify_fill,
        new_svg)
    
    # Colour keywords
    colours = json.loads(files("pyflagoras.data").joinpath("colour_aliases.json").read_text(encoding="utf-8"))
    for colour_name in colours.keys():
        if '"' + colour_name + '"'  in new_svg or "'" + colour_name + "'" in new_svg:
            new_svg.replace(colour_name, colours[colour_name])
    return new_svg

