def data_prep():
    data = []
    with open('data3.txt', 'r') as f:
        data = f.readline()
    return data


def part1():
    data = data_prep()

    position = [0, 0]
    places = {tuple(position): 1}
    for c in data:
        if c == '>':
            position[0] += 1
        elif c == '<':
            position[0] -= 1
        elif c == '^':
            position[1] += 1
        else:
            position[1] -= 1

        if tuple(position) in places:
            places[tuple(position)] += 1
        else:
            places[tuple(position)] = 1

    return len(places)


def part2():
    data = data_prep()

    position = [[0, 0], [0, 0]]
    places = {tuple(position[0]): 1}
    turn = 0
    for c in data:
        if c == '>':
            position[turn][0] += 1
        elif c == '<':
            position[turn][0] -= 1
        elif c == '^':
            position[turn][1] += 1
        else:
            position[turn][1] -= 1

        if tuple(position[turn]) in places:
            places[tuple(position[turn])] += 1
        else:
            places[tuple(position[turn])] = 1
        turn += 1
        turn %= 2

    return len(places)
