# Данный модуль и реализованный в нем класс SavingVacancies
# не используется в главном модуле user_interaction для взаимодействия с пользователем и
# поэтому не тестировался.

# from src.vacancy import Vacancy
#
#
# class SavingVacancies:
#     """Класс для сохранения информации о вакансиях, добавления новых вакансий,
#     удаление вакансий и получение данных по указанным критериям"""
#     vacancy_list: list
#
#     def __init__(self, vacancy_list=None):
#         self.vacancy_list = vacancy_list if vacancy_list else []
#
#     def __str__(self):
#         result = ""
#         for vacancy in self.vacancy_list:
#             result += str(vacancy) + "\n"
#         return result
#
#     def add_vacancy(self, vacancy: Vacancy) -> list[Vacancy]:
#         """Метод добавляет вакансию в вакансии, если такой вакансии ещё нет.
#         Параметр vacancy - объект вакансии типа Vacancy, метод возвращает обновленный
#         список вакансий"""
#
#         # Проверяем, есть ли уже вакансия с такими же названием и работодателем
#         if not any(key_vacancy.name_vacancy == vacancy.name_vacancy
#                    and key_vacancy.employer == vacancy.employer
#                    for key_vacancy in self.vacancy_list):
#             self.vacancy_list.append(vacancy)
#         return self.vacancy_list
#
#     def delete_vacancy(self, name_vacancy: str, employer: str) -> bool:
#         """Удаляет вакансию из списка вакансий по названию вакансии и работодателю.
#         Возвращает True, если вакансия была успешно удалена, иначе False"""
#
#         found = False
#         for index, vacancy in enumerate(self.vacancy_list):
#             if vacancy.name_vacancy == name_vacancy and vacancy.employer == employer:
#                 del self.vacancy_list[index]
#                 found = True
#                 break
#         return found


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
#
#     # Сохранение информации о вакансиях в файл
#     json_saver = SavingVacancies()
#     print(json_saver)
#     json_saver.add_vacancy(vacancy_1)
#     print(json_saver)
#     json_saver.add_vacancy(vacancy_2)
#     print(json_saver)
#     json_saver.add_vacancy(vacancy_2)
#     print(json_saver)
#     json_saver.add_vacancy(vacancy_3)
#     print(json_saver)
#     json_saver.delete_vacancy("Python Developer", "Кадровое агентство Candidate")
#     print(json_saver)
