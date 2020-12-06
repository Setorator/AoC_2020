def main1():
    groups = []
    with open("input.txt") as f:
        group = ""
        for line in f.readlines():
            if len(line.strip()) == 0:
                groups.append(group)
                group = ""
            else:
                group += line.strip()
        groups.append(group)

    res = 0
    for group in groups:
        unique = {c for c in group}
        res += len(unique)

    print("Sum anyone yes: " + res.__str__())


def main2():
    groups = []
    with open("input.txt") as f:
        group = []
        for line in f.readlines():
            if len(line.strip()) == 0:
                groups.append(group)
                group = []
            else:
                group.append(line.strip())
        groups.append(group)

    res = 0
    for group in groups:
        for c in group[0]:
            res += 1 if all_yes(group[1:], c) else 0

    print("Sum everyone yes: " + res.__str__())


def all_yes(lst, c):
    if len(lst) == 0:
        return True
    return c in lst[0] and all_yes(lst[1:], c)


if __name__ == "__main__":
    main1()
    main2()
