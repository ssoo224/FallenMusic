from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = 22776977
API_HASH = "03c90a05ee5ac2287f11e2cfb73648ac"
BOT_TOKEN = "7873853121:AAHznmevVDj3F8r-vC6ctQzXeJiXaAmdZ8I"
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = 7115002714
PING_IMG = getenv("PING_IMG", "https://i.ibb.co/HqPfKH9/image.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg")

SESSION = "AgCIVfMAOpD4GSbUpBy7709ICTynrgx5Fn_yB5ALm8mw75vs8CPQLvdY2LWsQZpHwu2wYoFX5Mk5NayTuJlsUE47gz7yqz8MAUqtH8-6gP7DVnjCosaUN0VIQ4pWNG5RpeQwMUJ3ZRW6oXNra3LypielfolICgujB4SXItHXwMJ_89llTlza-Cmu9xroDtRZWPmDUZYDBa3NWR6bllGMo91w_FLNFWgocDntUD_HrrHUdp4aBh6fLb_Vc9sElkEFwzY0f2XzYMDBD9mRUiUCo11WbvjNRs9WCsLU3aQe2jwTOYkzehIKxUP7Ck3uW3y_gczoRz-1imltc7H2JAaeEcdDmweB8AAAAAHMVWK_AA"
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/sorpiongroup")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Scorpion_scorp")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7115002714").split()))

FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
