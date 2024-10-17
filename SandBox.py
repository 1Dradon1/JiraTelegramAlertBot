# from flask import Flask, request
#
# app = Flask(__name__)
#
#
# @app.route('/rest/webhooks/NewWorks', methods=['POST'])
# def webhook():
#     data = request.json
#     print('Получен вебхук:', data)
#     return 'Вебхук принят', 200
#
# if __name__ == '__main__':
#     app.run(port=5000)
# import time
# import logging
# from JiraBot import JiraBot
# from configs.Config_Test import Config
#
# logging.basicConfig(level=logging.DEBUG)
# config = Config()
#
# jira = JiraBot(config)
# while True:
#     time.sleep(5)
#     print(str(jira.test_connection()))