import pytest
from unittest.mock import patch, Mock
from src.headhunter_api import HeadHunterApi


@patch('requests.get')
def test_head_hunter_api_connect(mock_get):
    """Тест метода класса HeadHunterApi подключения к API hh.ru и проверки статус-кода ответа."""

    # Создаем Mock объект для имитации ответа API
    mock_response = Mock()
    mock_response.status_code = 200  # Устанавливаем статус-код успешного ответа
    mock_get.return_value = mock_response
    # Создание экземпляра класса для работы с API сайтов с вакансиями
    hh_api = HeadHunterApi()
    # Проверяем прошел ли запрос успешно
    result = hh_api.send_connect()
    assert result == 200


@patch('requests.get')
def test_head_hunter_api_connect_failed(mock_get):
    """Тест метода класса HeadHunterApi подключения к API hh.ru и когда запрос к API
    завершается с ошибкой."""

    # Создаем Mock объект для имитации ответа API
    mock_response = Mock()
    mock_response.status_code = 400  # Устанавливаем статус-код ошибки
    mock_get.return_value = mock_response
    # Создание экземпляра класса для работы с API сайтов с вакансиями
    hh_api = HeadHunterApi()
    with pytest.raises(Exception):
        assert hh_api.send_connect() == "Запрос не выполнен с кодом состояния: 400"


def response_json():
    return {"items": [{
        "name": "Python Developer",
        "area": {"name": "Москва"},
        "employer": {"name": "Компания А"},
        "snippet": {"requirement": "Опыт разработки от 3-х лет"},
        "salary": {"from": 110000, "to": 180000},
        "url": "https://api.hh.ru/vacancies/118000777?host=hh.ru"}]}


@patch('requests.get')
def test_get_vacancies(mock_get):
    """Тест метода класса HeadHunterApi подключения к API hh.ru и получения вакансий"""

    # Создаем Mock объект для имитации ответа API
    mock_response = Mock()
    mock_response.status_code = 200  # Устанавливаем статус-код успешного ответа
    mock_response.json.return_value = response_json()
    mock_get.return_value = mock_response

    expected = [{
        "name_vacancy": "Python Developer",
        "area": "Москва",
        "employer": "Компания А",
        "requirement": "Опыт разработки от 3-х лет",
        "salary_from": 110000,
        "salary_to": 180000,
        "url": "https://api.hh.ru/vacancies/118000777?host=hh.ru"
    }]
    # Создание экземпляра класса для работы с API сайтов с вакансиями
    hh_api = HeadHunterApi()
    result = hh_api.get_vacancies()
    assert result == expected
