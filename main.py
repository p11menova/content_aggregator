from models.models import News, NewsList
from typing import List
import requests
from bs4 import BeautifulSoup


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
    try:
        for elem in news_from_source:
            instance = News(elem.find('category').getText(),
                            elem.find('title').getText(),
                            elem.find('description').getText().strip(),
                            elem.find('description').getText().strip())
            converted_news.append(instance)
        return converted_news
    except AttributeError as err:
        print(err)


def save_to_newslist(converted_news: List[News]):
    """ сохранение новостей в NewsList
     :param converted_news: новости, конвертированные в экземпляры News"""
    NewsList.add_content(converted_news)


def main():
    news_from_source = get_content()
    converted_news = convert_to_classes(news_from_source)
    #save_to_newslist(converted_news)


if __name__ == '__main__':
    #get_content()
    main()
