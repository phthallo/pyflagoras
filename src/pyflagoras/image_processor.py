from PIL import Image
import os
import logging
def extract_colours(img: str) -> list[tuple]:
    """
    Returns the RGB codes of the colours in the ijmage
    
    Arguments:
    img (str): Path of the image to extract colours from. 
    """
    if not os.path.exists(img):
        raise Exception(f"The image '{img}' does not exist.")
    image = Image.open(img).convert("RGB", palette="IMAGE.ADAPTIVE")
    colours = image.getcolors(maxcolors=1000000) # IMPORTANT: Figure out a feasible amount of colours based on the image size?
    logging.info(f"{len(colours)} colours extracted from image.")
    return ([i[1] for i in colours])

