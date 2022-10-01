# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.

n = int(input('Enter number: '))


def sequence(n):
    return [[x, round((1 + 1 / x) ** x, 2)] for x in range(1, n + 1)]


print(dict(sequence(n)))
print(round(sum(dict (sequence(n)))))