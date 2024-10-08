from telebot.util import quick_markup
import traceback

from TgMessage import TgMessage
from ErrorHandler import ErrorHandler


class Utils:
    @staticmethod
    def alert_dadm(tickets, bot, issue_link_pattern, config):
        try:
            message = TgMessage()
            for ticket in tickets:
                message.processing_markup(ticket, issue_link_pattern)

            print(bot.send_message(config.TELEGRAM_GROUP_ID, text=message.text,
                                   reply_markup=quick_markup(message.markup_dict),
                                   parse_mode="HTML").json)
            del message

    # todo начать писать resolve
        except Exception as e:
            error_handler = ErrorHandler(e, traceback.format_exc())
            error_handler.save_error_log()

            error_handler.handel_unexpected_error()
