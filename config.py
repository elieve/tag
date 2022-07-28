import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "16589591"))
    API_HASH = os.environ.get("API_HASH", "396d3b2b0f1cd575ab6a34fe65afd7cc")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5541963320:AAHKvCNHfRLiMmoGho0z6DEllhhW9K6elh4")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOIoBuxJa2re6FhPmtw_dmd7Y6Ruatsax7MatM9E9ZmOUQ9YRheB2FtN-ycTqOM-QSceEJsc1nxXwsPo71kXrEmc3wBNBfgP4OrW1FErQz7JMj5_U_SUL06laskBS2cp_zbgB3YCAPBRqfna-j64kq4ZclglISqm-i3A_gtFcbwdzHBhmaHtdE0dJh0nUZWr0exRnzbmezk03EzWHKV9_tiIRd50Dv92gkEFhIvdH1T3yju3KuA9wuY1VwkaML4LQq4lNMeAlQNq-YIBmDHrXgnJ_ObxnTFeU7UEz98b9uYQrSa0GL_jSOJssw9yt5Dwp9zwDnuqy3ZJjiSj56NyWAXclw28=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "elieverobot")
    SUPPORT = os.environ.get("SUPPORT", "ygabutkan")
    CHANNEL = os.environ.get("CHANNEL", "ygabutkan")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
