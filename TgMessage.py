class TgMessage:
    def __init__(self):
        self.text = ""
        self.markup_dict = {}

    def processing_markup(self, issue, issue_link_pattern):
        key = issue.key
        summary = issue.fields.summary

        self.text += f"<b>{key}</b>: {summary}\n"
        link = f"{issue_link_pattern}/{key}"
        self.markup_dict[f"{key}"] = {"url": link}