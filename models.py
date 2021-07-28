from typing import List
import uuid


class News:
    def __init__(self, theme: str, title: str,
                 brief: str, text: str, date: str):
        """ инициализация объектов
        :param theme: тема, к которой относится новость
        :param title: заголовок
        :param brief: краткое содержание
        :param text: основной текст новости
        :param date: дата опубликования"""
        self.id = uuid.uuid4()
        self.theme = theme
        self.title = title
        self.brief = brief
        self.text = text
        self.date = date

    def get_data(self):
        """ получение полных моделей
        :return: все данные о модели """
        model_dict = {'title': self.title, 'theme': self.theme,
                      'text': self.text}
        return model_dict

    def get_data_for_feed(self):
        """ получение короткие модели в ленту
        :return: короткие данные о модели"""
        short_model_dict = {'title': self.title, 'theme': self.theme,
                            'brief': self.brief}
        return short_model_dict


class NewsList:
    def __init__(self):
        self.content = []

    def add_content(self, converted_news: List[News]):
        if self.content:
            # проверка, не дублируются ли новости
            converted_news = list(filter(lambda x: x.date > self.content[-1].date, converted_news))
        self.content += converted_news

    def get_certain_category(self, category: List):
        """фильтрация получаемых новостей по категории(ям)
        :param category: список категорий(и), новости по которым нужно получить
        :return: отфильрованный по категории(ям) список новостей"""
        return list(filter(lambda x: x.theme in category, self.content))

