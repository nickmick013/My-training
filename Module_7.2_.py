"""
Создайте функцию custom_write(file_name, strings), которая принимает аргументы file_name - название файла для записи,
strings - список строк для записи.
Функция должна:
1. Записывать в файл file_name все строки из списка strings, каждая на новой строке.
2. Возвращать словарь strings_positions, где ключом будет кортеж (<номер строки>, <байт начала строки>), а значением
- записываемая строка. Для получения номера байта начала строки используйте метод tell() перед записью.
"""
from idlelib.iomenu import encoding


def custom_write(file_name, strings):
    dict_strings = {}
    strings_positions = 0
    file = open(file_name, 'a', encoding='utf-8')
    for string in strings:
        strings_positions +=1
        cursor = file.tell()
        dict_strings[(strings_positions, cursor)] = string
        file.write(string + '\n')
    file.close()
    return dict_strings

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]


result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)