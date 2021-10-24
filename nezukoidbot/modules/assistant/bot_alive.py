from nezukoidbot import ALIVE_NAME
from nezukoidbot.modules import currentversion

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = "https://telegra.ph/file/bcecc640c26dd9268941d.jpg"
pm_caption = "➥ **ASSISTANT IS:** `ONLINE`\n\n"
pm_caption += "➥ **SYSTEMS STATS**\n"
pm_caption += "➥ **Telethon Version:** `1.23.0` \n"
pm_caption += "➥ **Python:** `3.9.0` \n"
pm_caption += "➥ **Database Status:**  `Functional`\n"
pm_caption += "➥ **Current Branch** : `master`\n"
pm_caption += f"➥ **Version** : `{currentversion}`\n"
pm_caption += f"➥ **My Owner** : {DEFAULTUSER} \n\n"

# only Owner Can Use it
@assistant_cmd("alive", is_args=False)
@peru_only
async def nezuko(event):
    await tgbot.send_file(event.chat_id, PM_IMG, caption=pm_caption)
