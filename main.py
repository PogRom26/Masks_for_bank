import os
from pathlib import Path

from src.utils import load_transactions
from src.reading_trans import reading_transaction
from src.processing import filter_by_state, sort_by_date
from src.generators import filter_by_currency
from src.find_operation import process_bank_search


def main(file_with_operations:str, key_for_filter_by_state:str,
         key_for_sort_by_date:bool, key_for_sort_by_date_reverse:bool,
         code_for_filter_by_currency:str, search_for_process_bank_search:str) -> any:

    """Отвечает за основную логику проекта и связывает функциональности между собой"""
    list_with_data = []
    path_to_file = ""

    # Определение какой файл будет открыт для работы
    # К reading_trans.py - reading_transaction. К utils.py - load_transactions.

    project_dir = Path(__file__).parent
    data_dir = "data"
    data_folder = os.path.join(project_dir, data_dir)

    if file_with_operations == "JSON":
        json_files = [f.name for f in Path(data_folder).rglob('*.json')]
        file_name = "".join(json_files)

        path_to_file = os.path.join(project_dir, data_dir, file_name)
        list_with_data = load_transactions(path_to_file)

    elif file_with_operations == "CSV":
        csv_files = [f.name for f in Path(data_folder).rglob('*.csv')]
        file_name = "".join(csv_files)

        path_to_file = os.path.join(project_dir, data_dir, file_name)
        list_with_data = reading_transaction(path_to_file)

    elif file_with_operations == "XLSX":
        xlsx_files = [f.name for f in Path(data_folder).rglob('*.xlsx')]
        file_name = "".join(xlsx_files)

        path_to_file = os.path.join(project_dir, data_dir, file_name)
        list_with_data = reading_transaction(path_to_file)


    # Определение фильтрации. К processing.py - filter_by_state
    list_after_filter =[]
    if key_for_filter_by_state == "EXECUTED":
        list_after_filter = filter_by_state(list_with_data, "EXECUTED")

    if key_for_filter_by_state == "CANCELED":
        list_after_filter = filter_by_state(list_with_data, "CANCELED")

    if key_for_filter_by_state == "PENDING":
        list_after_filter = filter_by_state(list_with_data, "PENDING")

    # Сортировка. К processing.py - sort_by_date
    list_after_sort = []
    if key_for_sort_by_date:
        if key_for_sort_by_date_reverse:
            list_after_sort = sort_by_date(list_after_filter)
        else:
            list_after_sort = sort_by_date(list_after_filter, reverse=False)
    else:
        list_after_sort = list_after_filter

    # Показывать рублевые транзакции. К generators.py - filter_by_currency
    list_after_filter_by_currency = list(filter_by_currency(list_after_sort, code_for_filter_by_currency))

    # Показывает операции с фильтром по слову. К find_operation.py - process_bank_search
    if search_for_process_bank_search:
        list_after_filter_by_word = process_bank_search(list_after_filter_by_currency, search_for_process_bank_search)
    else:
        list_after_filter_by_word = list_after_filter_by_currency

    if len(list_after_filter_by_word) > 0:
        return list_after_filter_by_word
    else:
        return "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"


###########################################################################
# Приветствие и вопрос
que_about_file = ("""
 Привет!

 Добро пожаловать в программу работы с банковскими транзакциями.
 Выберите необходимый пункт меню:
 1. Получить информацию о транзакциях из JSON-файла
 2. Получить информацию о транзакциях из CSV-файла
 3. Получить информацию о транзакциях из XLSX-файла""")

print(que_about_file)
print()

#Определение типа файла, из которого будут обрабатываться операции.
# К reading_trans.py - reading_transaction. Для извлечения файла из CSV или XLSX
# К utils.py - load_transactions. Для извлечения файла из JSON

while True:
    answer_about_file = input("Введите его номер: ")
    print()
    if answer_about_file in "123" and len(answer_about_file) == 1:

        if answer_about_file == "1":
            print("Для обработки выбран JSON-файл")
            file_with_operations = "JSON"
            break

        elif answer_about_file == "2":
            print("Для обработки выбран CSV-файл")
            file_with_operations = "CSV"
            break

        elif answer_about_file == "3":
            print("Для обработки выбран XLSX-файл")
            file_with_operations = "XLSX"
            break
    else:
        print("Выбрано число не соответствующее пункту. Попробуйте еще раз")


#Определение фильтрации по операциям. К processing.py - filter_by_state
que_about_status = """
Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING """

print(que_about_status)
print()

while True:
    answer_about_status = input("Укажите статус: ")
    print()
    if answer_about_status.lower() in ["executed", "canceled", "pending"]:

        if answer_about_status.lower() == "executed":
            key_for_filter_by_state = "EXECUTED"
            print('Операции отфильтрованы по статусу "EXECUTED"')
            break

        elif answer_about_status.lower() == "canceled":
            key_for_filter_by_state = "CANCELED"
            print('Операции отфильтрованы по статусу "CANCELED"')
            break

        elif answer_about_status.lower() == "pending":
            key_for_filter_by_state = "PENDING"
            print('Операции отфильтрованы по статусу "PENDING"')
            break

    else:
        print(f'Статус операции "{answer_about_status}" недоступен')

print()

#Сортировка по дате. К processing.py - sort_by_date
while True:
    answer_about_sort_by_date = input("Отсортировать операции по дате? Да/Нет: ")
    if answer_about_sort_by_date.lower() == "да":
        key_for_sort_by_date = True
        break

    elif answer_about_sort_by_date.lower() == "нет":
        key_for_sort_by_date = False
        break

print()

#Сортировка по возрастанию или убыванию. К processing.py - sort_by_date
if answer_about_sort_by_date.lower() == "да":
    while True:
        answer_about_sort_by_date_reverse = input("Отсортировать: по убыванию/по возрастанию: ")
        if answer_about_sort_by_date_reverse.lower() == "по убыванию":
            key_for_sort_by_date_reverse = True
            break

        elif answer_about_sort_by_date_reverse.lower() == "по возрастанию":
            key_for_sort_by_date_reverse = False
            break
else:
    key_for_sort_by_date_reverse = False

print()

#Показывать рублевые транзакции. К generators.py - filter_by_currency
while True:
    answer_about_rub_trans = input("Выводить только рублевые транзакции? Да/Нет: ")
    if answer_about_rub_trans.lower() == "да":
        code_for_filter_by_currency = "RUB"
        break

    elif answer_about_rub_trans.lower() == "нет":
        code_for_filter_by_currency = None
        break

print()

# #Показывает операции с фильтром по слову. К find_operation.py - process_bank_search
while True:
    answer_about_filter = input("Отфильтровать список транзакций по определенному слову? Да/Нет: ")
    if answer_about_filter.lower() == "да":
        search_for_process_bank_search = input("Укажите это слово: ")
        break

    elif answer_about_filter.lower() == "нет":
        search_for_process_bank_search = False
        break

print()

print(main(file_with_operations, key_for_filter_by_state, key_for_sort_by_date, key_for_sort_by_date_reverse, code_for_filter_by_currency, search_for_process_bank_search))
