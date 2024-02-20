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
    tag_found = False
    for tag in reversed(tags):
        if tag in genres:
            main_tag = tag
            tag_found = True
            break

    # If none of the genres matched, see if any of the secondary genre
    # strings contain a primary genre
    if not tag_found:
        for tag in reversed(tags):
            for g in genres:
                if g in tag:
                    main_tag = g
                    tag_found = True
        
    # If there is still no match: set the genre to an empty string
    if not tag_found:
        main_tag = ""

    return main_tag

def shrink_genius_tag(tag: dict) -> str:
    return tag["name"].lower().replace("&", "-")