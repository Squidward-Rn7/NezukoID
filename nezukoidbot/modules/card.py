from faker import Faker as dc

from nezukoidbot import bot as nezukoidbot

from ..utils import admin_cmd as wtf


@nezukobot.on(wtf("card"))
async def _firee(nezuko):
    cyber = dc()
    killer = cyber.name()
    kali = cyber.address()
    chris = cyber.credit_card_full()
    await nezuko.edit(f"βπππ:-\n`{killer}`\n\nπΈπππ£ππ€π€:-\n`{kali}`\n\nβππ£π:-\n`{chris}`")
