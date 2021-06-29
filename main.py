from models.news_model import News, NewsList


def get_content():
    #work with requests
    return ['newsfromsource']


def transformate_into_classes(news_from_source):
    news = [News() for i in news_from_source]
    return news


def save_into_newslist(news):
    NewsList.add_content(news)

def main():
    news_from_source = get_content('filters')
    news = transformate_into_classes(news_from_source)
    save_into_newslist(news)

if __name__ == '__main__':
    main()


