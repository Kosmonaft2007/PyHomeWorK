# fail = open('first_fail.txt', 'r')
# mn_1 = fail.read()
# fail.close()
mn_1 = '5x^3+7x^2+5x+3=0'

# fail = open('second_fail.txt', 'r')
# mn_2 = fail.read()
# fail.close()
mn_2 = '4x^2+24x+2=0'

print(mn_1)
print(mn_2)

mn_1_spisok = [x for c in (mn_1.partition('=')[0]).split('+')]
mn_2_spisok = [x for c in (mn_2.partition('=')[0]).split('+')]


def razbor_mn(mn):
    mn_dext = {}
    x = len(mn) - 1
    for i in range(0, len(mn)):
        mn_dext[x] = int((mn[i]).partition('x')[0])
        x -= 1
    return mn_dext


mn_1_dect = razbor_mn(mn_1_spisok)
mn_2_dect = razbor_mn(mn_2_spisok)

if (len(mn_1_dect) > len(mn_2_dect)):
    for i in range(len(mn_2_dect), len(mn_1_dect)):
        mn_2_dect[i] = 0
elif (len(mn_2_dect) > len(mn_1_dect)):
    for i in range(len(mn_1_dect), len(mn_2_dect)):
        mn_1_dect[i] = 0


def summa_mn(mn_1, mn_2):
    resultat_mn = ''
    x = len(mn_1) - 1
    for i in range(0, len(mn_1)):
        if (x > 1):
            resultat_mn += f'{(mn_1[x] + mn_2[x])}x^{x}'
        elif (x == 1):
            resultat_mn += f'{(mn_1[x] + mn_2[x])}x'
        elif (x == 0):
            resultat_mn += f'{(mn_1[x] + mn_2[x])}'
        if (x > 0):
            resultat_mn += '+'
        x -= 1
    else:
        resultat_mn += '=0'
        return resultat_mn

    res_mn = summa_mn(mn_1_dect, mn_2_dect)
    print(res_mn)

    fail = open('summa.txt', 'w')
    fail.write(res_mn)
    fail.close()
