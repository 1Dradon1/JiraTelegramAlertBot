import traceback

from configs.Config import Config
from JiraBot import JiraBot
from ErrorHandler import ErrorHandler
from Utils import Utils

import telebot
import threading
import time


config = Config()


def main():
    bot = telebot.TeleBot(config.BOT_TOKEN)
    jira = JiraBot(config)

    while True:
        # todo добавить таймаут на запрос и сообщать, если он случается
        tickets = jira.get_open_tickets()

        if tickets:
            alert_thread = threading.Thread(target=Utils.alert_dadm, args=(tickets, bot, config.issue_link_pattern, config))
            alert_thread.start()

        time.sleep(config.REFRESH_RATE)


if __name__ == '__main__':
    while True:
        try:
            main()

    # todo начать писать resolve
        except Exception as e:
            error_handler = ErrorHandler(e, traceback.format_exc())
            error_handler.save_error_log()

            if f"JiraError HTTP 502 url: {config.JIRA_URL}/rest/api/2/serverInfo" in str(e):
                error_handler.handel_jira_connection_error()
                continue

            else:
                error_handler.handel_unexpected_error()
                continue


