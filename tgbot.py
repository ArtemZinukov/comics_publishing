import os

import telegram

from environs import Env
from scripts import download_comic_xkcd


def send_and_delete_comic(bot, chat_id, path_to_file):
    try:
        with open(path_to_file, "rb") as file:
            document = file.read()
        bot.send_document(chat_id=chat_id,
                          document=document)
    finally:
        os.remove(path_to_file)


def main():
    env = Env()
    env.read_env()
    bot = telegram.Bot(token=env.str("TG_BOT_TOKEN"))
    tg_chat_id = env.str("TG_CHAT_ID")
    filename = download_comic_xkcd()
    send_and_delete_comic(bot, tg_chat_id, filename)


if __name__ == "__main__":
    main()
