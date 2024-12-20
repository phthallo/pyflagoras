import numpy as np
from PIL import Image, ImageDraw
import re
import logging
import os

from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF
from pathlib import Path
import fitz


from .image_processor import extract_colours, highlight_colours
from .flag_info import flag_attr, format_rgb
from .utils import rgb_hex, hex_rgb
from .similarity_algorithms import _low_cost, _pythagoras, _cielab


class Pyflagoras:
    def __init__(self, image, flag, output, algorithm, svg, verbose, highlight):
        self.image = image
        self.flag = flag
        self.output = output
        self.algorithm = algorithm
        self.svg = svg
        self.verbose = verbose
        self.highlight = highlight

    def parse_similarity(flag_colours: list[tuple], image_colours: list[tuple], algorithm: str) -> list[tuple]:
        """
        Generates a similarity rank for each of the image's colours compared to the flag's colours.

        Arguments:
        flag_colours (list[tuple]): The colours of the flag to use, formatted as a list of tuples in the format (r, g, b) -> the list returned by flag_info's format_rgb()
        image_colours (list[tuple]): The colours obtained from the image, formatted as a list of tuples in the format (r, g, b) -> the list returned by image_processor's extract_colours()
        """
        all_pairings = []
        for flag_colour in set(flag_colours):
            flag_colour_pairings = []
            for image_colour in image_colours:
                pair = globals()["_" + algorithm](flag_colour, image_colour)
                flag_colour_pairings.append(pair)
            logging.info(f"Generated {len(flag_colour_pairings)} pairings for {flag_colour}")
            all_pairings.append(flag_colour_pairings)

        return all_pairings

    def assign_rgb(rgb_similarity: list[list[tuple[tuple]]]) -> dict:
        """
        Assigns each value in rgb1 the closest colour to it out of rgb2 based on the results of the parse_similarity

        Slightly cursed things going on in the type hints, sorry! If it makes more sense: 
        A list of:
            m amount of lists, where m is the number of colours in the flag
            n amount of ((flag_rgb), (image_rgb), similarity) tuples within each list, where n is equal to the number of colours in the image.
        """
        optimum_pairs = {}
        for colour_similarity in rgb_similarity:
            curr_min = 1234567890 # We want the minimum difference, so a really big number is here. Yes, the maximum possible integer is 1234567890 (sarcasm)
            curr_pair = ()
            for colour_pairing in colour_similarity:
                if colour_pairing[2] < curr_min:
                    curr_min = colour_pairing[2]
                    curr_pair = colour_pairing[1]
            logging.info(f"Found pair {rgb_hex(colour_pairing[0]), rgb_hex(curr_pair)} with a difference of {curr_min:.2f}")
            optimum_pairs[(rgb_hex(colour_pairing[0]))] = rgb_hex(curr_pair)
        return optimum_pairs

    def replace_colours(flag_svg: str, optimum_pairs: dict) -> str:
        """
        Replaces the hex codes of the colours within the original flag's .svg with the most similar colour from the image.

        Arguments:
        flag_svg (str): The svg of the flag (from flags/.*.json)
        optimum_pairs (dict): A dictionary where the key is the hex code of a flag's colour, and the value is the hex code of the similar colour.
        """
        for flag_colour in optimum_pairs.keys():
            flag_svg = re.sub(flag_colour, optimum_pairs[flag_colour], flag_svg, flags=re.IGNORECASE) # There's inconsistency in the source json files as to whether the hex codes are in uppercase or lowercase.
            logging.info(f"{flag_colour} ({hex_rgb(flag_colour)}) replaced with {optimum_pairs[flag_colour]} ({hex_rgb(optimum_pairs[flag_colour])})")
        return flag_svg
    
    def run(self):
        image_colours = extract_colours(self.image, [self.verbose, self.highlight])
        flag_attributes = flag_attr(self.flag)
        svg_colours = re.findall(r"#(?:[0-9a-fA-F]{3}){1,2}", flag_attributes["svg"]) # This should return a list of hex codes found in the svg data
        logging.info(f"{len(svg_colours)} .svg hex codes found: {svg_colours}")
        format_r = [hex_rgb(i) for i in svg_colours] # convert each colour into its RGB tuple so similarity can be compared.
        if any([self.verbose, self.highlight]):
            generate_similarity = Pyflagoras.parse_similarity(format_r, image_colours[0], self.algorithm)
        else:
            generate_similarity = Pyflagoras.parse_similarity(format_r, image_colours, self.algorithm)
        assign_similar_colours = Pyflagoras.assign_rgb(generate_similarity)
        if any([self.verbose, self.highlight]):
            image_copy = Image.open(self.image).convert("RGB", palette="IMAGE.ADAPTIVE").copy()
            image_draw = ImageDraw.Draw(image_copy, "RGBA")
            for colour in assign_similar_colours:
                col = (hex_rgb(assign_similar_colours[colour]))
                colour_coords_y, colour_coords_x = np.where(np.all(image_colours[1]==col,axis=2))
                if self.highlight:
                    highlight_colours(image_copy, image_draw, Path(self.image).stem, flag_attributes['id'], [colour_coords_x[0], colour_coords_y[0]])
                if self.verbose:    
                    logging.info(f"Similar colour {rgb_hex(col)} ({col}) can be found at [{colour_coords_x[0]}, {colour_coords_y[0]}] on input image.")
                
        substituted = Pyflagoras.replace_colours(flag_attributes["svg"], assign_similar_colours)
        self.output = ((self.output)
        .replace("{n}", Path(self.image).stem)
        .replace("{N}", Path(self.image).name)
        .replace("{f}", flag_attributes['name'])
        .replace("{F}", flag_attributes['id'])
        .replace('"', "")
        )
        with open(f"{self.output}.svg", "w", encoding="utf-8") as file:
            file.write(substituted)

        drawing = svg2rlg(f"{self.output}.svg")
        renderPDF.drawToFile(drawing, f"{self.output}.pdf")
        png = (fitz.open(f"{self.output}.pdf")[0]).get_pixmap()
        png.save(f"{self.output}.png")
        os.remove(f"{self.output}.pdf")
        if not self.svg:
            os.remove(f"{self.output}.svg")

        print(f"🏳️‍🌈  Generated {flag_attributes['name']} ({flag_attributes['id']}) flag from {Path(self.image).name} as {self.output}.png!")


