# Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
## ✔ Количество строк и имя файла передаются как аргументы функции.

import random


def fill_in_the_file(number_of_line: int, file_name: str):
    z = 1
    while z <= number_of_line:
        line_for_file = str(random.randint(-1000,1000)) + '|' + str(random.uniform(-1000, 1000))
        with open(file_name, 'a', encoding='utf-8') as f:
            f.write(f'{line_for_file}, \n')
        z += 1

if __name__ == '__main__':
    fill_in_the_file(1, 'fn.txt')
