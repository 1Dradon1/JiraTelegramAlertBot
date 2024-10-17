import traceback

from jira import JIRAError

from configs.Config_Test import Config
from JiraBot import JiraBot
from ErrorHandler import ErrorHandler
from AlertHandler import AlertHandler

import telebot
import threading
import time


config = Config()


def main():
    bot = telebot.TeleBot(config.BOT_TOKEN)
    jira = JiraBot(config)

    while True:
        # todo добавить таймаут на запрос и сообщать, если он случается
        issues, works = jira.get_open_tickets()

        if issues:
            alert_thread = threading.Thread(target=AlertHandler.alert_issue_dadm, args=(issues, bot, config))
            alert_thread.start()

        if works:
            alert_thread = threading.Thread(target=AlertHandler.alert_works_dadm, args=(works, bot, config))
            alert_thread.start()

        time.sleep(config.REFRESH_RATE)


if __name__ == '__main__':
    while True:
        try:
            main()

    # todo начать писать resolve
        except JIRAError as e:
            if e.status_code == 502:
                error_handler = ErrorHandler(e, traceback.format_exc(), config)
                error_handler.handel_jira_connection_error()


        except Exception as e:
            error_handler = ErrorHandler(e, traceback.format_exc(), config)
            error_handler.save_error_log()
            error_handler.handel_unexpected_error()
            continue


