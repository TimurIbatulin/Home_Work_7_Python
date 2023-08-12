# Напишите функцию, которая генерирует псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.

import random
from string import ascii_lowercase, ascii_uppercase


def give_a_name_file():
    name_file = random.choice(ascii_uppercase)
    lenght_name = random.randint(4,6)
    for i in range(lenght_name):
        name_file = name_file + random.choice(ascii_lowercase)
    with open('replacement_fantasy.txt', 'a', encoding='utf-8') as f:
        f.write(f'{name_file} \n')

if __name__ == '__main__':
    give_a_name_file()