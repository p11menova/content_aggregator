from models.models import News, DBWork
from typing import List
from const import *
import requests
from bs4 import BeautifulSoup
from helpers import convert_to_correct_format


def get_content() -> List:
    """ запрос получения исходных данных источнику
     :return: данные из источников """
    lenta_content = []
    try:
        response = requests.get('https://lenta.ru/rss/')
        lenta_content = BeautifulSoup(response.text, "xml").find_all('item')
    except requests.exceptions.RequestException as err:
        print(type(err))
    return lenta_content


def convert_to_classes(news_from_source: List) -> List[News]:
    """ преобразование исходных данных в экземпляры класса
    :param news_from_source: данные, полученные из источников
    :return: список данных, конвертированных в экземпляры News """
    converted_news = []

    for elem in news_from_source:
        try:
            instance = News(theme=define_my_category(elem.find('category').getText()),
                            title=elem.find('title').getText(),
                            brief=elem.find('description').getText().strip(),
                            text=elem.find('description').getText().strip(),
                            date=convert_to_correct_format(elem.find('pubDate').get_text()))

            converted_news.append(instance)

        except AttributeError as err:
            print(err)
    return converted_news


def define_my_category(elem_category: str):
    """ распределение исходных данных по моим категориям """
    return ([k for k, v in CATEGORIES.items() if elem_category in v] or
                      [NewsCategories.other])[0]


dbw1 = DBWork()


def main():
    news_from_source = get_content()
    converted_news = convert_to_classes(news_from_source)

    dbw1.insert_data(converted_news)
    #dbw1.delete_data(COLLECTION_NAME)
    print([a for a in dbw1.get_data(COLLECTION_NAME, filter={'theme': 'СМИ'})])


if __name__ == '__main__':
    main()
