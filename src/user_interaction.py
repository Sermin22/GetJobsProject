import os
from headhunter_api import HeadHunterApi
from json_saver import JSONSaver
from src.auxiliary_functions import save_to_json, get_salary_range, job_filtering


def user_interaction():
    """Функция для взаимодействия с пользователем"""

    search_query = input("Введите поисковый запрос: ")
    # Создаем экземпляр класса для работы с API сайта с вакансиями HH.ru
    hh_api = HeadHunterApi()
    # Получение вакансий с hh.ru в формате JSON
    hh_vacancies = hh_api.get_vacancies(search_query)
    # Сортируем вакансии по убыванию значения salary_from (Зарплата ОТ)
    sorted_vacancies = sorted(hh_vacancies, key=lambda x: x['salary_from']
    if x['salary_from'] is not None else 0, reverse=True)
    try:
        # Получаем значение количества для вывода первых топ-вакансий по заплате
        top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    except ValueError:
        # Если пользователь ввел не число или оставил поле пустым, устанавливаем top_n равной длине списка
        top_n = len(sorted_vacancies)
    # Получаем нужные вакансии
    if top_n > len(sorted_vacancies):
        top_vacancies = sorted_vacancies
    else:
        top_vacancies = sorted_vacancies[:top_n]
    # Получаем абсолютный путь к корневой директории проекта
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Указываем путь к записи файла file_json
    file_path = os.path.join(BASE_DIR, "data", "saver.json")
    # Записываем JSON-файл с вакасиями
    save_to_json(top_vacancies, file_path)
    # Преобразуем вакансии как объект класса JSONSaver для дальнейшей работы с вакансиями
    top_vacancies_json_file = JSONSaver()
    # Получаем от пользователя название вакансии и город (через пробел) для фильтрации вакансий
    name_vacancy, area = job_filtering()
    # Получаем диапазон зарплат, например: 100000-150000 или None, если они введены неверно
    # или ввод пропущен.
    salary_from, salary_to = get_salary_range()
    # Получаем вакансии с ключевым словом в названии, города и диапазона зарплат
    top_vacancies_json_file.get_vacancy(name_vacancy, area, salary_from, salary_to)


if __name__ == "__main__":
    user_interaction()
