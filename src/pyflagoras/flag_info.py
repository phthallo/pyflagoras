import json
import os 
import logging
from importlib.resources import files
from pathlib import Path
from .utils import svg_format

def flag_attr(flag_alias: str) -> str:
    """
    Returns information about the flag and whether it was custom.
    
    Arguments:
    flag_alias (str): Either the path to the .svg file or the alias of an included pride flag.

    Returns:
    str: flag data in json
    """
    flag_alias = flag_alias.lower()
    all_flags = json.loads(files("pyflagoras.data").joinpath("flag_aliases.json").read_text(encoding="utf-8"))
    if os.path.exists(flag_alias): # Check if custom .svg is being loaded.
        flag_name = Path(flag_alias).stem # Use .svg file name as final name.
        with open(flag_alias, "r", encoding="utf-8") as file: 
            data = svg_format(file.read()) # Run standardiser on custom svgs
        location = json.dumps({
            "name": flag_name, # Custom .svgs don't have this kind of metadata associated with them so... oops
            "id": flag_name, # "
            "svg": data
        })
    elif flag_alias in all_flags: # Check if existing .svg is being loaded. 
        flag_name = all_flags[flag_alias]
        location = files("pyflagoras.flags").joinpath(flag_name+".json").read_text(encoding="utf-8")
    else:
        raise Exception(f"The alias '{flag_alias}' is not associated with a flag.")
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
        
