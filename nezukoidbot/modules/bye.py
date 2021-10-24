"""
.bye
"""
import time

from telethon.tl.functions.channels import LeaveChannelRequest

from nezukoidbot import CMD_HELP
from nezukoidbot.utils import nezuko_on_cmd, sudo_cmd


@nezuko.on(nezuko_on_cmd("bye"))
@nezuko.on(sudo_cmd("bye", allow_sudo=True))
async def leave(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        time.sleep(3)
        if e.is_group:
            await e.edit("`I’m not wanted here so I’m leaving.`")
            await borg(LeaveChannelRequest(e.chat_id))
        else:
            await e.edit("`Boss, This is Not A Chat`")


CMD_HELP.update(
    {
        "bye": "**Bye**\
\n\n**Syntax : **`.bye`\
\n**Usage :** use this plugin to leave a group."
    }
)
