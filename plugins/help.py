from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"<b>🔸 First send youtube video link.\n\n🔸 Then Select video format and video quality.\n\n🔸 Now wait, I will upload video to telegram.\n\n🔹 Youtube playlists are not supported</b>"
    await message.reply_text(helptxt)
