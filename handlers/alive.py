import asyncio
from time import time
from datetime import datetime
from modules.config import BOT_USERNAME
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/5932850420f4f3f61ac81.jpg",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
💥 𝗛𝗲𝗹𝗹𝗼, 𝗜 𝗔𝗺 𝗜𝗿𝗼𝗻♡𝗛𝗲𝗮𝗿𝘁 𝗠𝘂𝘀𝗶𝗰 𝗕𝗼𝘁.
𝗜 𝗖𝗮𝗻 𝗣𝗹𝗮𝘆 𝗠𝘂𝘀𝗶𝗰 𝗜𝗻 𝗚𝗿𝗼𝘂𝗽𝘀 𝗩𝗖...😍
┏━━━━━━━━━━━━━━━━━┓
┣★ 𝗢𝘄𝗻𝗲𝗿 : [𝗛𝗮𝗿𝘀𝗵](https://t.me/H4RSH_007)
┣★ 𝗦𝘂𝗽𝗽𝗼𝗿𝘁 : [𝗜𝗿𝗼𝗻𝗛𝗲𝗮𝗿𝘁](https://t.me/ironheartsupport722)
┣★ 𝗦𝗼𝘂𝗿𝗰𝗲 : [𝗖𝗹𝗶𝗰𝗸 𝗛𝗲𝗿𝗲](https://t.me/H4RSH_007)
┗━━━━━━━━━━━━━━━━━┛

━━━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "😆 ❰ 𝘼𝙙𝙙 𝙈𝙚 𝙄𝙣 𝙂𝙧𝙤𝙪𝙥 ❱ 😆", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "/alive", "/ironheart"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/5932850420f4f3f61ac81.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 𝗦𝘂𝗽𝗽𝗼𝗿𝘁 💞", url=f"https://t.me/ironheartsupport722")
                ]
            ]
        ),
    )


@Client.on_message(commandpro(["repo", "#repo", "@repo", "/repo", "source"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/5932850420f4f3f61ac81.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "😆 𝘾𝙡𝙞𝙘𝙠 𝙃𝙚𝙧𝙚 𝙏𝙤 𝙂𝙚𝙩 𝙍𝙚𝙥𝙤 😆", url=f"https://t.me/H4RSH_007")
                ]
            ]
        ),
    )
