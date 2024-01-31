from telegram.constants import ParseMode


async def show_animated_loader(message):
    """
    Provides loading animation during qr code generation.
    Args:
        message: message to edit to show loader
    """
    await message.edit_text(text="<b>Generating QR Code /</b>", parse_mode=ParseMode.HTML)
    await message.edit_text(text="<b>Generating QR Code -</b>", parse_mode=ParseMode.HTML)
    await message.edit_text(text="<b>Generating QR Code \\</b>", parse_mode=ParseMode.HTML)
    await message.edit_text(text="<b>Generating QR Code |</b>", parse_mode=ParseMode.HTML)
    return None
