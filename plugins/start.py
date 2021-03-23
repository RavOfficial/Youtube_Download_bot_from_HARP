from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Update Channel 🇱🇰", url="https://t.me/Harp_Tech")]
        [InlineKeyboardButton("Update Chat 🇱🇰", url="https://t.me/HARP_Chat")]
    ])
    welcomed = f"<b>Hey {message.from_user.first_name} \nIf you need help 🙄 Just click /help\n\n</b>"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
