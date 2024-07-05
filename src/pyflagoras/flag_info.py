import json
import os 
import logging
from importlib.resources import files

def flag_attr(flag_alias: str) -> str:
    flag_alias = flag_alias.lower()
    all_flags = json.loads(files("pyflagoras").joinpath("flag_aliases.json").read_text(encoding="utf-8"))
    if flag_alias not in all_flags:
        raise Exception(f"The alias '{flag_alias}' is not associated with a flag.")
    else:
        flag_name = all_flags[flag_alias]
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
        
