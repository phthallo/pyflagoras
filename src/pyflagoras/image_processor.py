from PIL import Image
import os
import numpy as np
import logging
def extract_colours(img: str, verbose: bool) -> list[tuple]:
    """
    Returns the RGB codes of the colours in the ijmage
    
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

