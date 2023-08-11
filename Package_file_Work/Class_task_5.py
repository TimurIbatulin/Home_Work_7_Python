# Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.



from Class_task_4 import auto_create_file


def file_genereid(**kwargs):
    parametr_extension = locals().get('kwargs')
    for i in parametr_extension:
        exten = i
        count_file = int(parametr_extension.get(i))
        auto_create_file(extension_file=exten, min_len=4, max_len=4, min_byte=4, max_byte=4, quantity_file=count_file)



file_genereid(txt = 1, doc = 2)

