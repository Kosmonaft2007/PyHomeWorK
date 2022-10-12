
from random import randint
# def get_temoerature():
#     return 0  # заглушка - 0

def get_temoerature(senser):
    return randint (-20,0)  if senser else  randint (0, 20)

def get_preassure(senser):
    if senser:
        return randint (720, 750)
    else:
        return randint (750, 770 )

def get_wind_speed(senser):
    if senser == 1:
        return randint(0, 30)
    else:
        return randint(30, 50)