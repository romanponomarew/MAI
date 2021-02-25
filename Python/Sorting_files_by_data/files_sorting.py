# -*- coding: utf-8 -*-

import os, time, shutil


# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk(path)  Принимает имя папки(или путь до нее)
#   Возвращает кортеж (Имя папки, имена вложенных папок, имена файлов)

#   os.path.dirname(path)  Возвращает имя каталога из переданного
#   в агрументе пути dirname('/home/User/Documents/file.txt')

#   os.path.join Соединяет переданные значения в строку-путь:
#   os.path.join('home', 'User', 'Desktop', 'file.txt') --->  'home/User/Desktop/file.txt'

#   os.path.normpath(path) Нормализует переданный путь os.path.normpath('/home/./Documents') ---> /home/Documents
#   os.path.getmtime(path) Возвращает время последней модификации файла или каталога в формате float(с начала ЭПОХИ)
#   НУЖНО перевести в time.ctime(mtime)

#   time.gmtime  Возвращает время ЭПОХИ в UTC: print("\nгод:", result.tm_year) print("tm_hour:", result.tm_hour)
#   os.makedirs  Создать директорию и все промежуточные d = 'a/b/c/d/test_dir'  >>> os.makedirs(d, 0o774)
#   shutil.copy2 Копирует файл dest = shutil.copy2(source, destination)
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.


class SortingFilesByData:
    """
    На вход исходная папка с файлами и желаемое название отсортированной папки
    На выходе папка с файлами, отсортированными по годам и месяцам
    """

    def __init__(self, sorting_directory_path: str, result_directory_name: str):
        self.sorting_directory_path = sorting_directory_path
        self.result_directory_name = result_directory_name
        self.result_directory_path = ""
        self.result_directories = {"root_directory": self.result_directory_name, "years": [], "months": []}

    def make_dir(self):
        """
        Создать результирующую папку в текущей директории
        :return:
        """
        os.makedirs(self.result_directory_name, mode=0o777)  # "icons_by_year"

    def sorting_files(self):
        tree = os.walk("icons")
        for dirname, directories, files in tree:
            print("dirname", dirname)
            print("directories", directories)
            print("files", files)
            for file in files:
                print("--+--+---+---+--")
                file_path = os.path.join(dirname, file)
                print("file_path=", file_path)
                file_age_time = os.path.getmtime(file_path)
                file_data = time.gmtime(file_age_time)
                print("file_data=", file_data)

                file_data_year = file_data.tm_year
                print("file_data_year=", file_data_year)
                file_data_month = file_data.tm_mon
                print("file_data_month=", file_data_month)
                print("------------")

                if file_data_year in self.result_directories["years"]:
                    if file_data_month in self.result_directories["months"]:
                        self.file_copy(
                            file_path_source=file_path,
                            file_path_destination=os.path.join(self.result_directory_name,
                                                               str(file_data_year), str(file_data_month)))
                    else:
                        self.make_month_directory(year=file_data_year, month=file_data_month)
                        self.result_directories["months"].append(file_data_month)
                        self.file_copy(
                            file_path_source=file_path,
                            file_path_destination=os.path.join(self.result_directory_name,
                                                               str(file_data_year), str(file_data_month)))
                    # Копировать файл в сууществующую директорию self.result_directory_name/file_data_year

                else:
                    self.make_year_directory(file_data_year)
                    self.result_directories["years"].append(file_data_year)
                    self.make_month_directory(year=file_data_year, month=file_data_month)
                    self.result_directories["months"].append(file_data_month)
                    self.file_copy(
                        file_path_source=file_path,
                        file_path_destination=os.path.join(self.result_directory_name,
                                                           str(file_data_year), str(file_data_month)))

    def make_year_directory(self, year):
        """
        В результрующей папке создать папки-номер года
        :return:
        """
        path = os.path.join(self.result_directory_name, str(year))  # "icons/2018"
        os.makedirs(path, mode=0o777)

    def make_month_directory(self, year, month):
        """
        В результрующей папке/номер_года создать папки-номер месяца
        :return:
        """
        path = os.path.join(self.result_directory_name, str(year), str(month))
        os.makedirs(path, mode=0o777)

    def file_copy(self, file_path_source, file_path_destination):
        """
        Копируем файл в нужную папку
        :return:
        """
        file_path_source = os.path.normpath(file_path_source)
        file_path_destination = os.path.normpath(file_path_destination)
        shutil.copy2(file_path_source, file_path_destination)


test1 = SortingFilesByData(sorting_directory_path="icons", result_directory_name="icons_by_year")
test1.make_dir()
test1.sorting_files()

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
