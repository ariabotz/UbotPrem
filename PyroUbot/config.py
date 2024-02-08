import os

DEVS = [
    6890751790,
]

API_ID = int(os.getenv("API_ID", "21393516"))

API_HASH = os.getenv("API_HASH", "9ea808c58bec34fb6c8a7da1e32b5ddc")

BOT_TOKEN = os.getenv("BOT_TOKEN", "6728027184:AAEZHRbPyFuUPjOvOH8Fl5QE9r_GRyYNAsk")

OWNER_ID = int(os.getenv("OWNER_ID", "6890751790"))

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1002048436505"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1001473548283").split()))

MAX_BOT = int(os.getenv("MAX_BOT", "550"))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

COMMAND = os.getenv("COMMAND", ".")
PREFIX = COMMAND.split()

OPENAI_KEY = os.getenv(
    "OPENAI_KEY",
    "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",
).split()

MONGO_URL = os.getenv(
    "MONGO_URL",
    "mongodb+srv://ariaputrapratamaaaa:jys25mZSkyH3x9jo@cluster0.nebsqze.mongodb.net/",
)


