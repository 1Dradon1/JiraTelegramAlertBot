import time
import datetime
import telebot


class ErrorHandler:
    def __init__(self, e, trace, config):
        self.config = config
        self.bot = telebot.TeleBot(self.config.BOT_TOKEN)
        self.e = e
        self.trace = trace


    def handel_jira_connection_error(self):
        self.bot.send_sticker(self.config.TELEGRAM_GROUP_ID,
                         "CAACAgIAAxkBAAIIdWcEP0GuBPrRLuZkGt5gGmUSreK8AAKPVwACF6D4S8O6kooizCVCNgQ")

        self.bot.send_message(self.config.TELEGRAM_GROUP_ID,
                         text="<b>JIRA Error 502</b>\nIs JIRA down? In this case exception will resolve after it'll up",
                         parse_mode="HTML")

        time.sleep(self.config.REFRESH_RATE)


    def handel_unexpected_error(self):
        self.bot.send_message(self.config.TELEGRAM_GROUP_ID,
                         text=str(self.e)[:100] + f"\n error occurrenced, but i'll still trying to connect")

        time.sleep(self.config.REFRESH_RATE)


    def save_error_log(self):
        with open(f"{datetime.datetime.now().strftime('%Y_%m_%d %H_%M_%S')}.log", "a") as f:

            f.write(str(self.e)+"\n\n" + str(self.trace)+"\n\n")

