import os
import threading

from telegram.constants import ParseMode
from submodules import qr_handler as qh
from ui.builder import show_animated_loader


# ------------------- User input functions ------------------- #
async def show_help(update, context):
    """
    Function to list help commands.
    Args:
        update: default telegram arg
        context: default telegram arg
    """
    await update.message.reply_text("""Simply send a text to generate a QR for it!\n
Have ideas and suggestions for this mini project? Head over to the <a href="https://github.com/tjtanjin/tele-qr">Project Repository</a>!""", parse_mode=ParseMode.HTML, disable_web_page_preview=True) # noqa
    return None


async def get_input(update, context):
    """
    Function to get input string from user.
    Args:
        update: default telegram arg
        context: default telegram arg
    """
    chat_id = update.message.chat.id
    try:
        processing_msg = await update.message.reply_text("<b>Generating QR Code |</b>",
                                                         parse_mode=ParseMode.HTML)
        conversion_process = threading.Thread(target=qh.generate_qr,
                                              args=(chat_id, update.message.text))
        conversion_process.start()
        while conversion_process.is_alive():
            await show_animated_loader(processing_msg)

        await context.bot.send_document(chat_id=chat_id,
                                        document=open('./images/{}.png'.format(chat_id), 'rb'),
                                        caption="Here is your QR Code!")
        os.remove("./images/{}.png".format(chat_id))
    except (Exception,):
        await context.bot.send_message(chat_id=chat_id, text='An error has occurred. Please open an issue at our <a href="https://github.com/tjtanjin/tele-qr">Project Repository</a>!', parse_mode=ParseMode.HTML, disable_web_page_preview=True) # noqa
    return None
