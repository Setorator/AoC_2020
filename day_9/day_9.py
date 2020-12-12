

def main1():
    lines = []
    with open("input.txt") as f:
        for line in f.readlines():
            lines.append(int(line.strip()))

    i = 25
    while i < len(lines):
        correct = False
        for j in range(i-25, i-1):
            for k in range(j+1, i):
                if lines[j] + lines[k] == lines[i]:
                    correct = True
        if not correct:
            print("Error: " + lines[i].__str__())
            return
        i += 1


def main2():
    lines = []
    with open("input.txt") as f:
        for line in f.readlines():
            lines.append(int(line.strip()))

    goal = 776203571
    start = 0
    while start < len(lines):
        sum_lines = []
        for i in range(start, len(lines)):
            sum_lines.append(lines[i])
            if sum(sum_lines) > goal:
                start += 1
                break
            elif sum(sum_lines) == goal:
                print("Min + Max = {}".format(min(sum_lines) + max(sum_lines)))
                return


if __name__ == "__main__":
    main1()
    main2()
