# 1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.

# a = int(input())
#
# b = int(input())
#
# if a*a == b or b*b == a:
#     print('yes')
# else:
#     print('no')

# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

# max_var = 0
#
# for i in range(5):
#     a = int(input())
#     if max_var < a:
#         max_var = a
#
#         print(max_var)

# 3. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

# 6. Пример проверки ложности утверждения (x ≡ z ) ∨ (x → (y ∧ z))

for x in range(2):
    for y in range(2):
        for z in range(2):
            if not (x == z or x <= y and z):
                print(x, y, z)