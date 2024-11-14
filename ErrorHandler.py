import time
import datetime

import telebot

from telebot.apihelper import ApiException

from jira import JIRAError, JIRA
import traceback
from configs.Config_Test import Config

config = Config()

class ErrorHandler:
    """
     self.config: config
     self.bot: Telegram bot
     self.e: error
     self.trace: error traceback
    """
    def __init__(self, e, trace, config):
        self.config = config
        self.bot = telebot.TeleBot(self.config.BOT_TOKEN)
        self.e = e
        self.trace = trace
        self._error_handling_info = "Информацию об обработке ошибок можно почитать тут: "

    def handel_jira_502_error(self):
        """
        Alerts Telegram about a JIRA connection error and then tries to reconnect to JIRA.
        :return:
        """
        self.bot.send_sticker(self.config.TELEGRAM_GROUP_ID,
                         "CAACAgIAAxkBAAIIdWcEP0GuBPrRLuZkGt5gGmUSreK8AAKPVwACF6D4S8O6kooizCVCNgQ")

        self.bot.send_message(self.config.TELEGRAM_GROUP_ID,
                              text=f"<b>JIRA Error 502</b>\nЖира упала? В таком случае я починюсь, когда она отлипнет\n{self._error_handling_info}",
                              parse_mode="HTML")

        while True:
            try:
                jira = JIRA(server=self.config.JIRA_URL, basic_auth=self.config.basic_auth, timeout=self.config.JIRA_CONNECTION_TIMEOUT)
                self.bot.send_message(self.config.TELEGRAM_GROUP_ID,
                                      text="<b>JIRA Error 502</b>\n resolved",
                                      parse_mode="HTML")
                break
            except Exception as e:
                print(e)
                time.sleep(10)
        time.sleep(self.config.ERROR_RESOLVING_TIMEOUT)


    def handel_unexpected_error(self):
        """
        Alerts Console about a unknown error and then tries to reconnect to JIRA and Telegram.
        :return:
        """
        self.bot.send_message(self.config.TELEGRAM_GROUP_ID,
                              text=f"{str(self.e)[:300]}\nПроизошла непредвиденная ошибка, но я все еще пытаюсь подключиться\n{self._error_handling_info}")

        while True:
            try:
                jira = JIRA(server=self.config.JIRA_URL, basic_auth=self.config.basic_auth,
                            timeout=self.config.JIRA_CONNECTION_TIMEOUT)
                bot = telebot.TeleBot(self.config.BOT_TOKEN)
                bot.send_message(self.config.TELEGRAM_GROUP_ID,
                                      text=f"<b>{self.e}</b>\n resolved!",
                                      parse_mode="HTML")
                break
            except Exception as e:
                print(e)
                time.sleep(self.config.ERROR_RESOLVING_TIMEOUT)

    @staticmethod
    def save_error_log(e, trace):
        """
        saves error into ./%Y_%m_%d %H.log
        :param e: error
        :param trace: error traceback
        :return:
        """
        with open(f"app_logs/{datetime.datetime.now().strftime('%Y_%m_%d %H')}.log", "a") as f:
            f.write(f"{datetime.datetime.now().strftime('%Y_%m_%d %H %M %S')}\n")
            f.write(str(e)+"\n\n" + str(trace)+"\n\n")


# метод, который можно вешать на другие методы как wrapper для добавление обработки ошибок
def handle_errors(func):
    """
    wrapper method to handle any error
    :param func:
    :return:
    """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except JIRAError as e:
            trace = traceback.format_exc()
            error_handler = ErrorHandler(e, trace, config)
            error_handler.save_error_log(e, trace)

            if e.status_code == 502:
                error_handler.handel_jira_502_error()
            else:
                error_handler.handel_unexpected_error()

        except ApiException as e:
            test_telegram_bot()

        except Exception as e:
            trace = traceback.format_exc()
            error_handler = ErrorHandler(e, trace, config)
            error_handler.save_error_log(e, trace)
            error_handler.handel_unexpected_error()

        finally:
            pass

    return wrapper


def test_telegram_bot():
    """
    tests Telegram bot connection
    :return:
    """
    while True:
        try:
            bot = telebot.TeleBot(config.BOT_TOKEN)
            bot.send_message(config.TELEGRAM_GROUP_ID,
                                  text=f"Подключение к телеграмм восстановлено\nИнформацию об обработке ошибок можно почитать тут: ")
            break
        except Exception as e:
            trace = traceback.format_exc()
            error_handler = ErrorHandler(e, trace, config)
            error_handler.save_error_log(e, trace)
            print(f"{e}\n\n{trace}")
            time.sleep(config.ERROR_RESOLVING_TIMEOUT)