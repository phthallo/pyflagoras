import json
import os 
import logging
from importlib.resources import files

def flag_attr(flag_name: str) -> str:
    if not (os.path.exists(os.path.join(os.path.dirname(__file__), "flags", flag_name+".json"))):
        raise Exception(f"The flag '{flag_name}' does not exist.")
    location = files("pyflagoras.flags").joinpath(flag_name+".json").read_text(encoding="utf-8")
    data = json.loads(location)
    logging.info(f"Loading attributes of flag '{flag_name}'")
    return data

def format_rgb(flag_colours: list[dict]) -> list[tuple]:
    """
    Formats the colours of the provided flag as a list of tuples.

    Arguments:
    flag_colours (list[dict]): The "colours" metadata (including name, hex, RGB codes etc) from a standard flag.json file.
    """
    return [ 
        (i["r"], i["g"], i["b"]) for i in flag_colours
        ] 
        
