import os
import aiohttp
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command("telegraph") & filters.private)
async def telegraph_upload(bot, update):
    replied = update.reply_to_message
    if not replied:
        return await update.reply_text("Rᴇᴘʟʏ Tᴏ A Pʜᴏᴛᴏ Oʀ Vɪᴅᴇᴏ Uɴᴅᴇʀ 5ᴍʙ")
    
    # Download media to local
    media = await replied.download()
    
    # Notify user
    text = await update.reply_text("Downloading completed. Uploading to envs.sh ...")
    
    try:
        async with aiohttp.ClientSession() as session:
            with open(media, "rb") as f:
                files = {"file": f}
                async with session.post("https://envs.sh/api/v1/upload", data=files) as resp:
                    if resp.status != 200:
                        return await text.edit_text(f"Upload failed with status code {resp.status}")
                    res_json = await resp.json()
        
        # Get file URL from response
        file_url = res_json.get("url")
        if not file_url:
            return await text.edit_text("Failed to get file URL from envs.sh response.")
        
        # Remove downloaded file
        os.remove(media)
        
        # Send link with inline buttons
        await text.edit_text(
            f"<b>Link:</b>\n\n<code>{file_url}</code>",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Open Link", url=file_url),
                 InlineKeyboardButton("Share Link", url=f"https://telegram.me/share/url?url={file_url}")],
                [InlineKeyboardButton("✗ Close ✗", callback_data="close")]
            ])
        )
    except Exception as e:
        await text.edit_text(f"Error: {e}")
        if os.path.exists(media):
            os.remove(media)
