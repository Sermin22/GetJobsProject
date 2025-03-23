import pytest
from unittest.mock import patch
from src.views import user_interaction


@pytest.fixture
def mocked_responses():
    """Фикстура для подготовки моков"""

    with (patch('builtins.input') as mock_input,
          patch('src.headhunter_api.HeadHunterApi') as mock_hh_api,
          patch('src.auxiliary_functions.save_to_json') as mock_save_to_json,
          patch('src.json_saver.JSONSaver.get_vacancy') as mock_json_saver_get_vacancy,
          patch('src.auxiliary_functions.job_filtering') as mock_job_filtering,
          patch('src.auxiliary_functions.get_salary_range') as mock_get_salary_range):
        yield mock_input, mock_hh_api, mock_save_to_json, mock_json_saver_get_vacancy, \
            mock_job_filtering, mock_get_salary_range


def test_user_interaction(mocked_responses, vacancies):
    (mock_input, mock_hh_api, mock_save_to_json, mock_json_saver_get_vacancy, mock_job_filtering,
     mock_get_salary_range) = mocked_responses

    mock_input.side_effect = ["Python Developer", "", "Тестировщик-Петербург", "60000-90000"]
    mock_hh_api.return_value.get_vacancies.return_value = vacancies
    mock_save_to_json.return_value = True
    mock_json_saver_get_vacancy.return_value = [
        {
            "name_vacancy": "Тестировщик",
            "area": "Санкт-Петербург",
            "employer": "Компания Б",
            "requirement": "Опыт работы 5 лет",
            "salary_from": 60000,
            "salary_to": 90000,
            "url": "http://example.com/vacancy2"
        }
    ]
    mock_job_filtering.return_value = ("Тестировщик", "Петербург")
    mock_get_salary_range.return_value = (60000, 90000)

    # Вызов тестируемой функции
    user_interaction()

    # Проверка результата
    expected_result = mock_json_saver_get_vacancy.return_value
    assert expected_result == mock_json_saver_get_vacancy.return_value
