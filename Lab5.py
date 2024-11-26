import random
#Задание1
list1 = [3, 5, 10, 3, 45, 3, 11, 30, 55]
for i in list1:
    if i == 3: list1[list1.index(i)] = 30
print(list1)
#Задание2
list1 = [i*i for i in list1]
print(list1)
#Задание3
print(max(list1)/len(list1))
#Задание4
tuple = (4, 5, 6, 47, 3*6)
good = True
for i in tuple:
    if type(tuple[0]) != type(i):
        good = False
if good == True: print(sorted(tuple))
else:
    print("В кортеже разные типы данных. Их сортировка приведёт к ошибке.")
#Задание5
shop = {"сыр": 125, "яблоки": 100, "молоко": 140, "торт": 350, "апельсины": 105}
for i in shop:
    if shop[i] == min(list(shop.values())):
        print(f"Самый дешёвый товар - {i}, стоит всего {shop[i]} денег. ")
    if shop[i] == max(list(shop.values())):
        print(f"Самый дорогой товар - {i}, стоит аж {shop[i]} денег. ")
#Задание6
dictionary = {}
for i in list1:
    dictionary[i] = i
print(dictionary)
#Задание7
re_dict = {"help": "помогать", "send": "отправить", "fighter": "боец"}
word = input("Введите слово ")
if word in re_dict.values():
    for i in re_dict:
        if re_dict[i] == word:
            print(f"На английском это слово значит {i}")
else:
    print("Такого слова нет в словаре")
#Задание8
items = ("камень", "ножницы", "бумага", "ящерица", "спок")
print("Введите объект (камень, ножницы, бумага, ящерица, спок)")
p1 = input()
if p1 in items:
    p2 = random.choice(items)
    if (p1 == items[1] and p2 == items[2]) or (p1 == items[2] and p2 == items[0]) or (p1 == items[0] and p2 == items[3]) or (p1 == items[3] and p2 == items[4]) or (p1 == items[4] and p2 == items[1]) or (p1 == items[1] and p2 == items[3]) or (p1 == items[3] and p2 == items[2]) or (p1 == items[2] and p2 == items[4]) or (p1 == items[4] and p2 == items[0]) or (p1 == items[0] and p2 == items[1]):
        print(f"{p1} > {p2}. вы выиграли")
    else:
        print(f"{p1} < {p2}. вы проиграли")
else:
    print("неверный ввод")