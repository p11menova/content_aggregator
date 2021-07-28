"""константы: категории новостей"""


class NewsCategories:
    politics = 'Политика'
    science = 'Наука'
    media = 'СМИ'
    culture = 'Культура'
    activity = 'Активность'


CATEGORIES = {
    NewsCategories.politics: ('Бывший СССР', 'Россия', 'Мир', 'Экономика', 'Силовые структуры'),
    NewsCategories.science: 'Наука и техника',
    NewsCategories.media: ('Интернет и СМИ', 'Из жизни'),
    NewsCategories.culture: ('Культура', 'Ценности', 'Среда обитания'),
    NewsCategories.activity: ('Спорт', 'Путешествия')
}