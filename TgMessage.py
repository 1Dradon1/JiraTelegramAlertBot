class TgMessage:
    def __init__(self):
        self.text = ""
        self.markup_dict = {}

    def append_ticket(self, issue, issue_link_pattern):
        """
        appends ticket title and link to TgMessage
        :param issue: JIRA ticket
        :param issue_link_pattern: config var
        :return: 
        """
        key = issue.key
        summary = issue.fields.summary

        self.text += f"<b>{key}</b>: {summary}\n"
        link = f"{issue_link_pattern}/{key}"
        self.markup_dict[f"{key}"] = {"url": link}