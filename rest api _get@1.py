"""

Обращаемся к API сайта "https://api.chucknorris.io"
получаем случайную фразу "Чак Нориса" на английском языке,
после полученую  фразу передаем параметром в API Яндекс переводчик и получаем переведеную фразу.

"""
import requests
import json


class Phrase:

    def __init__(self):
        # Получаем url and key для яндекс переводчика.
        with open('url_key.json')as info:
            self.data = json.load(info)

        # Получаем фразу "Чак Нориса"
        self.phrase()

    def phrase(self):
        answer = requests.get('https://api.chucknorris.io/jokes/random')
        if answer.status_code == 200:
            # Передаем в яндекс переводчик параметры.
            # Поумолчанию мы используем перевод(с Английского языка на Русский язык )
            language = 'en_ru'
            # Параметры : 1-Текст ,2-Язык перевода.
            self.yandex_api(answer.json()['value'], language)
        else:
            print('Ошибка')

    def yandex_api(self, my_text, language):
        # Передаем в качестве параметра полученую фразу и получаем её перевод.
        params = {
            "key": self.data['key'],
            "text": my_text,
            "lang": language  # Здесь мы указываем с какого языка на какой мы делаем переводим
        }

        self.response = requests.get(self.data['URL'], params=params)
        self.answer = self.response.json()
        if self.response.status_code == 200:
            print(''.join(self.answer['text']))
        else:
            print(''.join(self.answer['message']))


if __name__ == '__main__':
    Phrase()


