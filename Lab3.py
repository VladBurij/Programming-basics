#Задание 1
name = input("Введите своё имя: ")
age = input("Введите свой возраст: ")
for i in range(0,10): print(f"Меня зовут {name} и мне {age} лет.")
#Задание 2
num = input("Введите число от 1 до 9: ")
for i in range(1,11): print(f"{num} * {i} = {int(num)*i}")
#Задание 3
list = []
i0 = 0
while i0 < 100:
    i0 += 2
    list.append(i0)
print(list)
#Задание 4
num1 = int(input("Введите число: "))
fact = 1
for i in range(1,num1+1): fact*=i
print(fact)
#Задание 5
index = 20
list1 = []
while index >= 0:
    list1.append(index)
    index -= 1
print(list1)
#Задание 6
num2 = int(input("Введите число: "))
if num2 < 3: print("Число фибоначчи равно 1")
else:
    i1 = 1
    i2 = 1
    for i in range(0, num2 - 3):
        f_sum = i1 + i2
        i1 = i2
        i2 = f_sum
    print(i2)
#Задание 7
text = input("Введите слово: ")
text1 = ""
for i in text:
    text1 += i + str(text.index(i)+1)
print(text1)
#Задание 8
while True:
    nums = input("Введите два числа через пробел: ")
    nums = nums.split()
    print(f"Их сумма равна: {int(nums[0])+int(nums[1])}")