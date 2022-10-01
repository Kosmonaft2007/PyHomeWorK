
# int
namber = 10

# float
price = 100.5

# str
name = 'Adraham'

# bool
status = False

print(namber)

print('Test')

# Напишите программу вывода на экран трех последовательно идущих чисел, каждое на отдельной строке.
# Первое число вводит пользователь, остальные числа вычисляются в программе.
# number = int(input())
# print(number)
# print(number+1)
# print(number+1+1)
# # print(a, a + 1, a + 2, sep="\n")

# Напишите программу, которая считывает три целых числа и выводит на экран их сумму. Каждое число записано в отдельной строке.
# a, b, c = int(input()), int(input()), int(input())
# print(a + b + c)

# a = int(input())
# print("Объем = ", a**3)
# print("Объем = ", 6*(a**2))
# print(f'Объем = {a ** 3}\nПлощадь полной поверхности = {6 * a ** 2}')


# a, b = int(input()), int(input())
# print((3*(a+b)**3)+ (275*b**2)-(127*a) -41)

# a = int(input())
# print(f'Следующее за числом {a} число: {a+1}')
# print(f"Для числа {a} предыдущее число: {a-1}")
#
#
# a, b,c = int(input()), int(input()), int(input())
# print(a+b+c)
# print((int(input()) + int(input()) + int(input()) + int(input())) * 3)
#
# a, d, n = int(input()), int(input()), int(input())
# print(a+d*(n-1))
#
# a = int(input())
# print(f'{a}---{2*a}---{3*a}---{4*a}---{5*a}')

a = int(input())
if 7 < a < -3:
    print('Принадлежит')
else:
    print('Не принадлежит')


n = int(input())
if not (-3 < n < 7):
    print('Принадлежит')
else:
    print('Не принадлежит')

x = int(input())
if len(str(x)) == 4 and (x % 7 == 0 or x % 17 == 0):
    print('YES')
else:
    print('NO')