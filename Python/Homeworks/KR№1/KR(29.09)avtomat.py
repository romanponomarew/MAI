def abc(spisok, number):
    for i in reversed(range(8)):
        spisok[1][i] = str(number % 2)
        number = number // 2
    return spisok, number

def loop(count, old_spisok, c, spisok):
    for k in range(count):
        for i in range(len(old_spisok[0])):
            if (i == 0):
                string = "0" + old_spisok[k][i] + old_spisok[k][i + 1];
            elif (i == (len(old_spisok[0]) - 1)):
                string = old_spisok[k][i - 1] + old_spisok[k][i] + "0";
            else:
                string = old_spisok[k][i - 1] + old_spisok[k][i] + old_spisok[k][i + 1]
            for j in range(8):
                if (string == spisok[0][j]): c.append(spisok[1][j]);
        old_spisok.append(list(c))
        c.clear()
    return old_spisok

def main():
    print("Введите число (от 0 до 255)")
    number = int(input())
    print("Введите количество прогонов")  # сколько раз полностью преобразовать вектор
    count = int(input())
    while True:
        if ((number < 0) or (number > 255)):
            print("Вы ввели неподходящее число \n Введите число от 0 до 255 заново:")
            number = int(input())
        else: break
    spisok = [['111', '110', '101', '100', '011', '010', '001', '000'], ['0', '0', '0', '0', '0', '0', '0', '0']]
    abc(spisok, number)
    old_spisok = []
    c = []
    old_spisok.append(['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'])
    loop(count, old_spisok, c, spisok)
#Выводим по итерациям работу автомата
    for i in range(count + 1):
        print(*old_spisok[i])

main()