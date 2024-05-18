import json
import os 

def flag_attr(flag_name: str) -> str:
    if not (os.path.exists("src/pyflagoras/flags/"+flag_name+".json")):
        raise Exception(f"File {flag_name}.json was not found.")
    with open("src/pyflagoras/flags/"+flag_name+".json", "r", encoding="utf-8") as json_file:
        data = json.load(json_file)
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
        
