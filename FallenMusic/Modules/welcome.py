import os
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from FallenMusic import app

# تعريف دالة command
def command(commands):
    return filters.command(commands, prefixes=["/", "!", "."])  # يمكنك تخصيص البادئات

# ترحيب عند دخول عضو جديد
@app.on_message(filters.new_chat_members)
async def wel__come(client: Client, message: Message):
    chat_id = message.chat.id
    for member in message.new_chat_members:
        await client.send_message(
            chat_id=chat_id,
            text=f"- نورت يحلو {member.mention}\n│ \n└ʙʏ في {message.chat.title}"
        )

# وداع عند خروج عضو
@app.on_message(filters.left_chat_member)
async def good_bye(client: Client, message: Message):
    chat_id = message.chat.id
    await client.send_message(
        chat_id=chat_id,
        text=f"- توصل بالسلامة\n│ \n└ʙʏ {message.left_chat_member.mention}"
    )

# أمر عموره وصاحب العظمة
@app.on_message(command(["علوش", "السورس", "العقرب", "علوشة"]) & filters.group)
async def kkpp(client: Client, message: Message):
    usr = await client.get_chat("I_e_e_l")
    name = usr.first_name
    photo = await client.download_media(usr.photo.big_file_id)
    await message.reply_photo(
        photo,
        caption=f"""**𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳

🧞‍♂️ ¦OMAR : {name}
🎯 ¦𝚄𝚂𝙴𝚁 : @{usr.username}
💣 ¦𝙸𝙳 : `{usr.id}`
🚀 ¦𝙱𝙸𝙾 : {usr.bio}

**𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(name, url=f"https://t.me/{usr.username}")]]
        ),
    )
