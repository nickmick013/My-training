import os
import time

from os.path import join, getmtime, getsize, dirname

directory = '.'

for root, dirs, files in os.walk(directory):
  for file in files:

        filepath = os.path.join(root, file)

try:
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        file_size = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)

        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {file_size} байт,'
          f' Время изменения: {formatted_time}, Родительская директория: {parent_dir}')

except FileNotFoundError:
        print(f'Файл {file} недоступен или был удален')


