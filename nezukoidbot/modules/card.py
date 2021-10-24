from faker import Faker as dc

from nezukoidbot import bot as nezukoidbot

from ..utils import admin_cmd as wtf


@nezukobot.on(wtf("card"))
async def _firee(nezuko):
    cyber = dc()
    killer = cyber.name()
    kali = cyber.address()
    chris = cyber.credit_card_full()
    await nezuko.edit(f"ℕ𝕒𝕞𝕖:-\n`{killer}`\n\n𝔸𝕕𝕕𝕣𝕖𝕤𝕤:-\n`{kali}`\n\nℂ𝕒𝕣𝕕:-\n`{chris}`")
