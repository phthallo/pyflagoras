from PIL import Image
import os
import numpy as np
import logging
def extract_colours(img: str) -> list[tuple]:
    """
    Returns the RGB codes of the colours in the ijmage
    
    Arguments:
    img (str): Path of the image to extract colours from. 
    """
    if not os.path.exists(img):
        raise Exception(f"The image '{img}' does not exist.")
    image = np.array(Image.open(img).convert("RGB", palette="IMAGE.ADAPTIVE"))
    palette = Image.open(img).convert("RGB", palette="IMAGE.ADAPTIVE")
    colours = palette.getcolors(maxcolors=1000000) # IMPORTANT: Figure out a feasible amount of colours based on the image size?
    return ([i[1] for i in colours],image)

