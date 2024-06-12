import os

import telegram

from environs import Env
from scripts import download_comics_xkcd, remove_file


def send_messages(bot, chat_id):
    document_dir = os.path.join(os.getcwd(), "Images")
    for comics in os.listdir(document_dir):
        path_to_file = os.path.join(document_dir, comics)
        with open(path_to_file, "rb") as file:
            document = file.read()
        bot.send_document(chat_id=chat_id,
                          document=document)


def main():
    env = Env()
    env.read_env()
    bot = telegram.Bot(token=env.str("TG_BOT_TOKEN"))
    tg_chat_id = env.str("TG_CHAT_ID")
    download_comics_xkcd()
    send_messages(bot, tg_chat_id)
    remove_file()


if __name__ == "__main__":
    main()
