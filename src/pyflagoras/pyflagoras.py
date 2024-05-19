import math
import re
from .image_processor import extract_colours
from .flag_info import flag_attr, format_rgb
from .utils import rgb_hex
from .similarity_algorithms import _low_cost, _pythagoras
from pathlib import Path

class Pyflagoras:
    def __init__(self, image, flag, output):
        self.image = image
        self.flag = flag
        self.output = output

    def parse_similarity(flag_colours: list[tuple], image_colours: list[tuple]) -> list[tuple]:
        """
        Generates a similarity rank for each of the image's colours compared to the flag's colours.

        Arguments:
        flag_colours (list[tuple]): The colours of the flag to use, formatted as a list of tuples in the format (r, g, b) -> the list returned by flag_info's format_rgb()
        image_colours (list[tuple]): The colours obtained from the image, formatted as a list of tuples in the format (r, g, b) -> the list returned by image_processor's extract_colours()
        """
        all_pairings = []
        for flag_colour in flag_colours:
            flag_colour_pairings = []
            for image_colour in image_colours:
                pair = _low_cost(flag_colour, image_colour)
                flag_colour_pairings.append(pair)
            all_pairings.append(flag_colour_pairings)
        return all_pairings

    def assign_rgb(rgb_similarity: list[list[tuple[tuple]]]) -> dict:
        """
        Assigns each value in rgb1 the closest colour to it out of rgb2 based on the results of the calc_colour_distance

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
            optimum_pairs[(rgb_hex(colour_pairing[0]))] = rgb_hex(curr_pair)
        return optimum_pairs

    def replace_colours(flag_svg: str, optimum_pairs: dict) -> str:
        """
        Replaces the hex codes of the colours within the original flag's SVG with the most similar colour from the image.

        Arguments:
        flag_svg (str): The svg of the flag (from flags/.*.json)
        optimum_pairs (dict): A dictionary where the key is the hex code of a flag's colour, and the value is the hex code of the similar colour.
        """
        for flag_colour in optimum_pairs.keys():
            flag_svg = re.sub(flag_colour, optimum_pairs[flag_colour], flag_svg, flags=re.IGNORECASE) # There's inconsistency in the source json files as to whether the hex codes are in uppercase or lowercase.
        return flag_svg
    
    def run(self):
        image_colours = extract_colours(self.image)
        flag_attributes = flag_attr(self.flag)
        format_r = format_rgb(flag_attributes["colors"])
        generate_similarity = Pyflagoras.parse_similarity(format_r, image_colours)
        assign_similar_colours = Pyflagoras.assign_rgb(generate_similarity)
        substituted = Pyflagoras.replace_colours(flag_attributes["svg"], assign_similar_colours)
        self.output = ((self.output)
        .replace("{n}", Path(self.image).stem)
        .replace("{N}", Path(self.image).name)
        .replace("{f}", flag_attributes['name'])
        .replace("{F}", flag_attributes['id'])
        .replace('"', "")
        )
        print(self.output)
        with open(f"{self.output}.svg", "w", encoding="utf-8") as file:
            file.write(substituted)
        print(f"🏳️‍🌈 Generated {flag_attributes['name']} ({self.flag}) flag from {Path(self.image).name} as {self.output}.svg!")


