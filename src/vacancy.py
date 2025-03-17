
class Vacancy:
    """Класc для работы с вакансиями"""
    name_vacancy: str
    area: str
    employer: str
    requirement: str
    salary_from: int
    salary_to: int
    url: str

    __slots__ = ("name_vacancy", "area", "employer", "requirement", "__salary_from",
                 "__salary_to", "url")

    def __init__(self, name_vacancy, area, employer, requirement, salary_from, salary_to, url):
        self.name_vacancy = name_vacancy
        self.area = area
        self.employer = employer
        self.requirement = requirement
        self.__salary_from = salary_from if salary_from else 0
        self.__salary_to = salary_to if salary_to else 0
        self.url = url

    def __str__(self):
        return (f"{self.name_vacancy}, {self.area}, {self.employer}, {self.requirement}, "
                f"{self.__salary_from}, {self.__salary_to}, {self.url}")

    def to_dict(self):
        """Метод возвращающий преобразованный объект класса Vacancy в виде словаря"""
        return {'name_vacancy': self.name_vacancy, 'area': self.area, 'employer': self.employer,
                'requirement': self.requirement, 'salary_from': self.get_salary_from, 'salary_to': self.get_salary_to,
                'url': self.url}

    # Методы получения зарплаты
    @property
    def get_salary_from(self):
        return self.__salary_from

    @property
    def get_salary_to(self):
        return self.__salary_to

    @classmethod
    def cast_to_object_list(cls, data_vacancies):
        """Метод, преобразующий набор данных из JSON в список объектов класса Vacancy"""
        vacancies = []
        for key_data in data_vacancies:
            vacancy = cls(**key_data)
            vacancies.append(vacancy)
        return vacancies

    # Методы сравнения по минимальной зарплате
    def __lt__(self, other):
        """Сравнение по минимальной зарплате"""
        return self.get_salary_from < other.get_salary_from

    def __gt__(self, other):
        """Сравнение по минимальной зарплате"""
        return self.get_salary_from > other.get_salary_from

    def __eq__(self, other):
        """Сравнение по минимальной зарплате"""
        return self.get_salary_from == other.get_salary_from

    def __le__(self, other):
        """Сравнение по минимальной зарплате"""
        return self.get_salary_from <= other.get_salary_from

    def __ge__(self, other):
        """Сравнение по минимальной зарплате"""
        return self.get_salary_from >= other.get_salary_from

    def __ne__(self, other):
        """Сравнение по минимальной зарплате"""
        return self.get_salary_from != other.get_salary_from


# if __name__ == "__main__":
#     # Создаем объект класса
#     from src.headhunter_api import HeadHunterApi
#
#     hh_api = HeadHunterApi()
#     # Получаем вакансии
#     hh_vacancies = hh_api.get_vacancies("Python developer")
#     # Преобразуем набор данных (список вакансий) из JSON в список объектов класса Vacancy
#     vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
#     # Выводим список объектов класса Vacancy
#     print(vacancies_list)
#     # Выводим наименование вакансии и работодателя первой в списке вакансии (она с индексом - 0)
#     print(vacancies_list[0].name_vacancy)
#     print(vacancies_list[0].employer)
#
#     # Пример работы конструктора класса с одной вакансией
#     vacancy = Vacancy("Python Developer", "Москва",
#                       "Кадровое агентство Candidate",
#                       "Опыт разработкиот 3-х лет", 110000, 180000,
#                       "https://api.hh.ru/vacancies/118000777?host=hh.ru")
#     print(vacancy)
#     print(vacancy.to_dict())
#
#     # Сравниваем минимальные зарплаты
#     vacancy1 = Vacancy("Программист", "Москва", "Компания А", [],
#                        50000, 80000, "http://example.com/vacancy1")
#     vacancy2 = Vacancy("Тестировщик", "Санкт-Петербург", "Компания Б", [],
#                        60000, 90000, "http://example.com/vacancy2")
#
#     print(vacancy1 < vacancy2)  # True, потому что минимальная зарплата у vacancy1 меньше
#     print(vacancy1 > vacancy2)  # False
#     print(vacancy1 == vacancy2)  # False
#     print(vacancy1 <= vacancy2)  # True
#     print(vacancy1 >= vacancy2)  # False
#     print(vacancy1 != vacancy2)  # True
