# Напишите функцию группового переименования файлов. Она должна:
# ✔ принимать параметр желаемое конечное имя файлов.
# При переименовании в конце имени добавляется порядковый номер.
# ✔ принимать параметр количество цифр в порядковом номере.
# ✔ принимать параметр расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# ✔ принимать параметр расширение конечного файла.
# ✔ принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение

import os


def home_work(*, way_to_files: str, name_file: str, count_digit_in_name: int, extension_file: str, disired_extension: str, letters_range: list):
    file_counte = 1
    for a, b, c in os.walk(way_to_files):
        for file_1 in c:
            if extension_file in file_1:
                new_name = ''
                a, *_ = file_1.split('.')
                for i in range(int(letters_range[0]), int(letters_range[1]), 1):
                    if i <= len(a):
                        new_name = new_name + a[i]
                new_name = new_name + name_file
                digit_simbol = str(file_counte)
                if len(digit_simbol) < count_digit_in_name:
                    count = count_digit_in_name - len(digit_simbol)
                    for q in range(count):
                        new_name = new_name + '0'
                    new_name = new_name + digit_simbol
                else:
                    new_name = new_name + digit_simbol
                if '.' in extension_file:
                    new_name = new_name + extension_file
                else:
                    new_name = new_name + '.' + extension_file
                file_counte += 1
                os.replace(os.path.join(way_to_files, file_1), os.path.join(way_to_files, new_name))


if __name__ == '__main__':
    home_work(way_to_files='/Volumes/Samsung_T5/Python/Home_Work_7/all', name_file='tutu', count_digit_in_name=3, extension_file='txt', disired_extension='eee', letters_range=[3,5])


        



