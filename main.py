from models.news_model import News, NewsList


def get_content(filters: list) -> list:
    """ work with requests """
    pass


def convert_to_classes(news_from_source: list) -> list:
    """ converting source content to News instances """
    pass


def save_to_newslist(news: list):
    """ saving news to newslist """
    NewsList.add_content(news)


def main():
    news_from_source = get_content(['filters'])
    news = convert_to_classes(news_from_source)
    save_to_newslist(news)


if __name__ == '__main__':
    main()
