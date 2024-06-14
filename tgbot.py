import os

import telegram

from environs import Env
from scripts import download_comic_xkcd, delete_comic


def send_comic(bot, chat_id, path_to_file):
    with open(path_to_file, "rb") as file:
        document = file.read()
    bot.send_document(chat_id=chat_id,
                      document=document)


def main():
    env = Env()
    env.read_env()
    bot = telegram.Bot(token=env.str("TG_BOT_TOKEN"))
    tg_chat_id = env.str("TG_CHAT_ID")
    try:
        filename = download_comic_xkcd()
        send_comic(bot, tg_chat_id, filename)
    finally:
        delete_comic(filename)


if __name__ == "__main__":
    main()
