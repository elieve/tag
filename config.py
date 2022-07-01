import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "16589591"))
    API_HASH = os.environ.get("API_HASH", "396d3b2b0f1cd575ab6a34fe65afd7cc")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5430925446:AAHKsxgxdetQSfzsfuFFhd6cGkXfOoPahAw")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOI0Bu13GLMU7zz5UqZv1mNf7mC2-Ri-q7VfDrX3ZK9OfaPyzeiOc44xdE_DMc52AsTAvrvkItE_8_RRTDD2NayEB8gjM9WdB4bazJIRfetX7WmCf0IwgbXmTWPCQBOXZHlkstzNNbrkWAckOzvd7vW8Jhz1i-MUP_-MhEeeG7Oa-x---jsg9fev7L_Tb8jSUVZw9PzKU3bp_N46eb-YY4nRMl1-V_4nN08wzzdiT_Zh6UAmAUAax3atWJodXFBKdjdXssgsvxqyREMLH3LDh1Gev81S2lkxUiLzEAVDsc-FtCfSjwk8KeOGaDcBFEC6cpLtCI8sDWcvmVqHMCzdCebPxWr4=")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "thehouse6bot")
    SUPPORT = os.environ.get("SUPPORT", "ygabutkan")
    CHANNEL = os.environ.get("CHANNEL", "ygabutkan")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
