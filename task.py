# Напишите функцию, которая получает на вход директорию и
# рекурсивно обходит её и все вложенные директории. Результаты обхода
# сохраните в файлы json, csv и pickle. Для дочерних объектов указывайте
# родительскую директорию. Для каждого объекта укажите файл это или директория.
# Для файлов сохраните его размер в байтах, а для директорий
# размер файлов в ней с учётом всех вложенных файлов и директорий.
# Пример:
# test/users/names.txt
# Результат в json для names.txt:
# {
# "name": names.txt
# "parent": users,
# "type": "file"
# }



import os
import json
import csv
import pickle


def get_directory_size(directory: str):
    """получение размера директории"""
    total_size = 0

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            total_size += os.path.getsize(file_path)

            return total_size


def travers_directory(directory: str):
    """создание списков для сохранения результатов"""
    json_data = []
    csv_data = []
    pickle_data = []

    # рекурсивный обход директорий
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)

            file_info = {
                'name': file,
                'type': 'file',
                'size': os.path.getsize(file_path)
            }
            json_data.append(file_info)
            csv_data.append(file_info)
            pickle_data.append(file_info)

       for dir in dirs:
           dir_path = os.path.join(root, dir)

           # получение информации о директории (имя, тип, размер файлов в ней)
           dir_info = {
               'name': file,
                'type': 'file',
                'size': os.path.getsize(file_path)

           }

           json_data.append(dir_info)
           csv_data.append(dir_info)
           pickle_data.append(dir_info)

    with open('result.json', 'w') as json_file:
        json.dump(json_data, json_file, indent=4)

    with open('result.csv', 'w', newline='') as csv_file:
        filednames = ['name', 'type', 'size']
        writer = csv.DictWriter(csv_file, filednames=filednames)
        writer.writeheader()
        writer.writerows(csv_data)

    with open('result.pickle', 'wb') as pickl_file:
        pickle.dump(pickle_data, pickl_file)


DIRECT_FILE = 'hwork'
travers_directory(DIRECT_FILE)

