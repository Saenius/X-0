
\field = [[' ' for _ in range(3)] for _ in range(3)]


def show():
    print(f'  0 1 2')
    for i in range(3):
        print(f'{i} {field[i][0]} {field[i][1]} {field[i][2]}')


# show()


def ask():
    while True:
        cords = input('Введите сначала число столбца по вертикали, затем - строки по горизотали: ').split()

        if len(cords) != 2:
            print('только 2 координаты!')
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print('введите числа!!')
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print('неверные координаты!')
            continue

        if field[x][y] != ' ':
            print('занято!')
            continue


        return x, y


def cross():
    x, y = ask()
    field[x][y] = 'X'


def zero():
    x, y = ask()
    field[x][y] = '0'


def check_win():
    win_strick = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)), ((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 0))]

    # for stricks in win_strick:
    #     simbols = []
    #
    #     for strick in stricks:
    #         simbols.append(field[strick[0]][strick[1]])
    #
    #         if simbols == ['X', 'X', 'X']:
    #             print(f'Выиграл X')
    #             return True
    #         if simbols == ['0', '0', '0']:
    #             print(f'Выиграл 0')
    #             return True

    for strick in win_strick:
        a, b, c = strick[0], strick[1], strick[2]

        if field[a[0]][a[1]] == field[b[0]][b[1]] == field[c[0]][c[1]] != ' ':
            print(f'-------Выиграл {field[a[0]][a[1]]}---------')
            return True

    return False


num = 0
while True:
    show()
    num += 1
    if num % 2 == 1:
        cross()
    else:
        zero()

    if check_win():
        show()
        break

    if num == 9:
        print('Ничья!')
        break





