import time

from jira import JIRA


class JiraBot:
    """
    method: get_open_tickets

    self.jira: JIRA class entity

    self.config: config entity

    """
    def __init__(self, config):

        self.jira = JIRA(server=config.JIRA_URL, basic_auth=config.basic_auth, timeout=config.JIRA_CONNECTION_TIMEOUT)
        self.config = config

    def get_open_tickets(self):
        """
        search for open tickets in Jira
        :return:
        """
        issues = []
        issues = self.jira.search_issues(self.config.JIRA_QUERY['open'], maxResults=False)
        time.sleep(1)
        works = {}
        works["approaching_works"] = self.jira.search_issues(self.config.JIRA_QUERY['works'], maxResults=False)
        time.sleep(1)
        works["upcoming_works"] = self.jira.search_issues(self.config.JIRA_QUERY['works'], maxResults=False)
        return issues, works



