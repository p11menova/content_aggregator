import datetime


class News:
    def __init__(self, theme, title, brief, content):
        self.theme = theme
        self.title = title,
        self.brief = brief
        self.content = content
        self.date = datetime.datetime.now()



class NewsList:
    def __init__(self):
        self.content = []

    def add_content(self, news):
        self.content.append(news)