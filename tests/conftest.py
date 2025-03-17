import pytest
from src.vacancy import Vacancy


@pytest.fixture
def vacancy():
    return Vacancy("Python Developer", "Москва", "Кадровое агентство Candidate",
                   "Опыт разработкиот 3-х лет", 110000, 180000,
                   "https://api.hh.ru/vacancies/118000777?host=hh.ru")

@pytest.fixture
def vacancy_2():
    return Vacancy("Python Developer", "Краснодар", "Кадровое агентство Candidate",
                   "Опыт разработкиот 5-ти лет", 150000, 210000,
                   "https://api.hh.ru/vacancies/118000888?host=hh.ru")

@pytest.fixture
def vacancies():
    return [
    {
        "name_vacancy": "Python Developer",
        "area": "Москва",
        "employer": "Компания А",
        "requirement": "Опыт разработки от 3-х лет",
        "salary_from": 110000,
        "salary_to": 180000,
        "url": "https://api.hh.ru/vacancies/118000777?host=hh.ru"
    },
    {
        "name_vacancy": "Тестировщик",
        "area": "Санкт-Петербург",
        "employer": "Компания Б",
        "requirement": "Опыт работы 5 лет",
        "salary_from": 60000,
        "salary_to": 90000,
        "url": "http://example.com/vacancy2"
    },
    {
        "name_vacancy": "Middle Python developer",
        "area": "Санкт-Петербург",
        "employer": "Компания В",
        "requirement": "Писать код бизнес-процессов",
        "salary_from": 120000,
        "salary_to": 150000,
        "url": "https://api.hh.ru/vacancies/117628372?host=hh.ru"
    }
]

@pytest.fixture
def response_json():
    return {
        "name_vacancy": "Python Developer",
        "area": "Москва",
        "employer": "Компания А",
        "requirement": "Опыт разработки от 3-х лет",
        "salary_from": 110000,
        "salary_to": 180000,
        "url": "https://api.hh.ru/vacancies/118000777?host=hh.ru"
    }