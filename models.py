import datetime
import json
from typing import List


class News:
    def __init__(self, theme: str, title: str,
                 brief: str, text: str):
        """ инициализация объектов
        :param theme: тема, к которой относится новость
        :param title: заголовок
        :param brief: краткое содержание
        :param text: основной текст новости """
        self.theme = theme
        self.title = title
        self.brief = brief
        self.text = text
        self.date = datetime.datetime.now()

    def get_data(self):
        """ получение полных моделей
        :return: все данные о модели """
        model_dict = {'title': self.title, 'theme': self.theme,
                      'text': self.text}
        return json.dumps(model_dict)

    def get_data_for_feed(self):
        """ получение короткие модели в ленту
        :return: короткие данные о модели"""
        short_model_dict = {'title': self.title, 'theme': self.theme,
                            'brief': self.brief}
        return json.dumps(short_model_dict)


class NewsList:
    def __init__(self):
        self.content = []

    def add_content(self, converted_news: List[News]):
        self.content += converted_news
