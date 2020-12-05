
def main1():
    res = []
    with open("input1.txt") as f:
        for line in f.readlines():
            res.append(int(line))

    i = 0
    j = 1
    res_value = 0
    while i < len(res):
        while j < len(res):
            if (res[i] != res[j]) and (res[i] + res[j] == 2020):
                res_value = res[i] * res[j]
                break
            j += 1
        if res_value != 0:
            break
        i += 1
        j = i + 1

    print("first val: " + res[i].__str__())
    print("second val: " + res[j].__str__())
    print("result val: " + res_value.__str__())


def main2():
    res = []
    with open("input1.txt") as f:
        for line in f.readlines():
            res.append(int(line))

    i = 0
    j = 1
    k = 2
    res_value = 0
    while i < len(res):
        while j < len(res):
            while k < len(res):
                if (res[i] != res[j]) and (res[i] + res[j] + res[k] == 2020):
                    res_value = res[i] * res[j] * res[k]
                    break
                k += 1
            if res_value != 0:
                break
            j += 1
            k = j +1
        if res_value != 0:
            break
        i += 1
        j = i + 1
        k = j + 1

    print("first val: " + res[i].__str__())
    print("second val: " + res[j].__str__())
    print("third val: " + res[k].__str__())
    print("result val: " + res_value.__str__())


if __name__ == "__main__":
    # Part 1
    # main1()

    # Part 2
    main2()