def part1():
    # read data
    with open('data1.txt') as f:
        data = f.readline()

    # solve, pretty straightforward
    level = 0
    for c in data:
        if c == '(':
            level += 1
        else:
            level -= 1
    return level


def part2():
    # read data
    with open('data1.txt') as f:
        data = f.readline()

    level = 0
    count = 0
    while level != -1:
        if data[count] == '(':
            level += 1
        else:
            level -= 1
        count += 1
    return count
