import asyncio
import os
import time
import requests
from config import START_IMG
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from FallenMusic import app
from random import choice, randint

# تعريف الدالة command
def command(aliases):
    return filters.command(aliases, prefixes=["/", "!", "."])

@app.on_message(
    command(["مطورين العقرب", "المطورين", "مطورين"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://i.ibb.co/HqPfKH9/image.jpg",
        caption=f"""**𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳
مرحبا بك عزيزي {message.from_user.mention} في قسم مطورين العقرب ميوزك
للتحدث مع مطورين اضغط علي الازرار بالاسفل👇
**𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Alloush", url=f"https://t.me/I_e_e_l"),
                ], [
                    InlineKeyboardButton(
                        "Mohammed", url=f"https://t.me/Zo_r0"),
                ], [
                    InlineKeyboardButton(
                        "السورس", url=f"https://t.me/Scorpion_scorp"),
                ],
            ]
        ),
    )

@app.on_message(
    command(["علوش"])
    & filters.group
)
async def yas(client, message):
    usr = await client.get_chat("I_e_e_l")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(
        photo,
        caption=f"""**𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳

🧞‍♂️ ¦𝙺𝙸𝙽𝙶 : {name}
🎯 ¦𝚄𝚂𝙴𝚁 : @{usr.username}
💣 ¦𝙸𝙳 : `{usr.id}`
🚀 ¦𝙱𝙸𝙾 : {usr.bio}

**𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
  )
