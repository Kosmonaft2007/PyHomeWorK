# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

my_list = [2,3,4,5,6]
print(my_list,'==>')


def res_list(my_list):
    res_list = []

    for i in range(len(my_list) // 2):
        res_list.append(my_list[i] * my_list[-i - 1])

    if len(my_list) % 2 != 0:
        res_list.append(my_list[len(my_list) // 2] ** 2)

    return res_list


print(res_list(my_list))