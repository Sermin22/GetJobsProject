import os
from abc import ABC, abstractmethod
from src.auxiliary_functions import read_json, save_to_json
from src.vacancy import Vacancy


class BaseJSONSaver(ABC):
    """Абстрактный класс для работы с файлами"""

    @abstractmethod
    def get_vacancy(self, *args, **kwargs):
        """Метод получения вакансий из файла"""
        pass

    @abstractmethod
    def add_vacancy(self, *args, **kwargs):
        """Метод добавляет вакансию в JSON-файл список вакансий, если такой вакансии ещё нет.
        Параметр vacancy - объект вакансии типа Vacancy, метод возвращает обновленный
        список вакансий"""
        pass

    @abstractmethod
    def delete_vacancy(self, *args, **kwargs):
        """Удаляет вакансию из JSON-файл списка вакансий по названию вакансии и работодателю.
        Возвращает True, если вакансия была успешно удалена, иначе False"""


class JSONSaver(BaseJSONSaver):
    """Класс для сохранения информации о вакансиях в JSON-файл, добавления новых вакансий
        в файл, удаление вакансий и получение данных из файла по указанным критериям"""

    def __init__(self, file_name="saver.json"):

        self.__file_name = file_name
        self.vacancies_list = []
        super().__init__()

        # Получаем абсолютный путь к корневой директории проекта
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        # Указываем путь к записи файла file_name_vacancies
        file_path = os.path.join(BASE_DIR, "data", self.__file_name)
        self.file_path = file_path

    @property
    def file_name(self):
        return self.__file_name

    @file_name.setter
    def file_name(self, filename):
        self.__file_name = filename

    def get_vacancy(self, name_vacancy=None, area=None, salary_from=None, salary_to=None):
        """Метод получения вакансий из файла по указанным критериям"""

        data = read_json(self.file_path)
        self.vacancies_list.extend(data)  # Добавляем данные из файла в список

        filtered_vacancies = []
        for vacancy in self.vacancies_list:
            # Фильтр по названию вакансии
            if name_vacancy is not None and name_vacancy.lower() not in vacancy.get("name_vacancy").lower():
                continue
            # Фильтр по области
            if area is not None and area.lower() not in vacancy.get("area").lower():
                continue

            # Фильтр по минимальной и максимальной зарплате, присутствуют ключи словаря (ОТ и ДО) "salary_from"
            # и "salary_to". Если хотя бы одного из них нет, элемент пропускается.
            # if (salary_from is not None or salary_to is not None) and \
            #         ("salary_from" not in vacancy or "salary_to" not in vacancy):
            #     continue

            # Фильтр только по минимальной зарплате только (ОТ), работает с ключом словаря "salary_from".
            # Если минимальной зарплаты нет, элемент пропускается. Зарплату фильтруем по минимальной ставке.
            if salary_from is not None and "salary_from" not in vacancy:
                continue
            # Сравниваем минимальную зарплату(ОТ) с salary_from и с salary_to: если она меньше или больше
            # указанного значения, то пропускается.
            if salary_from is not None and vacancy["salary_from"] < salary_from:
                continue
            if salary_from is not None and vacancy["salary_from"] > salary_to:
                continue

            # Фильтрация по зарплате ОТ и ДО в словаре:
            # if salary_from is not None and vacancy["salary_from"] < salary_from:
            #     continue
            # if salary_to is not None and vacancy["salary_to"] > salary_to:
            #     continue
            filtered_vacancies.append(vacancy)

        # Получаем абсолютный путь к корневой директории проекта
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # Указываем путь к записи файла
        file_path = os.path.join(BASE_DIR, "data", "filtered_file.json")
        save_to_json(filtered_vacancies, file_path)


    def add_vacancy(self, vacancy: Vacancy):
        """Метод добавляет вакансию в JSON-файл список вакансий, если такой вакансии ещё нет.
        Параметр vacancy - объект вакансии типа Vacancy, метод возвращает обновленный
        список вакансий"""

        data = read_json(self.file_path)
        self.vacancies_list.extend(data)  # Добавляем данные из файла в список

        # Проверяем, есть ли уже вакансия с такими же названием и работодателем
        if not any(key_vacancy["name_vacancy"] == vacancy.name_vacancy
                   and key_vacancy["employer"] == vacancy.employer
                   for key_vacancy in self.vacancies_list):
            self.vacancies_list.append(vacancy.to_dict())

        save_to_json(self.vacancies_list, self.file_path)

    def delete_vacancy(self, name_vacancy: str, employer: str) -> bool:
        """Удаляет вакансию из JSON-файл списка вакансий по названию вакансии и работодателю.
        Возвращает True, если вакансия была успешно удалена, иначе False"""

        data = read_json(self.file_path)
        self.vacancies_list.extend(data)  # Добавляем данные из файла в список

        found: bool = False
        for index, vacancy in enumerate(self.vacancies_list):
            if vacancy["name_vacancy"] == name_vacancy and vacancy["employer"] == employer:
                del self.vacancies_list[index]
                found = True
                break
        save_to_json(self.vacancies_list, self.file_path)
        return found

# if __name__ == "__main__":
#     vacancy_1 = Vacancy("Python Developer", "Москва",
#                       "Кадровое агентство Candidate",
#                       "Опыт разработки от 3-х лет", 110000, 180000,
#                       "https://api.hh.ru/vacancies/118000777?host=hh.ru")
#
#     vacancy_2 = Vacancy("Тестировщик", "Санкт-Петербург", "Компания Б",
#                         "Опыт работы 5 лет", 60000, 90000,
#                         "http://example.com/vacancy2")
#
#     vacancy_3 = Vacancy("Middle Python developer", "Санкт-Петербург",
#                          "ЛИГРЕС", "Писать код бизнес-процессов",
#                         120000, 150000,
#                         "https://api.hh.ru/vacancies/117628372?host=hh.ru")
#
#     vacancy_4 = Vacancy("Middle Python developer", "Санкт-Петербург",
#                         "МининС", "Писать код бизнес-процессов",
#                         120000, 150000,
#                         "https://api.hh.ru/vacancies/117628372?host=hh.ru")
#
#     vacancy_5 = Vacancy("Python developer", "Санкт-Петербург",
#                         "МининС", "Писать код бизнес-процессов",
#                         120000, 150000,
#                         "https://api.hh.ru/vacancies/117628372?host=hh.ru")
#
#     vacancy_6 = Vacancy("Python developer", "Санкт-Петербург",
#                         "МининС", "Писать код бизнес-процессов",
#                         120000, 150000,
#                         "https://api.hh.ru/vacancies/117628372?host=hh.ru")
#
#     # Абсолютный путь к файлу
#     base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#     file_path = os.path.join(base_dir, "data", "2025_03_13_Python_developer.json")
#
#     # Получение вакансий из файла с именем файла:
#     json_saver = JSONSaver(file_path)
#     json_saver.get_vacancy("Senior Python")
#
#     # Получение вакансий из файла без имени файла (название файла по умолчанию saver.json в классе):
#     json_saver_2 = JSONSaver()
#     json_saver_2.get_vacancy("Тестировщик")
#
#     # Сохранение информации о вакансиях в файл
#     json_saver_3 = JSONSaver()
#     json_saver_3.add_vacancy(vacancy_1)
#     json_saver_3.add_vacancy(vacancy_2)
#     json_saver_3.add_vacancy(vacancy_3)
#     json_saver_3.add_vacancy(vacancy_4)
#
#     # Добавление вакансии с работодателем как у vacancy_4, но названии вакансии другое
#     json_saver_3.add_vacancy(vacancy_5)
#     # Пробуем добавить вакансию аналогичную vacancy_5
#     json_saver_3.add_vacancy(vacancy_6)
#
#     # Удаление вакансии из JSON-файла "Middle Python developer", "ЛИГРЕС"
#     json_saver_3.delete_vacancy("Middle Python developer", "ЛИГРЕС")
