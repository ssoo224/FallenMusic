import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from FallenMusic import app
import re
import sys

GAME_MESSAGE = "𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳\n\n★¦ مرحبا بك عزيزي:\n★¦في قسم العاب العقرب\n\n𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳"
GAME_BUTTONS = [
    [ 
        InlineKeyboardButton ('★¦العاب 3D', callback_data= 'GAME1'),
        InlineKeyboardButton ('★¦العاب العقرب', callback_data= 'GAME2'),
    ], [
        InlineKeyboardButton ('السورس', url =f"https://t.me/Scorpion_scorp")
    ], [
        InlineKeyboardButton("◁", callback_data="close"),
    ]
]

nmla = []

@app.on_message(filters.command("رفع نمله"))
async def rf3nmla(client, message):
    if message.reply_to_message:
        if not message.reply_to_message.from_user.mention in nmla:
            nmla.append(message.reply_to_message.from_user.mention)
        await message.reply_text(f"تم رفع العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n نمله 😂♥️")
    else:
        await message.reply_text("يرجى الرد على رسالة العضو الذي تريد رفعه.")

@app.on_message(filters.command("تنزيل نمله"))
async def tnzelnmla(client, message):
    if message.reply_to_message:
        if message.reply_to_message.from_user.mention in nmla:
            nmla.remove(message.reply_to_message.from_user.mention)
        await message.reply_text(f"تم تنزيل العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n نمله 😂♥️")
    else:
        await message.reply_text("يرجى الرد على رسالة العضو الذي تريد تنزيله.")

@app.on_message(filters.command("المرفوعين نمل"))
async def nml(client, message):
    if nmla:
        nq = "\n".join(nmla)
        await message.reply_text(f"**المرفوعين نمل:**\n\n{nq}")
    else:
        await message.reply_text("لا يوجد أي أعضاء مرفوعين.")