"""
Импортированы следующие модули:
json - для получение данных из файла
os.path - из библиотеки для работы с операционными системами импортирован модуль os.path для работы с путями
tqdm - для работы над выводом прогресса обработки информации на экран
re - для работы с регулярными выражениями
argparse - для работы с аргументами командной строки
"""

import json
from tqdm import tqdm
import re
import argparse


def check_type_int(input_data):
    while True:
        try:
            int(input_data)
            return input_data
        except ValueError:
            print("Вы ввели некорректное значение. Повторите попытку: ")
            input_data = input()


class FileWork:
    """
    Класс FileWork служит для записи из текстового файла.
    """
    __data: object

    def __init__(self, file: str):
        """
        Конструктор с параметрами
        Parameters
        ----------
        __data: object
            Принимает полученные из файла записи
        file: str
            Путь, где расположен файл с данными
        """

        try:
            self.__data = json.load(open(file, encoding="utf8"))
        except BaseException:
            print("Некорректное содержимое файла")

    @property
    def data(self):
        """
        Геттер
        Возвращает объект с данными из файла
        Returns
        -------
        object
        """
        return self.__data


class Validator:
    """
    Класс Validator служит для проверки данных на соответствие определенным требованиям
    """
    __telephone: str
    __weight: int
    __inn: str
    __passport_series: str
    __university: str
    __age: int
    __political_views: str
    __worldview: str
    __address: str

    def __init__(self, telephone: str, weight: int, inn: str, passport_series: str,
                 university: str, age: int, political_views: str, worldview: str, address: str):
        """
        Конструктор с параметрами
        Parameters
        ----------
        telephone: str
            Номер телефона
        weight: int
            Вес
        inn: str
            ИНН (Идентификационный номер налогоплательщика)
        passport_series: str
            Серия паспорта
        university: str
            Название университета
        age: int
            Возраст
        political_views: str
            Политические взгляды
        worldview: str
            Мировозрение
        address: str
            Адрес
        """
        self.__telephone = telephone
        self.__weight = weight
        self.__inn = inn
        self.__passport_series = passport_series
        self.__university = university
        self.__age = age
        self.__political_views = political_views
        self.__worldview = worldview
        self.__address = address

    def check_telephone_number(self) -> bool:
        """
        Функция проверки номера телефона на соответствие его определенному формату
        Возвращает True, если ошибок не обнаружено, в противном случае False
        Returns
        -------
        bool flag
        """
        if re.match(r"[+]\d[-][(]\d\d\d[)][-]\d\d\d[-]\d\d[-]\d\d",
                    self.__telephone) is None:
            return False
        return True

    def check_weight(self) -> bool:
        """
        Функция проверки веса на соответствие его определенному формату
        Возвращает True, если ошибок не обнаружено, в противном случае False
        Returns
        -------
        bool flag
        """
        try:
            value = int(self.__weight)
            if value > 150 or value <= 0:
                return False
            return True
        except BaseException:
            return False

    def check_inn(self) -> bool:
        """
        Функция проверки ИНН на соответствие его определенному формату
        Возвращает True, если ошибок не обнаружено, в противном случае False
        Returns
        -------
        bool flag
        """
        if re.match(r"\d{12}", self.__inn) is None:
            return False
        return True

    def check_passport_series(self) -> bool:
        """
        Функция проверки серии паспорта на соответствие его определенному формату
        Возвращает True, если ошибок не обнаружено, в противном случае False
        Returns
        -------
        bool flag
        """
        if re.match(r"\d\d[ ]\d\d", self.__passport_series) is None:
            return False
        return True

    def check_university(self) -> bool:
        """
        Функция проверки названия университета на соответствие его определенному формату
        Возвращает True, если ошибок не обнаружено, в противном случае False
        Returns
        -------
        bool flag
        """
        if re.match(r'[а-яА-я .-]+$', self.__university) is None or not self.__university.find("университет"):
            return False
        return True

    def check_age(self) -> bool:
        """
        Функция проверки возраста на соответствие его определенному формату
        Возвращает True, если ошибок не обнаружено, в противном случае False
        Returns
        -------
        bool flag
        """
        try:
            value = int(self.__age)
            if value > 150 or value <= 0:
                return False
            return True
        except BaseException:
            return False

    def check_political_views(self) -> bool:
        """
        Функция проверки политических взглядов на соответствие его определенному формату
        Возвращает True, если ошибок не обнаружено, в противном случае False
        Returns
        -------
        bool flag
        """
        if re.match(r'[а-яА-я .]+$', self.__political_views) is None:
            return False
        return True

    def check_worldview(self) -> bool:
        """
        Функция проверки мировозрения на соответствие его определенному формату
        Возвращает True, если ошибок не обнаружено, в противном случае False
        Returns
        -------
        bool flag
        """
        if re.match(r'[а-яА-я .]+$', self.__worldview) is None:
            return False
        return True

    def check_address(self) -> bool:
        """
        Функция проверки адреса на соответствие его определенному формату
        Возвращает True, если ошибок не обнаружено, в противном случае False
        Returns
        -------
        bool flag
        """
        if re.match(r'[а-яА-я0-9 .]+$',
                    self.__address) is None or not self.__address.startswith("ул. "):
            return False
        return True

    def type_error(self) -> str:
        if not self.check_telephone_number():
            return "error_telephone_number"
        elif not self.check_weight():
            return "error_weight"
        elif not self.check_inn():
            return "error_inn"
        elif not self.check_passport_series():
            return "error_passport_series"
        elif not self.check_university():
            return "error_university"
        elif not self.check_age():
            return "error_age"
        elif not self.check_political_views():
            return "error_political_views"
        elif not self.check_worldview():
            return "error_worldview"
        elif not self.check_address():
            return "error_address"
        return "no_errors"


"""
Сортировка вставками
"""


def insertion_sort(data, param):
    for i in range(1, len(data)):
        temp = data[i]
        while i - 1 >= 0 and temp[param] < data[i - 1][param]:
            data[i] = data[i - 1]
            i -= 1
        data[i] = temp


"""
Поиск максимального значения в словаре
"""


def max_value_in_data(data: object, param: str):
    numbers = []
    for el in data:
        numbers.append(int(el[param]))
    return max(numbers)


"""
Сортировка по сегменту
"""


def bucket_sort(data, param: str):
    new_data = []
    tmp = max_value_in_data(data, param)
    for _ in range(len(data)):
        new_data.append([])
    for i in range(len(data)):
        number = int(data[i][param] / (tmp/len(data)))
        new_data[number].append(data[i]) if number != len(data) else new_data[len(data) - 1].append(data[i])
    for z in range(len(new_data)):
        insertion_sort(new_data[z], param)
    result = []
    for x in range(len(new_data)):
        result += new_data[x]
    return result


file_input = ""
file_output = ""
error_telephone_number_col = 0
error_weight_col = 0
error_inn_col = 0
error_passport_series_col = 0
error_university_col = 0
error_age_col = 0
error_political_views_col = 0
error_worldviews_col = 0
error_address_col = 0
counter = 0
no_error_counter = 0

parser = argparse.ArgumentParser(description="Validator")
parser.add_argument("-input", dest="file_input")
parser.add_argument("-output", dest="file_output")
args = parser.parse_args()
info = FileWork(args.file_input)
output = open(args.file_output, 'w')
# python Validator.py -input E:\\lab2.txt -output E:\\lab2result.txt
# C:\Users\Артем\PyCharmProjects\Lab2\main.py
# python C:\Users\Артем\PyCharmProjects\Lab2\main.py -input E:\\lab2.txt
# -output E:\\lab2result.txt
for element in info.data:
    counter += 1

print("1 - Отсортировать корректные записи по весу\n2 - Отсортировать корректные записи по возрасту\n0 - Не отсортировывать корректные записи")
menu = input("Введите ваш выбор: ")
menu = int(check_type_int(menu))
while menu < 0 or menu > 2:
    menu = input("Введено некорректное значение. Повторите ввод: ")
    menu = int(check_type_int(menu))


validated_data = []

with tqdm(total=100) as progressbar:
    for element in info.data:
        check = Validator(
            element['telephone'],
            element['weight'],
            element['inn'],
            element['passport_series'],
            element['university'],
            element['age'],
            element['political_views'],
            element['worldview'],
            element['address'])
        error_check = check.type_error()
        if error_check == "no_errors":
            no_error_counter += 1
            validated_data.append(element)
        else:
            if error_check == "error_telephone_number":
                error_telephone_number_col += 1
            elif error_check == "error_weight":
                error_weight_col += 1
            elif error_check == "error_inn":
                error_inn_col += 1
            elif error_check == "error_passport_series":
                error_passport_series_col += 1
            elif error_check == "error_university":
                error_university_col += 1
            elif error_check == "error_age":
                error_age_col += 1
            elif error_check == "error_political_views":
                error_political_views_col += 1
            elif error_check == "error_worldview":
                error_worldviews_col += 1
            elif error_check == "error_address":
                error_address_col += 1
        progressbar.update(100 / counter)
print("Данные из файла: " + file_input + "успешно обработаны!")
print("Результат обработки загружен в " + file_output)
print("Всего записей: " + str(counter) + "\n")
print("Число валидных записей: " + str(no_error_counter) + "\n")
print("Число невалидных записей " + str(counter - no_error_counter) + "\n")
print("Число невалидных записей по типам ошибок: " + '\n')
print("Некорректно указан номер телефона: " + str(error_telephone_number_col) + "\n")
print("Некорректно указан вес: " + str(error_weight_col) + "\n")
print("Некорректно указан ИНН: " + str(error_inn_col) + "\n")
print("Некорректно указана серия паспорта: " + str(error_passport_series_col) + "\n")
print("Некорректно указано название университета: " + str(error_university_col) + "\n")
print("Некорректно указан возраст: " + str(error_age_col) + "\n")
print("Некорректно указаны политические взгляды: " + str(error_political_views_col) + "\n")
print("Некорректно указано мировозрение: " + str(error_worldviews_col) + "\n")
print("Некорректно указан адрес: " + str(error_address_col) + "\n")

import datetime

time = datetime.datetime.now()
if menu != 0:
    validated_data = bucket_sort(validated_data, "weight") if menu == 1 else bucket_sort(validated_data, "age")

print(datetime.datetime.now()-time)
time = datetime.datetime.now()
with open('E:\\lab2res.json', 'w', encoding='UTF-8') as file:
    json.dump(validated_data, file)

print(datetime.datetime.now()-time)
time = datetime.datetime.now()
with open('E:\\lab2res.json', encoding='UTF-8') as file:
    validated_data = json.load(file)

print(datetime.datetime.now()-time)
time = datetime.datetime.now()

v_counter = 0
for element in validated_data:
    v_counter += 1


for element in tqdm(validated_data):
    output.write("{" + "\n telephone: " + element['telephone'] + "\n weight: " + str(element['weight']) + "\n inn: " + element['inn'] + "\n passport_series: " + element['passport_series'] + "\n university: " + element['university'] + "\n age: " + str(element['age']) + "\n political_views: " + element['political_views'] + "\n worldview: " + element['worldview'] + "\n address: " + element['address'] + "\n" + "}\n")
    progressbar.update(100/v_counter)

