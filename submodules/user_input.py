from telegram import ParseMode
from telegram.ext.dispatcher import run_async
from submodules import qr_handler as qh
import os, threading

#------------------- User input functions -------------------#
@run_async
def show_help(update, context):
    """
    Function to list help commands.
    Args:
        update: default telegram arg
        context: default telegram arg
    """
    update.message.reply_text("""Simply send a text to generate a QR for it!\n
Have ideas and suggestions for this mini project? Head over to the <a href="https://github.com/tjtanjin/tele-qr">Project Repository</a>!""", parse_mode=ParseMode.HTML, disable_web_page_preview=True)
    return None

@run_async
def get_input(update, context): 
    """
    Function to get input string from user.
    Args:
        update: default telegram arg
        context: default telegram arg
    """
    chat_id = update.message.chat.id
    generating_qr = False
    def load_animation(update, message):
        """
        Function that provides loading animation during qr code generation.
        Args:
            update: default telegram arg
            message: message showing progress to user
        """
        while generating_qr:
            message.edit_text(text="<b>Generating QR Code /</b>", parse_mode=ParseMode.HTML)
            message.edit_text(text="<b>Generating QR Code -</b>", parse_mode=ParseMode.HTML)
            message.edit_text(text="<b>Generating QR Code \\</b>", parse_mode=ParseMode.HTML)
            message.edit_text(text="<b>Generating QR Code |</b>", parse_mode=ParseMode.HTML)
        message.edit_text(text="<b>QR Code Generated:</b>", parse_mode=ParseMode.HTML)
        return None
    try:
        generating_qr = True
        generating = update.message.reply_text("<b>Generating QR Code |</b>", parse_mode=ParseMode.HTML)
        threading.Thread(target=load_animation, args=(update, generating)).start()
        qh.generate_qr(chat_id, update.message.text)
        generating_qr = False
        context.bot.send_document(chat_id=chat_id, document=open('./images/{}.png'.format(chat_id), 'rb'), caption="Here is your QR Code!")
        os.remove("./images/{}.png".format(chat_id))
    except:
        context.bot.send_message(chat_id=chat_id, text='An error has occurred. Please open an issue at our <a href="https://github.com/tjtanjin/tele-qr">Project Repository</a>!', parse_mode=ParseMode.HTML, disable_web_page_preview=True)
    return None