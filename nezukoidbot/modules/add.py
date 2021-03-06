"""Invite the user(s) to the current chat
Syntax: .invite <User(s)>"""

from telethon import functions

from nezukoidbot.utils import nezuko_on_cmd

"""Invite the user(s) to the current chat
Syntax: .invite <User(s)>"""

from telethon import functions

from nezukoidbot import CMD_HELP
from nezukoidbot.utils import edit_or_reply, nezuko_on_cmd, sudo_cmd


@nezuko.on(nezuko_on_cmd(pattern="invite ?(.*)"))
@nezuko.on(sudo_cmd(pattern="invite ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    to_add_users = event.pattern_match.group(1)
    if event.is_private:
        await edit_or_reply(
            event, "`.invite` users to a chat, not to a Private Message"
        )
    else:
        logger.info(to_add_users)
        if not event.is_channel and event.is_group:
            # https://lonamiwebs.github.io/Telethon/methods/messages/add_chat_user.html
            for user_id in to_add_users.split(" "):
                try:
                    await borg(
                        functions.messages.AddChatUserRequest(
                            chat_id=event.chat_id, user_id=user_id, fwd_limit=1000000
                        )
                    )
                except Exception as e:
                    await event.reply(str(e))
            await event.edit("Invited Successfully")
        else:
            # https://lonamiwebs.github.io/Telethon/methods/channels/invite_to_channel.html
            for user_id in to_add_users.split(" "):
                try:
                    await borg(
                        functions.channels.InviteToChannelRequest(
                            channel=event.chat_id, users=[user_id]
                        )
                    )
                except Exception as e:
                    await event.reply(str(e))
                await edit_or_reply(event, "Invited Successfully")


CMD_HELP.update(
    {
        "add": "**Add**\
\n\n**Syntax : **`.add <user_id or user-name>`\
\n**Usage :** Adds User To Group"
    }
)
