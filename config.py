from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

class Config(object):
    # required config variables
    API_HASH = getenv("6da533e7c45bc668182b5a0f5a4497dd", None)                # get from my.telegram.org
    API_ID = int(getenv("22658021", 0))                  # get from my.telegram.org
    BOT_TOKEN = getenv("7902782706:AAE-IS88ujC2w8zb8CT0LAs25joNPFUw8mI", None)              # get from @BotFather
    DATABASE_URL = getenv("mongodb+srv://mohsin:mohsin@cluster0.iauaztt.mongodb.net/?retryWrites=true&w=majority", None)        # from https://cloud.mongodb.com/
    HELLBOT_SESSION = getenv("BQFZu-UAgqtUIQNmJjC92qTFvTksgND6RVa_dq49tn0fJOXb7jw9ci5Obc9EigL57PHkNMg8W6VT0tgc3hx2uDA2tNKYZgHXpUEkWLGyLkI6y3PnRTySn9VQi5upM22WP_XWcmd3fBZruIWrerNJcBwXhAMB4AmBPPWTgrzMMabhPdcia3B0yX582rfnG_DitgydYtioOxlgyLYmjQhnFQacCdA7s7SFZNY0cwIwzI_xBhPFIT8E4rST6PJSMAWvo2FwQgdL8vvf3NCGkuVPQYKJnJIJrGkz0xWFFNMIeG7oIrVh5iu4-2-D8O8VTKGV5BrJ7DMJ8-l4MqJhcq-3t9cBLMmW2wAAAAF4n1AAAA", None)  # enter your session string here
    LOGGER_ID = int(getenv("-1002337115461", 0))            # make a channel and get its ID
    OWNER_ID = getenv("6318673920", "")                  # enter your id here

    # optional config variables
    BLACK_IMG = getenv("BLACK_IMG", "https://telegra.ph/file/2c546060b20dfd7c1ff2d.jpg")        # black image for progress
    BOT_NAME = getenv("BOT_NAME", "\x40\x4d\x75\x73\x69\x63\x5f\x48\x65\x6c\x6c\x42\x6f\x74")   # dont put fancy texts here.
    BOT_PIC = getenv("BOT_PIC", "https://te.legra.ph/file/5d5642103804ae180e40b.jpg")           # put direct link to image here
    LEADERBOARD_TIME = getenv("LEADERBOARD_TIME", "3:00")   # time in 24hr format for leaderboard broadcast
    LYRICS_API = getenv("LYRICS_API", None)             # from https://docs.genius.com/
    MAX_FAVORITES = int(getenv("MAX_FAVORITES", 30))    # max number of favorite tracks
    PLAY_LIMIT = int(getenv("PLAY_LIMIT", 0))           # time in minutes. 0 for no limit
    PRIVATE_MODE = getenv("PRIVATE_MODE", "off")        # "on" or "off" to enable/disable private mode
    SONG_LIMIT = int(getenv("SONG_LIMIT", 0))           # time in minutes. 0 for no limit
    TELEGRAM_IMG = getenv("TELEGRAM_IMG", None)         # put direct link to image here
    TG_AUDIO_SIZE_LIMIT = int(getenv("TG_AUDIO_SIZE_LIMIT", 104857600))     # size in bytes. 0 for no limit
    TG_VIDEO_SIZE_LIMIT = int(getenv("TG_VIDEO_SIZE_LIMIT", 1073741824))    # size in bytes. 0 for no limit
    TZ = getenv("TZ", "Asia/Kolkata")   # https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

    # do not edit these variables
    BANNED_USERS = filters.user()
    CACHE = {}
    CACHE_DIR = "./cache/"
    DELETE_DICT = {}
    DWL_DIR = "./downloads/"
    GOD_USERS = filters.user()
    PLAYER_CACHE = {}
    QUEUE_CACHE =  {}
    SONG_CACHE = {}
    SUDO_USERS = filters.user()


# get all config variables in a list
all_vars = [i for i in Config.__dict__.keys() if not i.startswith("__")]
