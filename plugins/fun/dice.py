# codes added by @lallu_tg
# use with proper credits

from pyrogram import Client, filters


# EMOJI CONSTANTS
DICE_E_MOJI = "🎲"
# EMOJI CONSTANTS


@Client.on_message(
   filters.private & filters.command(["roll", "dice"])
)
async def roll_dice(client, message):
    """ @RollaDie """
    rep_mesg_id = message.message_id
    if message.reply_to_message:
        rep_mesg_id = message.reply_to_message.message_id
    await client.send_dice(
        chat_id=message.chat.id,
        emoji=DICE_E_MOJI,
        disable_notification=True,
        reply_to_message_id=rep_mesg_id
    )
