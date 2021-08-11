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


class DBWork:
    """ класс работы с БД """

    client = MongoClient("mongodb+srv://p1menowa:Nr44Kvt!@firstcluster.l2dlg.mongodb.net/News?retryWrites=true&w=majority")
    db = client.get_database(DB_NAME)

    def insert_one_doc(self, data: dict):
        DBWork.db.NewsList.insert_one(data)

    def insert_data(self, data: List[News]):
        DBWork.db.NewsList.insert_many([news_instance.get_data() for news_instance in data])

    def get_one_doc(self, collection_name: str, filter: dict):
        return DBWork.db.get_collection(collection_name).find_one(filter)

    def get_data(self, collection_name: str, filter=None):
        # if filter:
        #     return DBWork.db.get_collection(collection_name).find(filter)
        return DBWork.db.get_collection(collection_name).find(filter)

    def delete_one_doc(self, collection_name:str, filter: dict):
        DBWork.db.NewsList.delete_one(filter)

    def delete_data(self, collection_name: str, filter=None):
        if filter is None:
            filter = {}
        DBWork.db.get_collection(collection_name).delete_many(filter)

