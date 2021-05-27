import string


def data_prep():
    data = []
    with open('data5.txt') as f:
        for line in f:
            data.append(line[:-1])
    return data


def part1():
    data = data_prep()
    vowels = 'aeiou'
    banned = ('ab', 'cd', 'pq', 'xy')
    doubles = tuple([c+c for c in string.ascii_lowercase])
    bad_count = 0
    for item in data:
        double_exists = 0
        vowels_count = 0
        already_naughty = 0
        for i in range(len(item)-1):
            if item[i:i + 2] in doubles:
                double_exists += 1
            if item[i:i+2] in banned:
                bad_count += 1
                already_naughty = 1
                break
            if item[i] in vowels:
                vowels_count += 1
        if item[-1] in vowels:
            vowels_count += 1
        if (vowels_count < 3 or double_exists < 1) and not already_naughty:
            bad_count += 1
            already_naughty = 1

    return len(data) - bad_count


def part2():
    data = data_prep()
    nice_count = 0
    for item in data:

        first_and_third = 0
        for i in range(len(item)-2):
            if item[i] == item[i+2]:
                first_and_third = 1
                break

        two_doubles_in_item = 0
        for i in range(len(item)-3):
            tmp_substring1 = item[i:i+2]
            tmp_substring2 = item[i+2:]
            if tmp_substring1 in tmp_substring2:
                two_doubles_in_item += 1

        if two_doubles_in_item and first_and_third:
            nice_count += 1


    return nice_count
