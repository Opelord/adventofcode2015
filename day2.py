def data_prep():
    data = []
    with open('data2.txt') as f:
        data = f.readlines()
    data = [x[:-1] for x in data]
    return data


def part1():
    # prepare data
    data = data_prep()

    area = 0
    for sizes in data:
        tmp_size = [int(x) for x in sizes.split('x')]
        tmp_area = tmp_size[0]*tmp_size[1] + tmp_size[1]*tmp_size[2] + tmp_size[0]*tmp_size[2]
        tmp_area *= 2
        tmp_area += min([tmp_size[0]*tmp_size[1], tmp_size[1]*tmp_size[2], tmp_size[0]*tmp_size[2]])
        area += tmp_area

    return area


def mul(a, b, c): return a*b*c


def part2():
    data = data_prep()

    ribbon = 0
    for sizes in data:
        tmp_size = [int(x) for x in sizes.split('x')]
        perimeter = [2*(tmp_size[0]+tmp_size[1]), 2*(tmp_size[1]+tmp_size[2]), 2*(tmp_size[0]+tmp_size[2])]
        ribbon += mul(*tmp_size)
        ribbon += min(perimeter)

    return ribbon
