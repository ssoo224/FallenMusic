from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import config
from FallenMusic import BOT_USERNAME

close_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="• مسح •", callback_data="close")]]
)


buttons = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="▷", callback_data="resume_cb"),
            InlineKeyboardButton(text="II", callback_data="pause_cb"),
            InlineKeyboardButton(text="‣‣I", callback_data="skip_cb"),
            InlineKeyboardButton(text="▢", callback_data="end_cb"),
        ]
    ]
)


pm_buttons = [
    [
        InlineKeyboardButton(
            text="‹ اضف البوت في مجموعتك ›",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [InlineKeyboardButton(text="• اوامࢪ التشغيل •", callback_data="fallen_help")],
    [
        InlineKeyboardButton(text="• سوࢪس العقرب •", url=config.SUPPORT_CHANNEL),
        InlineKeyboardButton(text="• جࢪوب الدعم •", url=config.SUPPORT_CHAT),
    ],
    [
        InlineKeyboardButton(
            text="• مطوࢪ السورس •", url="https://t.me/I_e_e_l"
        ),
        InlineKeyboardButton(text="• مالك البوت •", user_id=config.OWNER_ID),
    ],
]


gp_buttons = [
    [
        InlineKeyboardButton(
            text="‹ اضف البوت في مجموعتك ›",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [
        InlineKeyboardButton(text="• سوࢪس العقرب •", url=config.SUPPORT_CHANNEL),
        InlineKeyboardButton(text="• جࢪوب الدعم •", url=config.SUPPORT_CHAT),
    ],
    [
        InlineKeyboardButton(
            text="• مطوࢪ السورس •", url="https://t.me/I_e_e_l"
        ),
        InlineKeyboardButton(text="• مالك البوت •", user_id=config.OWNER_ID),
    ],
]


helpmenu = [
    [
        InlineKeyboardButton(
            text="• اوامࢪ التشغيل •",
            callback_data="fallen_cb help",
        )
    ],
    [
        InlineKeyboardButton(text="• اوامࢪ المطور •", callback_data="fallen_cb sudo"),
        InlineKeyboardButton(text="• اوامࢪ المالك •", callback_data="fallen_cb owner"),
    ],
    [
        InlineKeyboardButton(text="• ࢪجوع •", callback_data="fallen_home"),
        InlineKeyboardButton(text="• مسح •", callback_data="close"),
    ],
]


help_back = [
    [InlineKeyboardButton(text="• جࢪوب الدعم •", url=config.SUPPORT_CHAT)],
    [
        InlineKeyboardButton(text="• ࢪجوع •", callback_data="fallen_help"),
        InlineKeyboardButton(text="• مسح •", callback_data="close"),
    ],
]
