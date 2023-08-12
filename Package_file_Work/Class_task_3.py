# Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк, сколько в более длинном файле.
# ✔ При достижении конца более короткого файла, возвращайтесь в его начало

def generalization_file(digit_file: str, name_file: str):
    digit_2 = []
    name_2 = []
    final_file = []
    with (
        open(digit_file, 'r', encoding='utf-8') as digit_1,
        open(name_file, 'r', encoding='utf-8') as name_1
    ):
        for i in digit_1:
            temp = i.replace('\n','')
            temp = temp.replace(',', '')
            temp_2 = temp.split('|')
            digit_2.append(int(temp_2[0]) * float(temp_2[1]))
        for j in name_1:
            name_2.append(j.replace('\n', ''))
        if len(digit_2) > len(name_2):
            count = len(digit_2)
            re_count = len(digit_2) - len(name_2)
        else:
            count = len(name_2)
            re_count = len(name_2) - len(digit_2)
        for k in range(count):
            if k < len(digit_2):
                temp_digit = digit_2[k]
            else:
                temp_digit = digit_2[k - re_count]
            if k < len(name_2):
                temp_name = name_2[k]
            else:
                temp_name = name_2[k - re_count]
            if temp_digit < 0:
                temp_all = temp_name.lower() + ' ' + str(temp_digit * -1)
            else:
                temp_all = temp_name.upper() + ' ' + str(round(temp_digit))
            final_file.append(temp_all)
    with open('final_file.txt', 'w', encoding='utf-8') as f:
        for h in final_file:
            f.write(f'{h}, \n')


if __name__ == '__main__':
    generalization_file('fn.txt', 'replacement_fantasy.txt')        




        

