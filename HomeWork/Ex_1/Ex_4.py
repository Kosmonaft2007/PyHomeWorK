# 4. Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).
import random

random_number = random.randint(1, 4)

print(random_number)


if random_number > 0 and random_number < 5:
    if random_number == 1:
        print('x > 0 & y > 0')
    if random_number == 2:
        print('x > 0 & y < 0')
    if random_number == 3:
        print('x < 0 & y > 0')
    if random_number == 4:
        print('x < 0 & y < 0')
else:
    print("NO")
