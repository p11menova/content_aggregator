from models.models import News, NewsList
from typing import List
from const import *
import requests
from bs4 import BeautifulSoup
import datetime as dt


def get_content() -> List:
    """ запрос получения исходных данных источнику
     :param filters: фильтры к запросу (например, за определенную дату)
     :return: данные из источников"""
    try:
        response = requests.get('https://lenta.ru/rss/')
    except requests.exceptions.RequestException as err:
        print(type(err))
    else:
        lenta_content = BeautifulSoup(response.text, "xml").find_all('item')
        return lenta_content


def convert_to_classes(news_from_source: List) -> List[News]:
    """ преобразование исходных данных в экземпляры класса
    :param news_from_source: данные, полученные из источников
    :return: список данных, конвертированных в экземпляры News"""
    converted_news = []

    for elem in news_from_source:
        try:
            format_from = "%a, %d %b %Y %H:%M:%S %z"
            format_to = "%a %d %b %Y %H:%M:%S"
            instance = News(theme=elem.find('category').getText(),
                            title=elem.find('title').getText(),
                            brief=elem.find('description').getText().strip(),
                            text=elem.find('description').getText().strip(),
                            date=dt.datetime.strptime(elem.find('pubDate').get_text(),
                                                 format_from).strftime(format_to))

            converted_news.append(instance)
        except AttributeError as err:
            print(err)

    return converted_news


myNewsList = NewsList()


def save_to_newslist(converted_news: List[News]):
    """ сохранение новостей в NewsList
     :param converted_news: новости, конвертированные в экземпляры News"""
    for instance in converted_news:
        instance.theme = ''.join([i for i in CATEGORIES if instance.theme in CATEGORIES[i]])
    myNewsList.add_content(converted_news)
    return None


def main():
    news_from_source = get_content()
    converted_news = convert_to_classes(news_from_source)
    save_to_newslist(converted_news)
    filtered_with_category_news = myNewsList.get_certain_category([])


if __name__ == '__main__':
    main()
