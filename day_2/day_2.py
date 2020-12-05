
def main1():
    min_list = []
    max_list = []
    char_list = []
    passwords = []
    with open("input1.txt") as f:
        for line in f.readlines():
            dash_ind = line.index("-")
            colon_ind = line.index(":")
            first_space_ind = line.index(" ", 0, colon_ind)
            min_list.append(int(line[:dash_ind]))
            max_list.append(int(line[dash_ind+1:first_space_ind]))
            char_list.append(line[first_space_ind+1])
            passwords.append(line[colon_ind+2:])

    res = 0
    i = 0
    while i < len(passwords):
        s = passwords[i].count(char_list[i])
        if min_list[i] <= s <= max_list[i]:
            res += 1
        i += 1

    print("Result: " + res.__str__())


def main2():
    first_pos = []
    second_pos = []
    char_list = []
    passwords = []
    with open("input1.txt") as f:
        for line in f.readlines():
            dash_ind = line.index("-")
            colon_ind = line.index(":")
            first_space_ind = line.index(" ", 0, colon_ind)
            first_pos.append(int(line[:dash_ind]))
            second_pos.append(int(line[dash_ind + 1:first_space_ind]))
            char_list.append(line[first_space_ind + 1])
            passwords.append(line[colon_ind + 2:])

    res = 0
    i = 0
    while i < len(passwords):
        first_correct = passwords[i][first_pos[i]-1] == char_list[i]
        second_correct = passwords[i][second_pos[i]-1] == char_list[i]
        if first_correct != second_correct:
            res += 1
        i += 1

    print("Result: " + res.__str__())


if __name__ == "__main__":

    #main1()
    main2()