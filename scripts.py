import glob
import os
import random
import requests


def download_comics_xkcd():
    total_comics = 2944
    random_comics = random.randint(1, total_comics)
    url = f"https://xkcd.com/{random_comics}/info.0.json"
    response = requests.get(url)
    response.raise_for_status()
    response_json = response.json()
    url_image = response_json["img"]
    comic_number = response_json["num"]
    filename = f"Images/{comic_number}.png"
    write_to_file(url_image, filename)


def write_to_file(url, filename, params=None):
    response = requests.get(url, params=params)
    response.raise_for_status()
    with open(filename, "wb") as file:
        file.write(response.content)


def remove_file():
    document_dir = "./Images"
    files = glob.glob(os.path.join(document_dir, '*'))
    for file in files:
        os.remove(file)

