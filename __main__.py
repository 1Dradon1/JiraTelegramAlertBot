from Config import Config
from JiraBot import JiraBot
from TgMessage import TgMessage

import telebot
from telebot.util import quick_markup

import threading
import time

config = Config()




def main():
    bot = telebot.TeleBot(config.BOT_TOKEN)
    jira = JiraBot(config)

    while True:
        issues = jira.get_open_issues()

        if issues:
            alert_thread = threading.Thread(target=alert_dadm, args=(issues, bot))
            alert_thread.start()

        time.sleep(config.REFRESH_RATE)


def alert_dadm(issues, bot):
    message = TgMessage()
    for issue in issues:
        message.processing_markup(issue)

    print(bot.send_message(config.TELEGRAM_GROUP_ID, text=message.text, reply_markup=quick_markup(message.markup_dict),
                           parse_mode="HTML").json)
    del message


if __name__ == '__main__':
    main_thread = threading.Thread(target=main)
    main_thread.start()
