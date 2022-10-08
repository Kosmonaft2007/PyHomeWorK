# 4.* Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.


from random import uniform, randrange


def max_defference(my_list):
    min_value = 1
    max_value = my_list[0] % 1
    for val in my_list:
        val = round((val % 1, 2))
        if val < min_value: min_value = val
        if val > max_value: max_value = val


my_list = [1.1, 1.2, 3.1, 5, 10.01]

print(my_list)
print(max_defference(my_list))
