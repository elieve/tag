import os

from telethon import Button, events

from Zaid import *

IMG = os.environ.get(
    "PING_PIC", "https://telegra.ph/file/1096e0e416339bcbcf482.jpg"
)
ms = 4

ALIVE = os.environ.get(
    "ALIVE", "@baytoddd"
)

CAPTION = f"**꧁•⊹٭Ping٭⊹•꧂**\n\n   ⚜ {ms}\n   ⚜ ❝𝐌𝐲 𝐌𝐚𝐬𝐭𝐞𝐫❞ ~『{ALIVE}』"


@Zaid.on(events.NewMessage(pattern="^/ping"))
async def _(event):
    UMM = [[Button.url("⚜ Creator ⚜", "https://t.me/baytoddd")]]
    await Zaid.send_file(event.chat_id, IMG, caption=CAPTION, buttons=UMM)
