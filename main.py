
def main():
    """Отвечает за основную логику проекта и связывает функциональности между собой"""
    return "   "

print(main())


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

#Определение типа файла, из которого будут обрабатываться операции
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

#Сортировка по дате
while True:
    answer_about_sort_by_date = input("Отсортировать операции по дате? Да/Нет: ")
    if answer_about_sort_by_date.lower() == "да":
        key_for_sort_by_date = True
        break

    elif answer_about_sort_by_date.lower() == "нет":
        key_for_sort_by_date = False
        break

print()

#Сортировка по возрастанию или убыванию
while True:
    answer_about_sort_by_date_reverse = input("Отсортировать по возрастанию или по убыванию? Да/Нет: ")
    if answer_about_sort_by_date_reverse.lower() == "да":
        key_for_sort_by_date_reverse = True
        break

    elif answer_about_sort_by_date_reverse.lower() == "нет":
        key_for_sort_by_date_reverse = False
        break


#Показывать рублевые транзакции. К generators.py - filter_by_currency
while True:
    answer_about_rub_trans = input("Выводить только рублевые транзакции? Да/Нет: ")
    if answer_about_rub_trans.lower() == "да":
        code_for_filter_by_currency = "RUB"
        break

    elif answer_about_rub_trans.lower() == "нет":
        break




"""

Программа: Отфильтровать список транзакций по определенному слову 
в описании? Да/Нет

Пользователь: да/нет

Программа: Распечатываю итоговый список транзакций..."""
