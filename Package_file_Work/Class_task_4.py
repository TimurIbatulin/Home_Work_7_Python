# Создайте функцию, которая создаёт файлы с указанным расширением. Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазон

import random
from string import ascii_lowercase, ascii_uppercase


def auto_create_file(*, extension_file: str, min_len: int, max_len: int, min_byte: int, max_byte: int, quantity_file: int):
    if min_len == None:
        min_len = 6
    if max_len == None:
        max_len = 30
    if min_byte == None:
        min_byte = 256
    if max_byte == None:
        max_byte = 4096
    if quantity_file == None:
        quantity_file = 42
    counte = 0
    while counte < quantity_file:
        counte += 1
        name_file = random.choice(ascii_uppercase)
        lenght_name = random.randint(min_len, max_len)
        for i in range(lenght_name):
            name_file = name_file + random.choice(ascii_lowercase)
        name_file = name_file + random.choice(ascii_lowercase) + '.' + extension_file
        with open(name_file, 'wb') as f:
            f.truncate(random.randint(min_byte, max_byte))


