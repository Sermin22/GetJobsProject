import requests
from abc import ABC, abstractmethod


class BaseClassAPI(ABC):
    """Абстрактный класс создания классов для работы с API"""

    @abstractmethod
    def _connect(self, *args, **kwargs):
        """Защищенный метод подключения к API hh.ru и проверки статус-кода ответа."""
        pass

    @abstractmethod
    def get_vacancies(self, *args, **kwargs):
        """Метод получения вакансий"""
        pass


class HeadHunterApi(BaseClassAPI):
    """Класс для работы с API HeadHunter, подключение к API и получение вакансий"""

    # Атрибуты экземпляра класса — приватные
    __url: str
    __params: dict
    __vacancies: list

    def __init__(self):
        self.__url = 'https://api.hh.ru/vacancies'
        self.__params = {'text': '', 'search_field': 'name', 'area': 113, 'period': 3,
                         'only_with_salary': True, 'per_page': 100, 'page': 0}
        self.__vacancies = []
        super().__init__()

    @property
    def url(self):
        return self.__url

    @property
    def params(self):
        return self.__params

    @property
    def vacancies(self):
        return self.__vacancies

    def _connect(self):
        """Метод подключения к API hh.ru и проверки статус-кода ответа."""
        response = requests.get(self.url)
        if response.status_code != 200:
            raise Exception(f"Запрос не выполнен с кодом состояния: {response.status_code}")
        return response.status_code

    @property
    def send_connect(self):
        return self._connect

    def get_vacancies(self, keyword=None):
        """Метод получает вакансии с возможностью поиска по ключевому слову и
        преобразует их, отбирая необходимые ключи со значениями"""

        # Получаем список вакансий
        self.params['text'] = keyword
        if self.send_connect:
            response = requests.get(self.url, params=self.params)
            data = response.json()['items']
            self.vacancies.extend(data)
            self.params['page'] += 1
        # return self.vacancies

        # Преобразуем список вакансий
        vacancies_result = []
        for vacancy in self.vacancies:
            vacancy_data = {
                'name_vacancy': vacancy['name'],
                'area': vacancy['area']['name'],
                'employer': vacancy['employer']['name'],
                'requirement': vacancy['snippet']['requirement'],
                'salary_from': vacancy['salary']['from'],  # if vacancy['salary']['from'] is not None else 0,
                'salary_to': vacancy['salary']['to'],  # if vacancy['salary']['to'] is not None else 0,
                'url': vacancy['url']
            }
            vacancies_result.append(vacancy_data)
        return vacancies_result


# if __name__ == "__main__":
#     # Создание экземпляра класса для работы с API сайтов с вакансиями
#     hh_api = HeadHunterApi()
#     # Проверяем прошел ли запрос успешно
#     hh_connect = hh_api.send_connect()
#     print(hh_connect)
#     # Получение вакансий с hh.ru
#     hh_vacancies = hh_api.get_vacancies("Python developer")
#
#     print(hh_vacancies)
#     print(type(hh_vacancies))
#     print(len(hh_vacancies))
