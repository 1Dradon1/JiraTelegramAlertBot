class Config:
    JIRA_URL = 'http://172.23.180.57'
    JIRA_LOGIN = '<login>'
    JIRA_PASSWORD = '<password>'
    basic_auth = JIRA_LOGIN, JIRA_PASSWORD

    TELEGRAM_GROUP_ID = '<GROUP ID>'
    BOT_TOKEN = '<bot_token>' # токен бота в телеге

    JIRA_PROJECT_KEY = '<JIRA_project_key>'

    issue_link_pattern = f"{JIRA_URL}/project/{JIRA_PROJECT_KEY}/issues" # линк на issue

