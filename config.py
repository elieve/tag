import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "16589591"))
    API_HASH = os.environ.get("API_HASH", "396d3b2b0f1cd575ab6a34fe65afd7cc")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5430925446:AAHKsxgxdetQSfzsfuFFhd6cGkXfOoPahAw")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOKsBu8BSPI6KRzcvI23DexjHqAr0lLzM7S6LQADPDbJDKjEU1PKp5WACABchmUKRkmXiRrHiQcnChXhkTS_fJoN4yY51cSDFtBuL-ZkP5zpI5m8yA6ZkqFE82c7gI6i1v4yBIfpQhMqRp1RNofjp7mFC8ON4mKmzNH_odHgbw-65VK9PY45iT5voxEL_jxleqlHomdRRCFJHB5u47pIHTgiYs7IMqORSFW2o92qsdvldapCIKmXgqnKaeHY-rMH5zhCMCQgrlPf8ceduWCscJrYKCj1NlK-ZmrVs3LtoEYohirCHMN5iSnGf0hwxJLUL1aaj6mQmqW8cqWfZ2Z6b9Bn2Uzg=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "thehouse6bot")
    SUPPORT = os.environ.get("SUPPORT", "ygabutkan")
    CHANNEL = os.environ.get("CHANNEL", "ygabutkan")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
