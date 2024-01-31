import qrcode


def generate_qr(chat_id, user_input):
    """
    The function generates a QR code image and saves it to be returned to the user.
    Args:
        chat_id: unique identification for user
        user_input: user string to generate QR with
    """
    img = qrcode.make(user_input)
    img.save('./images/{}.png'.format(chat_id))
    return None
