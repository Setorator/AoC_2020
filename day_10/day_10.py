
def jolt(adapters, curr_ada, adapt_set):
    if len(adapters) == 0 or adapters[0] > curr_ada + 3:
        adapt_set[3].append(curr_ada + 3)
        print("Product = " + (len(adapt_set[1]) * len(adapt_set[3])).__str__())
        return
    elif adapters[0] > curr_ada:
        adapt_set[adapters[0] - curr_ada].append(curr_ada)

    jolt(adapters[1:], adapters[0], adapt_set)


if __name__ == "__main__":
    lines = []
    with open("input.txt") as f:
        for line in f.readlines():
            lines.append(int(line.strip()))

    # Part 1
    lines.sort()
    adapt_set = {1: [], 2: [], 3: []}
    adapt_set[lines[0]].append(lines[0])
    jolt(lines[1:], lines[0], adapt_set)

    # Part 2
    lines.append(lines[-1] + 3)
    lines.sort(reverse=True)
    lines.append(0)

    path_set = {lines[0]: []}
    path_variants = {lines[0]: 1}
    for line in lines:
        path_set[line] = [i for i in lines if line < i <= line+3]
        tmp = [path_variants[i] for i in path_set[line]]
        path_variants[line] = sum(tmp) if sum(tmp) != 0 else 1

    print("Paths: " + path_variants[0].__str__())


