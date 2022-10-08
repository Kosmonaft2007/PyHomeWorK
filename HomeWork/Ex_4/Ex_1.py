# 1. Вычислить число c заданной точностью d
def input_numbers():
    while True:
        num = input("введите_")
        try:
            number = float(num)
            return number
        except:
            print("вы введите не то число ")


def input_count():
    while True:
        num = input('введите контрольное число_')
        try:
            numbers = int(num)
            return numbers
        except:
            print("вы введите не то число")


number = input_numbers()
count = input_count()

print(f'{number:.{count}f}')
