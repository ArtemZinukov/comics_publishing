import glob
import os
import random
import requests


def download_comic_xkcd():
    total_comics = 2944
    random_comics = random.randint(1, total_comics)
    url = f"https://xkcd.com/{random_comics}/info.0.json"
    response = requests.get(url)
    response.raise_for_status()
    comic_info = response.json()
    url_image = comic_info["img"]
    comic_number = comic_info["num"]
    filename = os.path.join("Images", f"{comic_number}.png")
    return write_to_file(url_image, filename)


def write_to_file(url, filename, params=None):
    response = requests.get(url, params=params)
    response.raise_for_status()
    with open(filename, "wb") as file:
        file.write(response.content)
    return filename
