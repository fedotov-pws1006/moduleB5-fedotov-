fields = [["-", "-", "-"] for _ in range(3)]

def board(z):
    print(" ", "0", "1", "2")
    for i in range(len(fields)):
        print(str(i), *fields[i])


def coordinates(z):
    while True:
        spot = input("Введите координаты икс и игрек: ").split()
        if not (spot[0].isdigit() and spot[1].isdigit()):
            print("Введите числовые значения!")
            continue
        if len(spot) != 2:
            print("Введите два одинарных числа!")
            continue
        x, y = map(int, spot)
        if not (0 <= x <= 2 and 0 <= y <= 2):
            print("Введите целые числа в диапазоне от нуля до двух включительно!")
            continue
        if z[x][y] != "-":
            print("Данное поле занято!")
            continue

        break
    return x, y


def victory (z, user):
    winning_coordinates = (((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)),
                           ((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                           ((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 0)))

    for cord in winning_coordinates:
        symbols = []
        for c in cord:
            symbols.append(z[c[0]][c[1]])
        if symbols == [user, user, user]:
            return True

    return False


count = 0
while True:
    if count % 2 == 0:
        player = "x"
    else:
        player = "o"
    board(fields)
    x, y = coordinates(fields)
    fields[x][y] = player
    if count == 8:
        print("Ничья")
        break

    if victory(fields, player):
        if player == "x":
            player = "крестик"
        if player == "o":
            player = "нолик"
        print(f"Выиграл {player}!")
        board(fields)
        break

    count += 1





