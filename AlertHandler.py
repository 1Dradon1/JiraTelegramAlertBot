import time

from telebot.util import quick_markup
import traceback
import threading

from TgMessage import TgMessage
from ErrorHandler import ErrorHandler


class AlertHandler:
    @staticmethod
    def alert_issue_dadm(issues, bot, config):
        try:
            message = TgMessage()
            for issue in issues:
                message.processing_markup(issue, config.issues_link_pattern)

            print(bot.send_message(config.TELEGRAM_GROUP_ID, text=message.text,
                                   reply_markup=quick_markup(message.markup_dict),
                                   parse_mode='HTML').json)
            del message

    # todo начать писать resolve
        except Exception as e:
            error_handler = ErrorHandler(e, traceback.format_exc(), config)
            error_handler.save_error_log()
            error_handler.handel_unexpected_error()

    @staticmethod
    def alert_works_dadm(works, bot, config):
        try:
            message = TgMessage()

            if works["approaching_works"]:
                message.text += f"Через {config.works_delay} мин: \n"

                for work in works["approaching_works"]:
                    message.processing_markup(work, config.issues_link_pattern)

            if works["upcoming_works"]:
                message.text += "Скоро начнется: \n"
                for work in works["upcoming_works"]:
                    message.processing_markup(work, config.issues_link_pattern)

            print(bot.send_message(config.TELEGRAM_GROUP_ID, text=message.text,
                                   reply_markup=quick_markup(message.markup_dict),
                                   parse_mode='HTML').json)
            del message

        # todo начать писать resolve
        except Exception as e:
            error_handler = ErrorHandler(e, traceback.format_exc(), config)
            error_handler.save_error_log()
            error_handler.handel_unexpected_error()

    @staticmethod
    def start_alert_thread(target_func, items, bot, config):
        """Создает и запускает поток для передачи уведомлений"""
        if items:
            alert_thread = threading.Thread(target=target_func, args=(items, bot, config))
            alert_thread.start()