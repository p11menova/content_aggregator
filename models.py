"""описание моделей Новостей и НовостныхСписков"""

from typing import List
from pymongo import MongoClient
from const import *


class News:
    def __init__(self, theme: str, title: str,
                 brief: str, text: str, date: str):
        """ инициализация объектов
        :param theme: тема, к которой относится новость
        :param title: заголовок
        :param brief: краткое содержание
        :param text: основной текст новости
        :param date: дата опубликования"""
        self.theme = theme
        self.title = title
        self.brief = brief
        self.text = text
        self.date = date

    def get_data(self):
        """ получение полных моделей
        :return: все данные о модели """

        return {
            'title': self.title,
            'brief': self.brief,
            'theme': self.theme,
            'text': self.text,
            'date': self.date
        }

    def get_data_for_feed(self):
        """ получение короткие модели в ленту
        :return: короткие данные о модели"""

        return {
            'title': self.title,
            'theme': self.theme,
            'brief': self.brief,
            'date': self.date
        }

    def get_title(self):
        return {
            'title': self.title
        }


class DBWork:
    """ класс работы с БД """

    def __init__(self):
        """ Инит класса
        """
        self.client = MongoClient(DB_URL)
        self.db = self.client.get_database(DB_NAME)

        self.titles_field = self.db.NewsList.find({}, ({'_id': 0, 'title': 1}))

    def insert_one_doc(self, instanse: News):
        """
        одиночное добавление новости в бд
        :param instanse: одна новость экземпляра News"""
        if not self.check_if_in(instanse.get_title()):
            self.db.NewsList.insert_one(instanse.get_data())

    def insert_data(self, data: List[News]):
        """
        массовое добавление новостей в бд
        :param data: список новостей конвертированные в экземпляры News
        """
        data_for_insert = [news_instance.get_data() for news_instance in data
                                      if not self.check_if_in(news_instance.get_title())]
        if data_for_insert:
            self.db.NewsList.insert_many(data_for_insert)

    def check_if_in(self, instanse_title: dict):
        """
        проверка, нет ли новости в бд
        :param instanse_title: заголовок новости
        :return: правда/ложь, есть ли новость в бд
        """
        return True if instanse_title in self.titles_field else False

    def get_one_doc(self, collection_name: str, site_filter: dict):
        """
        одиночное получение новости из бд
        :param collection_name: имя коллекции
        :param site_filter: фильтр
        :return: одна новость по фильтру
        """
        return self.db.get_collection(collection_name).find_one(site_filter)

    def get_data(self, collection_name: str, site_filter=None):

        """
        массовое получение новостей из бд
        :param collection_name: имя коллекции
        :param site_filter: фильтр
        :return: несколько новостей по фильтру
        """
        return self.db.get_collection(collection_name).find(site_filter)

    def delete_one_doc(self, collection_name: str, site_filter: dict):
        """
        одиночное удаление новости из бд
        :param collection_name: имя коллекции
        :param site_filter: фильтр
        """
        self.db.get_collection(collection_name).delete_one(site_filter)

    def delete_data(self, collection_name: str, site_filter=None):
        """
        массовое удаление новостей из бд
        :param collection_name: имя коллекции
        :param site_filter: фильтр
        """
        site_filter = site_filter or {}
        self.db.get_collection(collection_name).delete_many(site_filter)

