# Дорабатываем функции из предыдущих задач.
# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

import os
from pathlib import Path
import random
from string import ascii_lowercase, ascii_uppercase

def file_way(way: str):
    way_insp = ''
    way_1 = way.split('/')
    way_1.remove('')
    *_, name_file = way_1

    if '.' in name_file:
        for i in range(len(way_1) - 1):
            way_insp = way_insp + '/' + way_1[i]
    else:
        way_insp = way
        name_file = random.choice(ascii_uppercase)
        lenght_name = random.randint(4,6)
        for i in range(lenght_name):
            name_file = name_file + random.choice(ascii_lowercase)
        name_file =name_file + '.txt'
    if os.path.exists(way_insp):
        finish = way_insp + '/' + name_file
        if os.path.exists(finish):
            print('Такой файл существует в этой директории')
        else:
            if Path(way_insp).is_dir():
                with open(finish, 'w', encoding='utf-8') as f:
                    f.write(finish)
            else:
                Path(way_insp).mkdir(parents=True)
                with open(finish, 'w', encoding='utf-8') as f1:
                    f1.write(finish)

file_way('/Volumes/Samsung_T5/Python/Home_Work_7/fn2.txt')
# file_way('/Volumes/Samsung_T5/Python/Home_Work_7')
 