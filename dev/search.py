"""
Fetch the latest pride flags from the pride.dev repository
"""

import requests
import re

def index_flags():
    """Fetches the latest index of pride flags from the pride.dev repository"""
    REPO = "https://api.github.com/repos/joehart/pride-flag-api/contents/data/flags"
    content = (requests.get(REPO).json())
    with open("dev/flag_list.txt", "w", encoding="utf-8") as file:
        for i in range(len(content)):
            file_name = (content[i]["name"])
            if file_name not in ["svg", "index.js"]:            
                file.write(file_name[:-3]+"\n")

def save_flag(flag):
    """Takes a flag and writes its API data to `flag_name`.json under src/flags"""
    API_ENDPOINT = "https://pride.dev/api/flags/"
    API_ENDPOINT="localhost:3000/api/flags/"
    response = requests.get(API_ENDPOINT + flag)
    if response.status_code == 200:
        with open("src/flags/"+flag+".json", "w", encoding="utf-8") as file:
            file.write(response.text)
            print("saving")
            return 0
    return 1

save_flag("intersexInclusive_2021")