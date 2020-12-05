
def main1():
    with open("input1.txt") as f:
        space = []
        for line in f.readlines():
            space.append(line.rstrip())

    row_size = len(space[0])
    x_pos = 0
    y_pos = 0
    count_trees = 0
    while y_pos < len(space) - 1:
        x_pos += 3
        x_pos %= row_size
        y_pos += 1

        if space[y_pos][x_pos] == "#":
            count_trees += 1

    print("Trees: " + count_trees.__str__())

def main2():
    with open("input1.txt") as f:
        space = []
        for line in f.readlines():
            space.append(line.rstrip())

    row_size = len(space[0])
    count_trees = [0, 0, 0, 0, 0]
    slopes = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2)
    ]

    for slope in slopes:
        y_pos = 0
        x_pos = 0
        while y_pos < len(space) - 1:
            x_pos += slope[0]
            x_pos %= row_size
            y_pos += slope[1]

            if space[y_pos][x_pos] == "#":
                count_trees[slopes.index(slope)] += 1

    print(count_trees.__str__())
    print("Product: ")


if __name__ == "__main__":

    #main1()

    main2()