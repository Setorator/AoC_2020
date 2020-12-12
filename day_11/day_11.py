import numpy as np


def evolve1(gen):
    new_gen = [gen[0]]
    changed = False
    for r in range(1, len(gen)-1):
        new_row = "."
        for c in range(1, len(gen[r])-1):

            if gen[r][c] != ".":
                # Calculate surrounding live neighbors
                surround = np.zeros((3, 3), int)
                for y in range(3):
                    for x in range(3):
                        surround[y][x] = 1 if gen[r-1+y][c-1+x] == "#" else 0
                # Don't count self
                surround[1][1] = 0
                alive = sum(sum(surround))

                if gen[r][c] == "L" and alive == 0:
                    new_row += "#"
                    changed = True
                elif gen[r][c] == "#" and alive >= 4:
                    new_row += "L"
                    changed = True
                else:
                    new_row += gen[r][c]
            else:
                new_row += "."
        new_row += "."
        new_gen.append(new_row)
    new_gen.append(gen[-1])

    return new_gen, changed


def main1(seats):
    gen, evolved = evolve1(seats)
    while evolved:
        gen, evolved = evolve1(gen)

    res = 0
    for i in gen:
        res += i.count("#")

    print("Taken seats: " + res.__str__())


def evolve2(gen):
    new_gen = [gen[0]]
    changed = False
    for r in range(1, len(gen) - 1):
        new_row = "."
        for c in range(1, len(gen[r]) - 1):

            if gen[r][c] != ".":

                right = None
                left = None
                for x in range(1, len(gen[0])):
                    if x < c and left is None:
                        left = True if gen[r][c-x] == "#" else False if gen[r][c-x] == "L" else None
                    elif x > c and right is None:
                        right = True if gen[r][x] == "#" else False if gen[r][x] == "L" else None

                up = None
                down = None
                for y in range(1, len(gen)):
                    if y > r and down is None:
                        down = True if gen[y][c] == "#" else False if gen[y][c] == "L" else None
                    elif y < r and up is None:
                        up = True if gen[r-y][c] == "#" else False if gen[r-y][c] == "L" else None

                upper_left = None
                lower_left = None
                for i in range(1, c+1):
                    if r-i >= 0 and upper_left is None:
                        upper_left = True if gen[r-i][c-i] == "#" else False if gen[r-i][c-i] == "L" else None
                    if r+i < len(gen) and lower_left is None:
                        lower_left = True if gen[r+i][c-i] == "#" else False if gen[r+i][c-i] == "L" else None

                upper_right = None
                lower_right = None
                for j in range(c+1, len(gen[0])):
                    if r - (j-c) >= 0 and upper_right is None:
                        upper_right = True if gen[r - (j-c)][j] == "#" else False if gen[r - (j-c)][j] == "L" else None
                    if r + (j-c) < len(gen) and lower_right is None:
                        lower_right = True if gen[r + (j-c)][j] == "#" else False if gen[r + (j-c)][j] == "L" else None

                # Calculate surrounding live neighbors
                alive = 1 if up else 0
                alive += 1 if upper_right else 0
                alive += 1 if right else 0
                alive += 1 if lower_right else 0
                alive += 1 if down else 0
                alive += 1 if lower_left else 0
                alive += 1 if left else 0
                alive += 1 if upper_left else 0

                if gen[r][c] == "L" and alive == 0:
                    new_row += "#"
                    changed = True
                elif gen[r][c] == "#" and alive >= 5:
                    new_row += "L"
                    changed = True
                else:
                    new_row += gen[r][c]
            else:
                new_row += "."
        new_row += "."
        new_gen.append(new_row)
    new_gen.append(gen[-1])

    return new_gen, changed


def main2(seats):
    gen, evolved = evolve2(seats)
    while evolved:
        gen, evolved = evolve2(gen)

    res = 0
    for i in gen:
        res += i.count("#")

    print("Taken seats: " + res.__str__())


if __name__ == "__main__":
    lines = []
    with open("input.txt") as f:
        for line in f.readlines():
            # Insert frame of "floor" around the map
            lines.append("." + line.strip() + ".")

    # Insert floor-frame in the top and bottom
    lines.insert(0, "."*len(lines[0]))
    lines.append("."*len(lines[0]))

    main1(lines)
    main2(lines)


