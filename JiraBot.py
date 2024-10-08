import time
from jira import JIRA


class JiraBot:
    def __init__(self, config):
        self.jira = JIRA(server=config.JIRA_URL, basic_auth=config.basic_auth)
        self.config = config


    def get_open_tickets(self):
        issues = self.jira.search_issues(self.config.JIRA_QUERY['open'], maxResults=False)
        time.sleep(1)
        works = []
        # works = self.jira.search_issues(Config.JIRA_QUERY['upcoming_works'], maxResults=False)
        return issues + works

    def get_approaching_works(self):
        works = self.jira.search_issues(self.config.JIRA_QUERY['test'], maxResults=False)