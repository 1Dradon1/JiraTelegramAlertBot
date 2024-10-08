class Config:
    JIRA_URL = 'http://172.23.180.57'
    JIRA_LOGIN = '<login>'
    JIRA_PASSWORD = '<password>'
    basic_auth = JIRA_LOGIN, JIRA_PASSWORD

    TELEGRAM_GROUP_ID = '<GROUP ID>'
    BOT_TOKEN = '<bot_token>' # токен бота в телеге

    JIRA_PROJECT_KEY = '<JIRA_project_key>'
    issue_link_pattern = f"{JIRA_URL}/projects/{JIRA_PROJECT_KEY}/issues" # линк на issue

    _works_delay = 13
    REFRESH_RATE = 180  # надо либо писать круглые минуты, либо добавить округление в формулу поиска ворксов

    JIRA_QUERY = {'open': 'project = INC AND (status = new OR status = Reopened)',
                  'far_upcoming_works': 'project in (WORKS, CWORKS, RPDWORKS) AND status = Confirmed AND '
                                        f'assignee in ("dadm@osmp.ru", dadmuser) and "Дата и время проведения работ" <= {_works_delay}m'
                                        f' and "Дата и время проведения работ" >= {_works_delay - (REFRESH_RATE / 60)}m',
                  'upcoming_works': 'project in (WORKS, CWORKS, RPDWORKS) AND status = Confirmed AND '
                                    f'assignee in ("dadm@osmp.ru", dadmuser) and "Дата и время проведения работ" <= {(REFRESH_RATE / 60)}m'
                                    f' and "Дата и время проведения работ" >= 0m',
                  'test': f"project={JIRA_PROJECT_KEY} AND status='To Do'"}

