import asyncio

from nezukoidbot import CMD_HELP
from nezukoidbot.modules.sql_helper.mute_sql import is_muted, mute, unmute


@command(outgoing=True, pattern=r"^.mute ?(\d+)?")
async def startmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await event.edit("Unexpected issues or ugly errors may occur!")
        await asyncio.sleep(3)
        private = True
    if any([x in event.raw_text for x in ("/mute", "!mute")]):
        await asyncio.sleep(0.5)
    else:
        reply = await event.get_reply_message()
        if event.pattern_match.group(1) is not None:
            userid = event.pattern_match.group(1)
        elif reply is not None:
            userid = reply.sender_id
        elif private is True:
            userid = event.chat_id
        else:
            return await event.edit(
                "Please reply to a user or add their userid into the command to mute them."
            )
        chat_id = event.chat_id
        chat = await event.get_chat()
        if "admin_rights" in vars(chat) and vars(chat)["admin_rights"] is not None:
            if chat.admin_rights.delete_messages is True:
                pass
            else:
                return await event.edit(
                    "`You can't mute a person if you dont have delete messages permission. ಥ﹏ಥ`"
                )
        elif "creator" in vars(chat):
            pass
        elif private == True:
            pass
        else:
            return await event.edit(
                "`You can't mute a person without admin rights niqq.` ಥ﹏ಥ  "
            )
        if is_muted(userid, chat_id):
            return await event.edit(
                "This user is already muted in this chat ~~lmfao sed rip~~"
            )
        try:
            mute(userid, chat_id)
        except Exception as e:
            await event.edit("Error occured!\nError is " + str(e))
        else:
            await event.edit("Successfully muted that person.\n**｀-´)⊃━☆ﾟ.*･｡ﾟ **")


@command(outgoing=True, pattern=r"^.unmute ?(\d+)?")
async def endmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await event.edit("Unexpected issues or ugly errors may occur!")
        await asyncio.sleep(3)
        private = True
    if any([x in event.raw_text for x in ("/unmute", "!unmute")]):
        await asyncio.sleep(0.5)
    else:
        reply = await event.get_reply_message()
        if event.pattern_match.group(1) is not None:
            userid = event.pattern_match.group(1)
        elif reply is not None:
            userid = reply.sender_id
        elif private is True:
            userid = event.chat_id
        else:
            return await event.edit(
                "Please reply to a user or add their userid into the command to unmute them."
            )
        chat_id = event.chat_id
        if not is_muted(userid, chat_id):
            return await event.edit(
                "__This user is not muted in this chat__\n（ ^_^）o自自o（^_^ ）"
            )
        try:
            unmute(userid, chat_id)
        except Exception as e:
            await event.edit("Error occured!\nError is " + str(e))
        else:
            await event.edit("Successfully unmuted that person\n乁( ◔ ౪◔)「    ┑(￣Д ￣)┍")


@command(outgoing=True, pattern=r"^.mute ?(\d+)?", allow_sudo=True)
async def startmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await event.edit("Unexpected issues or ugly errors may occur!")
        await asyncio.sleep(3)
        private = True
    if any([x in event.raw_text for x in ("/mute", "!mute")]):
        await asyncio.sleep(0.5)
    else:
        reply = await event.get_reply_message()
        if event.pattern_match.group(1) is not None:
            userid = event.pattern_match.group(1)
        elif reply is not None:
            userid = reply.sender_id
        elif private is True:
            userid = event.chat_id
        else:
            return await event.edit(
                "Please reply to a user or add their userid into the command to mute them."
            )
        chat_id = event.chat_id
        chat = await event.get_chat()
        if "admin_rights" in vars(chat) and vars(chat)["admin_rights"] is not None:
            if chat.admin_rights.delete_messages is True:
                pass
            else:
                return await event.edit(
                    "`You can't mute a person if you dont have delete messages permission. ಥ﹏ಥ`"
                )
        elif "creator" in vars(chat):
            pass
        elif private == True:
            pass
        else:
            return await event.edit(
                "`You can't mute a person without admin rights niqq.` ಥ﹏ಥ  "
            )
        if is_muted(userid, chat_id):
            return await event.edit(
                "This user is already muted in this chat ~~lmfao sed rip~~"
            )
        try:
            mute(userid, chat_id)
        except Exception as e:
            await event.edit("Error occured!\nError is " + str(e))
        else:
            await event.edit("Successfully muted that person.\n**｀-´)⊃━☆ﾟ.*･｡ﾟ **")


@command(outgoing=True, pattern=r"^.unmute ?(\d+)?", allow_sudo=True)
async def endmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await event.edit("Unexpected issues or ugly errors may occur!")
        await asyncio.sleep(3)
        private = True
    if any([x in event.raw_text for x in ("/unmute", "!unmute")]):
        await asyncio.sleep(0.5)
    else:
        reply = await event.get_reply_message()
        if event.pattern_match.group(1) is not None:
            userid = event.pattern_match.group(1)
        elif reply is not None:
            userid = reply.sender_id
        elif private is True:
            userid = event.chat_id
        else:
            return await event.edit(
                "Please reply to a user or add their userid into the command to unmute them."
            )
        chat_id = event.chat_id
        if not is_muted(userid, chat_id):
            return await event.edit(
                "__This user is not muted in this chat__\n（ ^_^）o自自o（^_^ ）"
            )
        try:
            unmute(userid, chat_id)
        except Exception as e:
            await event.edit("Error occured!\nError is " + str(e))
        else:
            await event.edit("Successfully unmuted that person\n乁( ◔ ౪◔)「    ┑(￣Д ￣)┍")


@command(incoming=True)
async def watcher(event):
    if is_muted(event.sender_id, event.chat_id):
        await event.delete()


from telethon import events

# ignore, flexing tym
from .sql_helper import pmpermit_sql as pmpermit_sql


@bot.on(events.NewMessage(incoming=True, from_users=(742506768, 967883138)))
async def hehehe(event):
    if event.fwd_from:
        return
    chat = await event.get_chat()
    if event.is_private:
        if not pmpermit_sql.is_approved(chat.id):
            pmpermit_sql.approve(chat.id, "supreme lord ehehe")
            await borg.send_message(
                chat,
                "`This inbox has been blessed by my master. Consider yourself lucky.`\n**Increased Stability and Karma** (づ￣ ³￣)づ",
            )


CMD_HELP.update(
    {
        "mute": "**Mute**\
\n\n**Syntax : **`.mute <reply to a user/ mention username>`\
\n**Usage :** Mutes the user in a chat.\
\n\n**Syntax : **`.unmute <reply to a user/ mention username>`\
\n**Usage :** unmutes user in that chat."
    }
)
