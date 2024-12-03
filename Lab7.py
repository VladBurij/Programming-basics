#Задание1
tasks = [("Проверить почту", 3), ("Написать отчёт", 1), ("Позвонить клиенту", 2)]
print((lambda x: sorted(x))(tasks))
#Задание2
purchases = [
    {"item": "Laptop", "price": 1000, "quantity": 2},
    {"item": "Mouse", "price": 25, "quantity": 5},
    {"item": "Keyboard", "price": 45, "quantity": 3}
]
m_list = list(map(lambda x: x["price"] * x["quantity"], purchases))
print(f"Самая дорогая покупка стоит {max(m_list)} рублей.")
#Задание3
clients = [
    {"name": "Alice", "income": 50000},
    {"name": "Bob", "income": 120000},
    {"name": "Charlie", "income": 70000}
]
list(map(lambda x: x.update({"category": "Low"}) if x["income"] < 50000 else x.update({"category": "Medium"}) if x["income"] < 100000 else x.update({"category": "High"}), clients))
print(clients)
#Задание4
flights = [
    {"flight": "A1", "departure": 9, "arrival": 12},
    {"flight": "B2", "departure": 14, "arrival": 18},
    {"flight": "C3", "departure": 6, "arrival": 8}
]
flights_12 = list(filter(lambda x: x if x["arrival"] >= 12 else None, flights))
print(flights_12)
#Задание5
messages = [
    {"user": "Исследователь А", "message": "Отчёт готов. Ссылка: http://foundation.org"},
    {"user": "Доктор Б", "message": "Документы можно найти здесь: https://classified.com"},
    {"user": "Охранник В", "message": "Нет аномальной активности за смену."},
    {"user": "Агент Г", "message": "Срочно изучите материалы по объекту 173 на http://statue-database.net"},
    {"user": "Д-р Кляйн", "message": "Обновлённый протокол эксперимента доступен: https://safezone.scp"},
    {"user": "Сотрудник Д", "message": "Просьба ознакомиться с https://docs.anomalies-secure.com перед сменой."},
    {"user": "Старший учёный Л", "message": "Все записи переданы. Никаких аномалий на объекте 096."},
    {"user": "Техник З", "message": "Проблема с сервером устранена. Подробнее: http://fix-report.internal"}
]
list(filter(lambda x: x.update({"message": "Ссылка: [ДАННЫЕ УДАЛЕНЫ]"}) if "http" in x["message"] else None, messages))
print(messages)
