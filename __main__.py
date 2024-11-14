from configs.Config_Test import Config
from JiraBot import JiraBot

from ErrorHandler import handle_errors
from AlertHandler import AlertHandler

import telebot
import threading
import time
import logging

# logging если не требуется детальная информация о работе приложения, достаточно режима WARNING
logger = logging.getLogger(__name__)
config = Config()

logging.basicConfig(filename='app_logs/app.log', level=logging.DEBUG)


@handle_errors
def main():
    bot = telebot.TeleBot(config.BOT_TOKEN)
    jira = JiraBot(config)

    while True:
        issues, works = jira.get_open_tickets()

        if issues:
            alert_thread = threading.Thread(target=AlertHandler.alert_issue_dadm, args=(issues, bot, config))
            alert_thread.start()

        if works["approaching_works"] or works["upcoming_works"]:
            alert_thread = threading.Thread(target=AlertHandler.alert_works_dadm, args=(works, bot, config))
            alert_thread.start()

        time.sleep(config.REFRESH_RATE)


if __name__ == '__main__':
    while True:
        main()




