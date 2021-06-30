"""
Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
Результаты анализа вставьте в виде комментариев к коду. Также укажите в комментариях версию Python и разрядность вашей ОС.
"""
# Win 10 x64 версии 10.0.19041
# Python 3.9.1 64bit
import sys
import random


# для помощи в расчетах напишем функцию которая будет возвращать размер переданных переменных
def memory_summary(lst: list):
    memory = 0
    for var in lst:
        spam = sys.getsizeof(var)
        print(f'# переменная: {var} занимает памяти: {spam}')
        memory += spam
    print(f'### общий размер: {memory} ')
    return memory

# для анализа возьмем по одной задаче из каждого ДЗ
# *************************************************************
# № 1 задача на вывод сумму и произведения цифр числа
# *************************************************************
# user_ch = int(input("введите трёхзначное число - "))
# a = user_ch % 10
# b = user_ch // 10 % 10
# c = user_ch // 100 % 10
# print(f'сумма цифр введённого числа : {a+b+c}')
# print(f'произведение цифр введённого числа : {a*b*c}')
# ***********  результат работы программы ***********************
# memory_summary([a, b, c, user_ch])
# введите трёхзначное число - 123
# сумма цифр введённого числа : 6
# произведение цифр введённого числа : 6
# ***********  результат работы замера  *************************
# переменная: 3 занимает памяти: 28
# переменная: 2 занимает памяти: 28
# переменная: 1 занимает памяти: 28
# переменная: 123 занимает памяти: 28
# общий размер: 112
# т.е. используется 4 переменные по 28 (или  иначе 4+24 согласно таблице из методички)

# *************************************************************
# № 2 задача с получение обратного числа для введённого - через цикл и строку, и через рекурсию
# *************************************************************
# result = ''
# user_input = input("введите целое натуральное число - ")
# for i in user_input:
#     result = i + result
# print(result)
# ***********  результат работы программы ***********************
# memory_summary([user_input, result, i])
# введите целое натуральное число - 12345
# 54321
# ***********  результат работы замера  *************************
# переменная: 12345 занимает памяти: 54 - строка
# переменная: 54321 занимает памяти: 54
# переменная: 5 занимает памяти: 50  - строка из одного символа
# общий размер: 158
# т.е. две переменные по 54 и одна переменная внутри цикла i ( 5 вызовов, по длине числа)

# def new_num(num: int):
#     memory_summary([num])
#     if num < 10:
#         return num
#     return new_num(num // 10) + ((num % 10) * 10 ** (len(str(num)) - 1))
# res = new_num(int(user_input))

# ***********  результат работы программы ***********************

# ***********  результат работы замера  *************************
#  в случае рекурсии также 5 вложенных вызовов (стек вызова), но т.к. работаем с числом размер выделяемой памяти меньше
# memory_summary([res])
# переменная: 12345 занимает памяти: 28
# общий размер: 28
# переменная: 1234 занимает памяти: 28
# общий размер: 28
# переменная: 123 занимает памяти: 28
# общий размер: 28
# переменная: 12 занимает памяти: 28
# общий размер: 28
# переменная: 1 занимает памяти: 28
# общий размер: 28
# переменная: 54321 занимает памяти: 28
# общий размер: 28
# итоговой переменной могло и не быть т.е. 5 * 28 = 140

# т.е. если сравнивать два решения то - вариант с использованием чисел экономичнее по памяти, но с использованием строки
# требует меньше операций (и более короткий код =) ). использование рекурсии расходует дополнительно больше памяти,
# чем решение через цикл

# *************************************************************
# № 3 задача на расчет суммы числе между min и max элементами
# *************************************************************
# sample_list = [random.randint(1, 100) for i in range(15)]
# result = 0
# max_ind = sample_list.index(max(sample_list))
# min_ind = sample_list.index(min(sample_list))
# for i in range(min(min_ind, max_ind)+1, max(min_ind, max_ind)):
#     memory_summary([i])
#     result += sample_list[i]
# print(f'1.максимальный элемент на {max_ind + 1} позиции; минимальный элемент на {min_ind + 1} позиции')
# print('2.сумма элементов между ними - ', result)

# ***********  результат работы программы ***********************
# memory_summary([sample_list, result, max_ind, min_ind])
# 1.максимальный элемент на 6 позиции; минимальный элемент на 11 позиции
# 2.сумма элементов между ними -  184

# ***********  результат работы замера  *************************
# переменная: 6 занимает памяти: 28
# общий размер: 28
# переменная: 7 занимает памяти: 28
# общий размер: 28
# переменная: 8 занимает памяти: 28
# общий размер: 28
# переменная: 9 занимает памяти: 28
# общий размер: 28
# в данном случае цикл отработал 4 раза, с переменной int в теле цикла

# переменная: [54, 95, 28, 72, 83, 97, 5, 73, 49, 57, 3, 34, 94, 65, 81] занимает памяти: 184
# переменная: 184 занимает памяти: 28
# переменная: 5 занимает памяти: 28
# переменная: 10 занимает памяти: 28
# общий размер: 268
# 2 вспомогательных переменных и одна для результата
# использование дополнитеных переменных обосновано читабельностью и простотой кода
