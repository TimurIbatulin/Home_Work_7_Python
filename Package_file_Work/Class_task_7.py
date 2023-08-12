# Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировк

import os
from pathlib import Path
import shutil

def sorted_file(way: str):
    for dir_path, dir_name, file_name in os.walk(way):
        for i in file_name:
            *_, extended = i.split('.')
            if extended == 'mp4' or extended == 'avi' or extended == 'wmv':
                way_new = way + '/' + 'video' 
                if Path(way_new).is_dir():
                    os.replace(os.path.join(way, i), os.path.join(way_new, i))
                else:
                    Path(way_new).mkdir(parents=True)
                    os.replace(os.path.join(way, i), os.path.join(way_new, i))
            if extended == 'jpg' or extended == 'tiff' or extended == 'jpeg':
                way_new = way + '/' + 'picture' 
                if Path(way_new).is_dir():
                    os.replace(os.path.join(way, i), os.path.join(way_new, i))
                else:
                    Path(way_new).mkdir(parents=True)
                    os.replace(os.path.join(way, i), os.path.join(way_new, i))
            if extended == 'txt' or extended == 'doc' or extended == 'rtf':
                way_new = way + '/' + 'documents' 
                if Path(way_new).is_dir():
                    os.replace(os.path.join(way, i), os.path.join(way_new, i))
                else:
                    Path(way_new).mkdir(parents=True)
                    os.replace(os.path.join(way, i), os.path.join(way_new, i))


if __name__ == '__main__':
    sorted_file('/Volumes/Samsung_T5/Python/Home_Work_7/all')

