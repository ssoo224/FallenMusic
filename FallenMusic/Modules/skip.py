from pyrogram import filters
from pyrogram.types import Message
from pytgcalls.types import AudioPiped, HighQualityAudio

from FallenMusic import BOT_USERNAME, app, fallendb, pytgcalls
from FallenMusic.Helpers import _clear_, admin_check, buttons, close_key, gen_thumb


@app.on_message(filters.command(["skip", "next"]) | filters.command(["تخطي","التالى","التالي"],prefixes= ["/", "!","","#"]) & filters.group)
@admin_check
async def skip_str(_, message: Message):
    try:
        await message.delete()
    except:
        pass
    get = fallendb.get(message.chat.id)
    if not get:
        try:
            await _clear_(message.chat.id)
            await pytgcalls.leave_group_call(message.chat.id)
            await message.reply_text(
                text=f"✎┊‌ الـتـالـي 🥺\n \n✎┊‌ بواسطة : {message.from_user.mention} 🥀\n\n**✎┊‌ مفيش اغاني** {message.chat.title}, **🕷**",
                reply_markup=close_key,
            )
        except:
            return
    else:
        title = get[0]["title"]
        duration = get[0]["duration"]
        file_path = get[0]["file_path"]
        videoid = get[0]["videoid"]
        req_by = get[0]["req"]
        user_id = get[0]["user_id"]
        get.pop(0)

        stream = AudioPiped(file_path, audio_parameters=HighQualityAudio())
        try:
            await pytgcalls.change_stream(
                message.chat.id,
                stream,
            )
        except:
            await _clear_(message.chat.id)
            return await pytgcalls.leave_group_call(message.chat.id)

        await message.reply_text(
            text=f"✎┊‌ الـتـالي 🥺\n \n✎┊‌ بواسطة : {message.from_user.mention} 🥀\n\n**✎┊‌ مفيش اغاني** {message.chat.title}, **🕷**",
            reply_markup=close_key,
        )
        img = await gen_thumb(videoid, user_id)
        return await message.reply_photo(
            photo=img,
            caption=f"**✎┊‌ تم التشغيل ✅**\n\n✎┊‌ **العنوان :** [{title[:27]}](https://t.me/{BOT_USERNAME}?start=info_{videoid})\n✎┊‌ **المدة :** `{duration}` دقيقه\n✎┊‌ **بواسطه :** {req_by}",
            reply_markup=buttons,
        )
