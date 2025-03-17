from src.vacancy import Vacancy


def test_vacancy_init(vacancy):
    assert vacancy.name_vacancy == "Python Developer"
    assert vacancy.area == "Москва"
    assert vacancy.employer == "Кадровое агентство Candidate"
    assert vacancy.requirement == "Опыт разработкиот 3-х лет"
    assert vacancy.get_salary_from == 110000
    assert vacancy.get_salary_to == 180000

def test_vacancy_str(vacancy):
    assert str(vacancy) == ("Python Developer, Москва, Кадровое агентство Candidate, "
                            "Опыт разработкиот 3-х лет, 110000, 180000, "
                            "https://api.hh.ru/vacancies/118000777?host=hh.ru")

def test_vacancy_to_dict(vacancy):
    """Тест, проверяющий корректное преобразование объект класса Vacancy в словарь"""
    assert vacancy.to_dict() == {'name_vacancy': 'Python Developer', 'area': 'Москва',
                                 'employer': 'Кадровое агентство Candidate', 'requirement':
                                 'Опыт разработкиот 3-х лет', 'salary_from': 110000, 'salary_to': 180000,
                                 'url': 'https://api.hh.ru/vacancies/118000777?host=hh.ru'}

def test_cast_to_object_list(vacancies):
    """Тест, проверяющий метод преобразования набора данных из JSON в список объектов класса Vacancy"""

    # Вызываем функцию создания объектов из JSON данных
    vacancies_list = Vacancy.cast_to_object_list(vacancies)

    # Проверяем количество объектов
    assert len(vacancies_list) == 3

    # Проверяем первую объект класса
    vacancy_1 = vacancies_list[0]
    assert isinstance(vacancy_1, Vacancy)
    assert vacancy_1.name_vacancy == "Python Developer"
    assert vacancy_1.area == "Москва"
    assert vacancy_1.requirement == "Опыт разработки от 3-х лет"
    assert vacancy_1.get_salary_from == 110000
    assert vacancy_1.get_salary_to == 180000
    assert vacancy_1.url == "https://api.hh.ru/vacancies/118000777?host=hh.ru"

def test_object_comparison(vacancy, vacancy_2):
    """Тестирование методов сравнения объектов класса Vacancy по минимальной зарплате(salary_from)"""

    # метод __lt__
    assert (vacancy < vacancy_2) == True  # True, потому что минимальная зарплата vacancy меньше
    # метод __gt__
    assert (vacancy > vacancy_2) == False
    # метод __eq__
    assert (vacancy == vacancy_2) == False
    # метод __le__
    assert (vacancy <= vacancy_2) == True
    # метод __ge__
    assert (vacancy >= vacancy_2) == False
    # метод __ne__
    assert (vacancy != vacancy_2) == True
