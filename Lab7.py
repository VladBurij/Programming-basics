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
clients_list = list(map(lambda x: x.update({"category": "Low"}), clients))
print(clients_list)