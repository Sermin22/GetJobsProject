import json


def read_json(file_path: str) -> list[dict]:
    """Функция, которая читает json-файл"""

    data: list[dict] = []
    try:
        with open(file_path, "r", encoding="UTF-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        # Если файла не существует, создаем новый пустой список
        data = []
    except json.JSONDecodeError as e:  # Обрабатываем ошибку декодирования JSON
        print(f"Ошибка декодирования JSON: {e}")
    except Exception as e:  # Обрабатываем другие возможные исключения
        print(f"Ошибка чтения файла: {e}")
    return data


def save_to_json(data: list[dict], file_path: str) -> None:
    """Функция записывает данные в JSON-файл"""

    try:
        # Открываем файл и записываем данные
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    except FileNotFoundError:
        # Обработка ситуации, когда путь не существует
        print(f"Путь '{file_path}' не найден.")
        # Обработка любых непредвиденных ошибок
    except Exception as e:
        print(f"Неожиданная ошибка при сохранении данных: {e}")
    return None


def get_salary_range():
    """Функция, возвращающая введенный диапазон зарплат. При неправильном вводе или пропуске данных
    значения возвращаются как None"""

    salary_input = input("Введите диапазон зарплат через дефис, пример: 100000-150000: ")

    if not salary_input.strip():  # Проверка на пустой ввод
        return None, None

    salary_range = salary_input.split("-")

    if len(salary_range) == 1:
        try:
            salary_from = int(salary_range[0].strip())
            salary_to = None  # Максимальная зарплата остается неопределенной
            return salary_from, salary_to
        except ValueError:
            return None, None  # Возвращаем None, если нельзя преобразовать в число
    elif len(salary_range) == 2:
        try:
            salary_from = int(salary_range[0].strip()) if salary_range[0].strip() else None
            salary_to = int(salary_range[1].strip()) if salary_range[1].strip() else None
            return salary_from, salary_to
        except ValueError:
            return None, None  # Возвращаем None, если хотя бы одна часть не конвертируется в число
    else:
        return None, None  # Неправильный формат, возвращаем None


# if __name__ == "__main__":
#     import os
#     from datetime import datetime
#     from src.headhunter_api import HeadHunterApi
#
#     # Определение ключевого слова для получения вакансий
#     keyword = "Python developer"
#     # Создание экземпляра класса для работы с API сайтов с вакансиями
#     hh_api = HeadHunterApi()
#     # Получение вакансий с hh.ru с применением ключевого слова
#     hh_vacancies = hh_api.get_vacancies(keyword)
#     # Формируем название файла, включающего текущую дату и ключевое слово в названии
#     date_today = datetime.now().strftime("%Y_%m_%d")
#     file_name = f"{date_today}_{keyword.replace(' ', '_')}.json"
#     # Получаем абсолютный путь к корневой директории проекта
#     BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#     # Указываем путь к записи файла file_name_vacancies
#     file_name_path = os.path.join(BASE_DIR, "data", file_name)
#     # Получаем JSON-файл с нужным названием и указанной директории
#     save_to_json(hh_vacancies, file_name_path)
#
#     # Прочитаем записанный JSON-файл
#     path_json_file = os.path.join(BASE_DIR, "data", "2025_03_09_Python_developer.json")
#     print(read_json(path_json_file))
