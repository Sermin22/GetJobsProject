# Данный модуль и реализованный в нем класс WorkingFiles
# не используется в главном модуле user_interaction для взаимодействия с пользователем и
# поэтому не тестировался.

# import os
# import json
#
#
# class WorkingFiles:
#     def __init__(self):
#         """Конструктор класса, который инициализирует путь к файлу.
#         Если путь не указан, он остаётся неопределённым до первого вызова метода."""
#
#         # Получаем абсолютный путь к корневой директории проекта
#         BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#         # Указываем путь к чтению и записи файла JSON - файла
#         file_path = os.path.join(BASE_DIR)
#         self.file_path = file_path
#
#     def read_json(self, file_path: str = None) -> list[dict]:
#         """ Функция, которая читает json-файл, где file_path - это путь к файлу.
#         Если не передан, используется путь, указанный в конструкторе.
#         Возвращает список словарей, прочитанных из файла.
#         """
#         # Проверяем указан ли путь к файлу
#         if file_path is None:
#             file_path = self.file_path
#         # Читаем файл
#         try:
#             with open(file_path, "r", encoding="UTF-8") as file:
#                 data = json.load(file)
#             return data
#         except FileNotFoundError:
#             # Если файла не существует, создаем новый пустой список
#             data = []
#         except json.JSONDecodeError as e:  # Обрабатываем ошибку декодирования JSON
#             print(f"Ошибка декодирования JSON: {e}")
#         except Exception as e:  # Обрабатываем другие возможные исключения
#             print(f"Ошибка чтения файла: {e}")
#         return data
#
#
#     def save_to_json(self, data, file_path: str = None):
#         """Функция записывает данные в JSON-файл, где data - это данные для записи в файл,
#         а file_path, этоп уть к файлу. Если он не передан, используется путь, указанный
#         в конструкторе."""
#
#         # Проверяем, указан ли путь
#         if file_path is None:
#             file_path = self.file_path
#         # Записываем данные в конец файла, если файла нет, то он будет создан
#         try:
#             with open(file_path, 'w', encoding='utf-8') as file:
#                 json.dump(data, file, ensure_ascii=False, indent=4)
#         except FileNotFoundError:
#             # Обработка ситуации, когда путь не существует
#             print(f"Путь '{file_path}' не найден.")
#             # Обработка любых непредвиденных ошибок
#         except Exception as e:
#             print(f"Неожиданная ошибка при сохранении данных: {e}")
#         return None


# if __name__ == "__main__":
#     # Получаем абсолютный путь к корневой директории проекта
#     BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#     # Указываем путь к записи файла file_name_vacancies
#     file_name_path = os.path.join(BASE_DIR, "data", "my_data.json")
#
#     # Создаем экземпляр класса с указанием пути к файлу
#     working_files = WorkingFiles(file_name_path)
#
#     # Записываем новые данные в файл
#     new_data = [
#         {"name": "Иван Иванов", "age": 30},
#         {"name": "Марья Петрова", "age": 25}
#     ]
#     working_files.save_to_json(new_data)
#
#     # Читаем данные из файла
#     data = working_files.read_json()
#     print(data)
