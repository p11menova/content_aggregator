"""константы"""


class NewsCategories:
    politics = 'Политика'
    science = 'Наука'
    media = 'СМИ'
    culture = 'Культура'
    activity = 'Активность'
    other = ''


CATEGORIES = {
    NewsCategories.politics: ('Бывший СССР', 'Россия', 'Мир', 'Экономика', 'Силовые структуры'),
    NewsCategories.science: ('Наука и техника'),
    NewsCategories.media: ('Интернет и СМИ', 'Из жизни'),
    NewsCategories.culture: ('Культура', 'Ценности', 'Среда обитания'),
    NewsCategories.activity: ('Спорт', 'Путешествия')
}


DB_NAME = 'News'
COLLECTION_NAME = 'NewsList'

FORMAT_FROM = "%a, %d %b %Y %H:%M:%S %z"
FORMAT_TO = "%a %d %b %Y %H:%M:%S"

