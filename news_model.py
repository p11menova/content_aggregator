import datetime


class News:
    def __init__(self, theme: str, title: str,
                 brief: str, content: tuple):
        self.theme = theme
        self.title = title
        self.brief = brief
        self.content = content  # content = text, image(s)
        self.date = datetime.datetime.now()


class NewsList:
    def __init__(self):
        self.content = []

    def add_content(self, news: list):
        self.content += news
