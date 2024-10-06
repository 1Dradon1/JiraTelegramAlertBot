from symtable import Class
import requests
from jira import JIRA
from Config import Config


class JiraBot:
    def __init__(self, config):
        self.jira = JIRA(server=config.JIRA_URL, basic_auth=config.basic_auth)
        self.config = config


    def get_open_issues(self):
        issues = self.jira.search_issues(f"project={self.config.PROJECT_KEY} AND status='To Do'", maxResults=False)
        return issues




