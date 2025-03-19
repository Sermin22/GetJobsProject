import json
from src.json_saver import JSONSaver, Vacancy
from unittest.mock import patch, mock_open


def test_json_saver_init():
    """
    Тестируем метод __init__. Проверяем, что файл был загружен и данные сохранены в списке вакансий.
    """
    mock_data = [
        {"name_vacancy": "Вакансия 1", "area": "Москва", "salary_from": 50000, "salary_to": 60000},
        {"name_vacancy": "Вакансия 2", "area": "Санкт-Петербург", "salary_from": 70000, "salary_to": 80000}
    ]

    # Создание мок для open
    m = mock_open(read_data=json.dumps(mock_data))

    # Патчим функцию open
    with patch('builtins.open', m):
        saver = JSONSaver()

        # Проверка, что файл был загружен и данные находятся в атрибутах
        assert saver.vacancies_list == mock_data
        assert saver.file_name == 'saver.json'

        # Проверка, что файл был открыт в режиме чтения
        m.assert_called_once_with(saver.file_path, 'r', encoding='UTF-8')


@patch('src.json_saver.save_to_json')
def test_get_vacancy_no_filter(mock_save_to_json):
    """
    Тестируем метод get_vacancy без фильтров.
    Ожидаем, что вернутся все вакансии из файла.
    """
    mock_data = [
        {"name_vacancy": "Вакансия 1", "area": "Москва",
         "employer": "Компания А", "requirement": "Опыт х лет",
         "salary_from": 50000, "salary_to": 60000},
        {"name_vacancy": "Вакансия 2", "area": "Санкт-Петербург",
         "employer": "Компания Б", "requirement": "Опыт х лет",
         "salary_from": 70000, "salary_to": 80000}
    ]
    # Создание мок для open
    m = mock_open(read_data=json.dumps(mock_data))
    # Патчим функцию open
    with patch('builtins.open', m):
        saver_1 = JSONSaver()
        saver_1.get_vacancy()  # Выполняем метод без фильтров

        assert len(saver_1.vacancies_list) == 2
        assert saver_1.vacancies_list == mock_data
        # Проверяем, что save_to_json была вызвана с правильными аргументами
        mock_save_to_json.assert_called_once_with(saver_1.vacancies_list, saver_1.file_path)


@patch('src.json_saver.save_to_json')
def test_get_vacancy_filter(mock_save_to_json):
    """
    Тестируем метод get_vacancy с фильтрацией по области.
    Ожидаем, что вернётся только одна вакансия.
    """
    mock_data = [
        {"name_vacancy": "Вакансия 1", "area": "Москва",
         "employer": "Компания А", "requirement": "Опыт х лет",
         "salary_from": 50000, "salary_to": 60000},
        {"name_vacancy": "Вакансия 2", "area": "Санкт-Петербург",
         "employer": "Компания Б", "requirement": "Опыт х лет",
         "salary_from": 70000, "salary_to": 80000}
    ]

    # Создание мок для open
    m = mock_open(read_data=json.dumps(mock_data))
    # Патчим функцию open
    with patch('builtins.open', m):
        saver_2 = JSONSaver()
        saver_2.get_vacancy(name_vacancy="Вакансия 1", area="Москва")  # Выполняем метод с фильтром

        # Проверяем, что filtered_vacancies содержит правильную вакансию
        assert len(saver_2.vacancies_list) == 1
        assert saver_2.vacancies_list[0]["name_vacancy"] == "Вакансия 1"
        assert saver_2.vacancies_list[0]["area"] == "Москва"
        # Проверяем, что save_to_json была вызвана с правильными аргументами
        mock_save_to_json.assert_called_once_with(saver_2.vacancies_list, saver_2.file_path)


@patch('src.json_saver.save_to_json')
def test_add_vacancy(mock_save_to_json):
    """Тестируем добавление новой вакансии."""

    mock_data = [
        {"name_vacancy": "Вакансия 1", "area": "Москва", "employer": "Компания 1", "salary_from": 50000,
         "salary_to": 60000},
        {"name_vacancy": "Вакансия 2", "area": "Санкт-Петербург", "employer": "Компания 2", "salary_from": 70000,
         "salary_to": 80000}
    ]

    # Создаем новую вакансию
    new_vacancy = Vacancy("Python Developer", "Москва", "Кадровое агентство Candidate",
                          90000, 120000, 150000, "https://api.hh.ru/vacancies/")

    # Создание мок для open
    m = mock_open(read_data=json.dumps(mock_data))
    with patch('builtins.open', m):
        saver_3 = JSONSaver()
        saver_3.add_vacancy(new_vacancy)

        # Проверяем, что filtered_vacancies содержит правильную вакансию
        assert len(saver_3.vacancies_list) == 3
        assert saver_3.vacancies_list[-1]["name_vacancy"] == "Python Developer"
        assert saver_3.vacancies_list[-1]["area"] == "Москва"
        assert saver_3.vacancies_list[-1]["employer"] == "Кадровое агентство Candidate"

        # Проверяем, что save_to_json была вызвана с правильными аргументами
        mock_save_to_json.assert_called_once_with(saver_3.vacancies_list, saver_3.file_path)


@patch('src.json_saver.save_to_json')
def test_delete_vacancy(mock_save_to_json):
    """
    Тестируем удаление вакансии.
    """
    mock_data = [
        {"name_vacancy": "Вакансия 1", "area": "Москва",
         "employer": "Компания 1", "salary_from": 50000,
         "salary_to": 60000},
        {"name_vacancy": "Вакансия 2", "area": "Санкт-Петербург",
         "employer": "Компания 2", "salary_from": 70000,
         "salary_to": 80000}
    ]

    # Создание мок для open
    m = mock_open(read_data=json.dumps(mock_data))
    # Патчим функцию open
    with patch('builtins.open', m):
        saver_4 = JSONSaver()
        result = saver_4.delete_vacancy(name_vacancy="Вакансия 1", employer="Компания 1")

        assert result is True
        assert len(saver_4.vacancies_list) == 1
        mock_save_to_json.assert_called_once_with(saver_4.vacancies_list, saver_4.file_path)
