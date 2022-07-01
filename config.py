import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "16715400"))
    API_HASH = os.environ.get("API_HASH", "2de611a73f73b8da8b0bcee9f855c815")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5417392757:AAFt3O1iesTxa44Vi5xR7x9Qow_HjQfF1nI")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOI0Bu2WVe4sdTHIdQFwKICF8WqUKH6OdvpMs83T4L04tOzZbGjcedwEiQr8VnqbME7S5cofSuwPaMdWEneM8q20a4YHBwU4943tnpWpLsrsSXGGju11tvafYqNW23hMmZh8-OZ-ZAMYbChBlkrFfs1ZNTYwM318JnkWyBQxP11Kp0bpDjKVTyVUHPR73RquYz1fuBFBEJGKQcdhxCboIhzNH8v9suHR2Nrypt97tTsBe_P3dP31k9tNUanN_BNnENH8DqnSDtmNrlL4HTmtFfbUpXpjHidta98dbX4u_ak1yk5vF3WjFrYSvG1a3l-MYL_oivWvhm_upqTr22gTEaFC5aOg=")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "@Wo_69bot")
    SUPPORT = os.environ.get("SUPPORT", "ygabutkan")
    CHANNEL = os.environ.get("CHANNEL", "ygabutkan")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
