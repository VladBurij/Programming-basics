#Задание1
def time_convertor(time, *converts):
    time_num = int(time[:-1])
    result = ""
    for i in converts:
        if time[-1] == "h" and i == "m":
            result += f"{time_num*60}m, "
        elif time[-1] == "h" and i == "s":
            result += f"{time_num*3600}s, "
        elif time[-1] == "m" and i == "h":
            result += f"{time_num/60}h, "
        elif time[-1] == "m" and i == "s":
            result += f"{time_num*60}s, "
        elif time[-1] == "s" and i == "h":
            result += f"{time_num/3600}h, "
        elif time[-1] == "s" and i == "m":
            result += f"{time_num/60}m, "
        else:
            return "Проверьте правильность ввода данных"
    return time + " = " + result
#Задание2
def bank(money, age):
    old_money = money
    if money >= 30000:
        for i in range (1, age+1):
            persent_m = money // 10000 * 0.003
            if persent_m > 5: persent_m = 5
            if i <= 3:
                money *= 1 + persent_m + 0.03
            elif i <= 6:
                money *= 1 + persent_m + 0.05
            else:
                money *= 1 + persent_m + 0.02
        return f"Ваша прибыль составит {money - old_money} рублей"
    else:
        return "Минимальная сумма вклада должна составлять более 30000 рублей"
#Задание3
def simple_numbers(start, end):
    if isinstance(start, int) and isinstance(end, int) and end != start+1 and end > start:
        result = []
        for number in range(start, end+1):
            number_del = 0
            for i in range (2, number):
                if number % i == 0:
                    number_del += 1
            if number_del == 0: result.append(number)
        if len(result) > 0:
            return f"Простые числа диапазона {start} и {end}: {result}."
    elif start >= end:
        return "Конечное число должно быть больше начального"
    elif end == start + 1:
        return "Слишком малый диапазон, нужно минимум 3 числа"
    else:
        return "Некорректные данные"
#Задание4
def plus_matrix(s, matrix_1, matrix_2):
    if len(matrix_1) == len(matrix_2) == s and s >= 2:
        for i in range(0, s):
            for k in range(0, s):
                matrix_1[i][k] += matrix_2[i][k]
        return matrix_1
    elif s < 2:
        return "Матрицы должны быть минимум 2-го порядка"
    else:
        return "Неверно указан размер матриц"
#Задание5
def palindrom(word):
    word = word.replace(" ", "")
    c = len(word) // 2
    if word[0:c] == word[-1:-c-1:-1]:
        return "Это палиндром"
    else:
        return "Это не палиндром"
print(time_convertor("24m", "h", "s"))
print(bank(100000, 5))
print(simple_numbers(1, 120))
print(plus_matrix(3, [[2,5,6],[5,3,8],[3,-1,-7]], [[5,2,-3],[4,1,-9],[-3,-2,6]]))
print(palindrom("а роза упала на лапу азора"))
print(palindrom("радар"))