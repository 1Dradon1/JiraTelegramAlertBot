import time
from jira import JIRA


class JiraBot:
    def __init__(self, config):
        self.jira = JIRA(server=config.JIRA_URL, basic_auth=config.basic_auth)
        self.config = config


    def get_open_tickets(self):
        issues = self.jira.search_issues(self.config.JIRA_QUERY['open'], maxResults=False)
        time.sleep(1)
        works = {}
        works["approaching_works"] = self.jira.search_issues(self.config.JIRA_QUERY['approaching_works'], maxResults=False)
        time.sleep(1)
        works["upcoming_works"] = self.jira.search_issues(self.config.JIRA_QUERY['upcoming_works'], maxResults=False)
        return issues, works