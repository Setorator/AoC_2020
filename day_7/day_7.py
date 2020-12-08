
def main1():
    rules = {}
    with open("input.txt") as f:
        for line in f.readlines():
            contain_ind = line.index(" contain ")
            contains_bags = line[contain_ind + len(" contain "):].split(", ")
            contains_bags[-1] = contains_bags[-1][:-2]

            for i in range(0, len(contains_bags)):
                contains_bags[i] += "s" if contains_bags[i][-1] != "s" else ""

            rules[line[:contain_ind]] = contains_bags

    res = 0
    for rule in rules:
        if find_gold(rules[rule], rules):
            res += 1

    print("Res: " + res.__str__())

    print("Gold bag contains: " + count_bags(rules["shiny gold bags"], rules).__str__())


def find_gold(bag_lst, rules):
    if bag_lst[0] == "no other bags":
        return False
    contains_gold = False
    for bag in bag_lst:
        bag_name = bag[2:]
        if bag_name == "shiny gold bags":
            return True
        elif find_gold(rules[bag_name], rules):
            contains_gold = True
    return contains_gold


def count_bags(bag_lst, rules):
    if bag_lst[0] == "no other bags":
        return 0
    num_bags = 0
    for bag in bag_lst:
        bag_num = int(bag[0])
        bag_name = bag[2:]
        if bag_name == "shiny gold bags":
            print("Error")
        else:
            num_bags += bag_num
            num_bags += bag_num * count_bags(rules[bag_name], rules)
    return num_bags

if __name__ == "__main__":
    main1()