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
        tickets = jira.get_open_tickets()

        if tickets:
            alert_thread = threading.Thread(target=alert_dadm, args=(tickets, bot))
            alert_thread.start()

        time.sleep(config.REFRESH_RATE)


def alert_dadm(tickets, bot):
    message = TgMessage()
    for ticket in tickets:
        message.processing_markup(ticket, config.issue_link_pattern)

    print(bot.send_message(config.TELEGRAM_GROUP_ID, text=message.text, reply_markup=quick_markup(message.markup_dict),
                           parse_mode="HTML").json)
    del message


if __name__ == '__main__':
    main_thread = threading.Thread(target=main)
    main_thread.start()
