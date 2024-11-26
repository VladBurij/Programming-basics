#Задание1
temp = int(input("Какова температура? "))
if temp >= 20:
    print("Кондиционер выкл")
else:
    print("Кондиционер вкл")
#Задание2
mounth = int(input("Введите номер месяца: "))
if mounth == 12 or mounth == 1 or mounth == 2:
    print("Зима")
elif 2 < mounth < 6:
    print("Весна")
elif 5 < mounth < 9:
    print("Лето")
elif 8 < mounth < 12:
    print("Осень")
else:
    print("Неверный номер месяца. Значение должно быть от 1 до 12.")
#Задание3
age = input("Введите возраст собаки: ")
if age.isdigit():
    age = float(age)
    if 1 <= age <= 22:
        if age >= 2:
            print(f"По человеческим меркам это {21 + (age - 2) * 4} лет.")
        else:
            print(f"По человеческим меркам это {age * 10.5} лет.")
    else:
        print("Возраст должен быть больше года и меньше 22 лет")
else:
    print("Неверный ввод. Нужно ввести число")
#Задание4
num = input("Введите целое число: ")
sum_num = 0
for i in num: sum_num += int(i)
if int(num[-1]) % 2 == 0 and sum_num % 3 == 0:
    print("Данное число делится нацело на 6")
else:
    print("Данное число не делится нацело на 6")
#Задание5
password = input("Введите пароль, да понадёжнее: ")
nums = 0
up_let = 0
low_let = 0
spec = 0
for i in password:
    if i.isdigit(): nums += 1
    if i.isupper(): up_let += 1
    if i.islower(): low_let += 1
    if i in ".,:;!?@_*-+()/#№¤%&<>|\\": spec += 1
if nums > 0 and up_let > 0 and low_let > 0 and spec > 0:
    print("Пароль принят.")
else:
    if nums == 0:
        print("В пароле нет цифр.")
    if up_let == 0:
        print("В пароле нет заглавных букв.")
    if low_let == 0:
        print("В пароле нет строчных букв.")
    if spec == 0:
        print("В пароле нет специальных знаков.")