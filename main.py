from models.models import News, NewsList
from typing import List
from const import *
import requests
from bs4 import BeautifulSoup
from helpers import convert_to_correct_format


def get_content() -> List:
    """ запрос получения исходных данных источнику
     :return: данные из источников"""
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
    :return: список данных, конвертированных в экземпляры News"""
    converted_news = []

    for elem in news_from_source:
        try:
            instance = News(theme=elem.find('category').getText(),
                            title=elem.find('title').getText(),
                            brief=elem.find('description').getText().strip(),
                            text=elem.find('description').getText().strip(),
                            date=convert_to_correct_format(elem.find('pubDate').get_text()))

            converted_news.append(instance)

        except AttributeError as err:
            print(err)
    return converted_news


myNewsList = NewsList()


def save_to_newslist(converted_news: List[News]):
    """ сохранение новостей в NewsList
     :param converted_news: новости, конвертированные в экземпляры News"""
    for instance in converted_news:
        instance.theme = ([k for k, v in CATEGORIES.items() if instance.theme in v] or
                          [NewsCategories.other])[0]
        myNewsList.add_content(converted_news)


def main():
    news_from_source = get_content()
    converted_news = convert_to_classes(news_from_source)
    save_to_newslist(converted_news)
    filtered_with_category_news = myNewsList.get_certain_category(['Политика'])


if __name__ == '__main__':
    main()
