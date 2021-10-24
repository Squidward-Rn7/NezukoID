from telethon.tl.functions.messages import SaveDraftRequest

from nezukoidbot.utils import edit_or_reply, nezukoid_on_cmd, sudo_cmd


@nezuko.on(nezuko_on_cmd(pattern="chain"))
@nezuko.on(sudo_cmd(pattern="chain", allow_sudo=True))
async def _(event):
    pokemonlub = await edit_or_reply(event, "Counting...")
    count = -1
    message = event.message
    while message:
        reply = await message.get_reply_message()
        if reply is None:
            await borg(
                SaveDraftRequest(
                    await event.get_input_chat(), "", reply_to_msg_id=message.id
                )
            )
        message = reply
        count += 1
    await pokemonlub.edit(f"Chain length: {count}")
