from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"В настоящее время поддерживается только Youtube Single (без плейлиста). Просто отправьте URL-адрес Youtube."
    await message.reply_text(helptxt)
