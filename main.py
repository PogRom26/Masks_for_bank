
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
while True:
    first_answer = input("Введите его номер: ")
    print()
    if first_answer in "123" and len(first_answer) == 1:

        if first_answer == "1":
            print("Для обработки выбран JSON-файл")
            file_with_operations = "JSON"
            break

        elif first_answer == "2":
            print("Для обработки выбран CSV-файл")
            file_with_operations = "CSV"
            break

        elif first_answer == "3":
            print("Для обработки выбран XLSX-файл")
            file_with_operations = "XLSX"
            break
    else:
        print("Выбрано число не соответствующее пункту. Попробуйте еще раз")



second_que = """
Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING """

print(second_que)
print()

while True:
    second_answer = input("Укажите статус: ")
    print()
    if second_answer.lower() in ["executed", "canceled", "pending"]:

        if second_answer.lower() == "executed":
            key = "EXECUTED"
            print('Операции отфильтрованы по статусу "EXECUTED"')
            break

        elif second_answer.lower() == "canceled":
            key = "CANCELED"
            print('Операции отфильтрованы по статусу "CANCELED"')
            break

        elif second_answer.lower() == "pending":
            key = "PENDING"
            print('Операции отфильтрованы по статусу "PENDING"')
            break

    else:
        print('Укажите корректный фильтр')
