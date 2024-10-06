import time
from symtable import Class


import requests
from jira import JIRA
from Config import Config


class JiraBot:
    def __init__(self, config):
        self.jira = JIRA(server=config.JIRA_URL, basic_auth=config.basic_auth)
        self.config = config


    def get_open_tickets(self):
        issues = self.jira.search_issues(Config.JIRA_QUERY['test'], maxResults=False)
        time.sleep(1)
        works = self.jira.search_issues(Config.JIRA_QUERY['test'], maxResults=False)

        return issues + works

    def get_approaching_works(self):
        works = self.jira.search_issues(Config.JIRA_QUERY['test'], maxResults=False)