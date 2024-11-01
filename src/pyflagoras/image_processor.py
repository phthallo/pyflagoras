from PIL import Image, ImageDraw
import os
import numpy as np
import logging

def extract_colours(img: str, verbose: bool) -> list[tuple]:
    """
    Returns the RGB codes of the colours in the image
    
    Arguments:
    img (str): Path of the image to extract colours from. 
    """
    if not os.path.exists(img):
        raise Exception(f"The image '{img}' does not exist.")
    
    palette = Image.open(img).convert("RGB", palette="IMAGE.ADAPTIVE")
    max_colours = palette.size[0]*palette.size[1]
    colours = palette.getcolors(maxcolors=max_colours) 
    if verbose:
        image = np.array(Image.open(img).convert("RGB", palette="IMAGE.ADAPTIVE"))
        return ([i[1] for i in colours], image)
    return ([i[1] for i in colours])

def highlight_colours(img: Image, draw: ImageDraw, img_name: str, flag_name: str, coords: list[int]) -> bool:
    """
    Saves an image where the identified 'similar colours' are highlighted with a circle. 
    
    Arguments:
    draw (str): Converted image to draw on. 
    file_name (str): File name of the original image.
    coords (list[int]): Coordinates of the first detected location of that colour.
    radius (int): Radius of the circle used to highlight
    """
    radius = 10
    point_list = [(coords[0]-radius, coords[1]-radius), (coords[0]+radius, coords[1]+radius)]
    draw.ellipse(point_list, outline=(235, 64, 52), width=2)
    logging.info(f"Highlighting coordinates {[int(i) for i in coords]} on {img_name}_{flag_name}_highlight_colour.png")
    img.save(f"{img_name}_{flag_name}_highlight_colour.png", "PNG")
    return True
            
