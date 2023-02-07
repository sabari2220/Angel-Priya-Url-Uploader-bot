#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Thank you @Sabari023

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger =logging.getLogger(__name__)

import os

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)


if __name__ == "__main__" :
    # create download directory, if not exist
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)
    plugins = dict(
        root="plugins"
    )
    app = pyrogram.Client(
        "BewafaAngelPriya",
        bot_token="5718780980:AAHqbMrZSBJYuhkpBfCCa8WCnqgphEBowRQ",
        api_id="29161994",
        api_hash="6de0c3c108577f72d5a50097108e9486",
        plugins=plugins
    )
    Config.AUTH_USERS.add(1513467017)
    app.run()
