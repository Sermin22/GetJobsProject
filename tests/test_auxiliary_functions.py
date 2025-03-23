import json
from unittest import mock
from unittest.mock import patch, mock_open
import pytest
from src.auxiliary_functions import read_json, save_to_json, get_salary_range, job_filtering


def test_read_json():
    '''Тестирование на вход путь до JSON-файла и возвращает список словарей с данными о вакансиях'''

    # Создаем мок для файла
    mocked_open = mock_open(read_data='[{"name_vacancy": "Вакансия 1", "area": "Москва", '
                                      '"salary_from": 50000, "salary_to": 60000}]')

    # Используем patch для замены вызова open
    with patch('builtins.open', mocked_open):
        # Здесь вызывай свою функцию, которая читает JSON-файл
        result = read_json("../data/saver.json")
        assert result == [{"name_vacancy": "Вакансия 1", "area": "Москва", "salary_from": 50000,
                           "salary_to": 60000}]


def test_read_json_not_found_file():
    '''Тестирование на вход если файл не найден, то возвращает пустой список'''

    # Создаем мок для файла
    mocked_open = mock_open(read_data=None)

    # Используем patch для замены вызова open
    with patch('builtins.open', mocked_open):
        # Здесь вызывай свою функцию, которая читает JSON-файл
        result = read_json("../data/saver.json")
        assert result == []


def test_read_json_empty_file():
    '''Тестирование на вход если файл пустой, то возвращает пустой список'''

    # Создаем мок для файла
    mocked_open = mock_open(read_data='')

    # Используем patch для замены вызова open
    with patch('builtins.open', mocked_open):
        # Здесь вызывай свою функцию, которая читает JSON-файл
        result = read_json("../data/saver.json")
        assert result == []


def test_read_json_error():
    '''Тестирование на вход путь до JSON-файла и если JSON-строка имеет неправильный формат,
    содержит некорректные символы или имеет другие ошибки и невозможно декорировать, то обрабатывает
    исключение и возвращает пустой список'''

    # Создаем мок для файла
    mocked_open = mock_open(read_data='[{"name_vacancy": "Вакансия 1", "area": "Москва", '
                                      '"salary_from": 50000, "salary_to": 60000}')

    # Используем patch для замены вызова open
    with patch('builtins.open', mocked_open):
        # Здесь вызывай свою функцию, которая читает JSON-файл
        result = read_json("../data/saver.json")
        assert result == []


def test_save_to_json_success():
    """Тест на успешное выполнение функции, записывающей данные в JSON-файл"""

    # Данные для записи
    data = [{"name_vacancy": "Вакансия 1", "area": "Москва", "salary_from": 50000, "salary_to": 60000}]
    # Путь к файлу
    file_path = 'saver.json'

    # Патчинг функции open
    with patch('builtins.open', new_callable=mock_open()) as mock_file:
        # Патчинг функции json.dump
        with patch('src.auxiliary_functions.json.dump', wraps=json.dump) as mock_dump:
            # Вызываем функцию
            save_to_json(data, file_path)

            # Проверка вызова функции open
            mock_file.assert_called_once_with(file_path, 'w', encoding='UTF-8')
            # Получаем объект, возвращаемый методом __enter__()
            handle = mock_file().__enter__()

            # Проверка вызова функции json.dump
            mock_dump.assert_called_once_with(
                data,
                handle,
                ensure_ascii=False,
                indent=4
            )


def test_save_to_json_file_not_found(capsys):
    """Тест на обработку исключения функции, записывающей данные в JSON-файл, если файл не найден"""

    # Неправильный путь к файлу
    file_path = '/unknown_path/saver.json'

    # Симуляция ошибки FileNotFoundError
    with patch('builtins.open', side_effect=FileNotFoundError()):
        save_to_json([], file_path)
        message = capsys.readouterr()
        assert message.out.strip() == f"Путь '{file_path}' не найден."


def test_save_to_json_error(capsys):
    """Тест на обработку исключения функции, записывающей данные в JSON-файл, если файл не найден"""

    # Не указан путь к файлу
    file_path = None

    # Симуляция любой другой ошибки Exception
    with patch('builtins.open', side_effect=Exception()):
        try:
            save_to_json([], file_path)
        except Exception as e:
            # Проверка сообщения об ошибке внутри блока except
            message = capsys.readouterr()
            assert message.out.strip() == f"Неожиданная ошибка при сохранении данных: {e}"


@pytest.mark.parametrize(
    "input_value, expected_output",
    [
        ("100000-150000", (100000, 150000)),
        ("100000-", (100000, None)),
        ("-150000", (None, 150000)),
        ("100000", (100000, None)),  # Один аргумент считается минимальной зарплатой
        ("", (None, None)),          # Пустой ввод
        ("abc-def", (None, None)),   # Некорректные данные
        ("100000-abc", (100000, None)),  # Частично некорректные данные
        ("abc-150000", (None, 150000)),  # Частично некорректные данные
        (" ", (None, None)),           # Пробелы
        ("100000-200000-300000", (None, None)),  # Слишком много аргументов
    ]
)
def test_get_salary_range(input_value, expected_output):
    """
    Тестирует функцию get_salary_range, возвращающую введенный диапазон зарплат. При неправильном
    вводе или пропуске данных значения возвращаются как None.
     Тестируем с различными входными значениями.
    """

    with mock.patch('builtins.input', return_value=input_value):
        assert get_salary_range() == expected_output


@pytest.mark.parametrize(
    "input_value, expected",
    [
        ("Developer-Москва", ("developer", "москва")),
        ("Developer-", ("developer", None)),
        ("-Москва", (None, "москва")),
        ("Developer", ("developer", None)),  # Один аргумент считается минимальной зарплатой
        ("", (None, None)),          # Пустой ввод
        (" ", (None, None)),           # Пробелы
        ("Developer-Москва-300000", (None))  # Слишком много аргументов
    ]
)
def test_job_filtering(input_value, expected):
    """
    Тестирует функцию job_filtering, возвращающую от пользователя название вакансии и город (через дефис)
    для фильтрации вакансий. При неправильном вводе или пропуске данных значения возвращаются как None.
     Тестируем с различными входными значениями.
    """

    with mock.patch('builtins.input', return_value=input_value):
        assert job_filtering() == expected
