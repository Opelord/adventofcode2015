import hashlib


def data_prep():
    data = []
    with open('data4.txt') as f:
        data = f.read()

    return data


def part1(n):
    data = data_prep()

    ans = 0
    while True:
        result = hashlib.md5((data+str(ans)).encode())
        if result.hexdigest()[:n] == n*'0':
            break
        ans += 1

    return ans


def part2():
    return part1(6)
