from logging import exception


def main():
    """Отвечает за основную логику проекта и связывает функциональности между собой"""
    return "   "

print(main())



# Приветствие и вопрос
first_que = ("""
 Привет! 

 Добро пожаловать в программу работы с банковскими транзакциями. 
 Выберите необходимый пункт меню:
 1. Получить информацию о транзакциях из JSON-файла
 2. Получить информацию о транзакциях из CSV-файла
 3. Получить информацию о транзакциях из XLSX-файла""")

print(first_que)
print()

#Определение типа файла, из которого будут обрабатываться операции
try:
    first_answer = int(input("Введите его номер: "))

    if 0 < first_answer < 4:
        print()
        if first_answer == 1:
            print("Для обработки выбран JSON-файл")
            file_with_operations = 1

        if first_answer == 2:
            print("Для обработки выбран CSV-файл")
            file_with_operations = 2

        if first_answer == 3:
            print("Для обработки выбран XLSX-файл")
            file_with_operations = 3

    else:
        print("Выбрано число не соответствующее пункту. Попробуйте еще раз")

except ValueError:
    print("Что-то не так с числом, попробуйте еще раз")


second_que = """
Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING """
print(second_que)
print()



try:
    second_answer = int("Укажите статус: ")

    if second_answer == "EXECUTED":
        print("OK")