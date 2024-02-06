import os

DEVS = [
    6723369488,
]

API_ID = int(os.getenv("API_ID", "25927541"))

API_HASH = os.getenv("API_HASH", "755b0d5e86f5469696fdd1abd0013c69")

BOT_TOKEN = os.getenv("BOT_TOKEN", "6672841006:AAHAeV1lN853--XTTZ1faY1GFV52xPUB850")

OWNER_ID = int(os.getenv("OWNER_ID", "6723369488"))

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
    "mongodb+srv://vewonon211:vewonon211@joysoy.kokbtub.mongodb.net/?retryWrites=true&w=majority",
)


