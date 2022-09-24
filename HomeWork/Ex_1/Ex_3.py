# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).


import random


random_x = random.randint(-10, 10)
random_y = random.randint(-10, 10)
print(random_x)
print(random_y)

if random_x != 0 and random_y != 0:
    if random_x > 0 and random_y > 0:
        print('1')
    if random_x > 0 and random_y < 0:
        print('2')
    if random_x < 0 and random_y < 0:
        print('3')
    if random_x < 0 and random_y > 0:
        print('4')
else:
    print("NO")




