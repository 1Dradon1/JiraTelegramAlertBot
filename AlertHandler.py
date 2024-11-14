from telebot.util import quick_markup
import threading

from TgMessage import TgMessage


class AlertHandler:

    @staticmethod
    def alert_issue_dadm(issues, bot, config):
        """
        Уведомляет о всех issue из переданного списка
        :param issues: массив issue библиотеки JIRA
        :param bot: telegram bot
        :param config:
        :return: none
        """
        message = TgMessage()
        for issue in issues:
            message.append_ticket(issue, config.issues_link_pattern)

        print(bot.send_message(config.TELEGRAM_GROUP_ID, text=message.text,
                               reply_markup=quick_markup(message.markup_dict),
                               parse_mode='HTML').json)
        del message



    @staticmethod
    def alert_works_dadm(works, bot, config):
        """
        approaching_works: Через {config.works_delay} мин
        upcoming_works: начнется через 0-3 мин
        уведомляет о issue как о WORKS, расчитанно именно на тикеты WORKS
        :param works: {"approaching_works": issue JIRA, "upcoming_works": issue JIRA}
        :param bot: telegram bot
        :param config:
        :return: none
        """
        message = TgMessage()

        if works["approaching_works"]:
            message.text += f"Через {config.works_delay} мин: \n"

            for work in works["approaching_works"]:
                message.append_ticket(work, config.issues_link_pattern)

        if works["upcoming_works"]:
            message.text += "Скоро начнется: \n"
            for work in works["upcoming_works"]:
                message.append_ticket(work, config.issues_link_pattern)

        print(bot.send_message(config.TELEGRAM_GROUP_ID, text=message.text,
                               reply_markup=quick_markup(message.markup_dict),
                               parse_mode='HTML').json)

        del message


    @staticmethod
    def start_alert_thread(target_func, items, bot, config):
        """
        Создает и запускает поток для передачи уведомлений
        :param target_func: alert_issue_dadm \ alert_works_dadm
        :param items: issues \ works
        :param bot: telegram bot
        :param config:
        :return: none
        """
        if items:
            alert_thread = threading.Thread(target=target_func, args=(items, bot, config))
            alert_thread.start()