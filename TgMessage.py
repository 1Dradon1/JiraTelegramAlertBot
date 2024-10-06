class TgMessage:
    def __init__(self):
        self.text = ""
        self.markup_dict = {}

    def processing_markup(self, issue):
        self.text += f"<b>{issue.key}</b>: {issue.fields.summary}\n"
        link = f"{config.issue_link_pattern}/{issue.key}"
        self.markup_dict[f"{issue.key}"] = {"url": link}