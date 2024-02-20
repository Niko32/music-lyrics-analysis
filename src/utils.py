from typing import List
import tomllib
import os

ROOT = f"{os.path.dirname(os.path.abspath(__file__))}/.."

with open(f"{ROOT}/config.toml", "rb") as f:
    config = tomllib.load(f)

genres: List[str] = config["genres"]


def get_main_tag(tags: List[str]):
    """ Find the main tag from a given list of tags and a list of genres. """

    # Get the main tag
    for tag in reversed(tags):
        if tag in genres:
            return tag

    # If none of the genres matched, see if any of the secondary genre
    # strings contain a primary genre
    for tag in reversed(tags):
        for g in genres:
            if g in tag:
                return g
        
    # If there is still no match: set the genre to an empty string
    return None

def shrink_genius_tag(tag: dict) -> str:
    return tag["name"].lower().replace("&", "-")