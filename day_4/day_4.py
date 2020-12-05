
fields = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid")

def main1():
    vals = []
    with open("input1.txt") as f:
        passport = []
        for line in f.readlines():
            if len(line) < 3:
                vals.append(passport)
                passport = []
                continue
            for field in fields:
                if field in line:
                    passport.append(field)

    vals.append(passport)
    res = 0
    for i in vals:
        if (len(i) == 8) or (len(i) == 7 and "cid" not in i):
            res += 1

    print("Res part 1: " + res.__str__())

def main2():

    min_max = {
        "byr": [1920, 2002],
        "iyr": [2010, 2020],
        "eyr": [2020, 2030],
        "hgt": [[150, 193], [59, 76]],
        "ecl": ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    }
    passports = []
    with open("input1.txt") as f:
        passport = {}
        for line in f.readlines():
            if len(line) < 3:
                passports.append(passport)
                passport = {}
                continue
            for field in fields:
                if field in line:
                    value_ind = line.index(":", line.index(field)) + 1
                    try:
                        passport[field] = line[value_ind:line.index(" ", value_ind)]
                    except ValueError:
                        if line[-1] == "\n":
                            passport[field] = line[value_ind:line.index("\n", value_ind)]
                        else:
                            passport[field] = line[value_ind:]

    passports.append(passport)

    res = 0
    for passport in passports:
        if not (len(passport) == 8 or (len(passport) == 7 and "cid" not in passport)):
            continue
        else:
            if "byr" in passport and not (min_max["byr"][0] <= int(passport["byr"]) <= min_max["byr"][1]):
                continue
            if "iyr" in passport and not (min_max["iyr"][0] <= int(passport["iyr"]) <= min_max["iyr"][1]):
                continue
            if "eyr" in passport and not (min_max["eyr"][0] <= int(passport["eyr"]) <= min_max["eyr"][1]):
                continue
            if "hgt" in passport:
                if "cm" in passport["hgt"]:
                    if not len(passport["hgt"][:-2]) == 3:
                        continue
                    if not min_max["hgt"][0][0] <= int(passport["hgt"][:-2]) <= min_max["hgt"][0][1]:
                        continue
                elif "in" in passport["hgt"]:
                    if not len(passport["hgt"][:-2]) == 2:
                        continue
                    if not (len(passport["hgt"][:2]) == 2 and min_max["hgt"][1][0] <= int(passport["hgt"][:-2]) <= min_max["hgt"][1][1]):
                        continue
                else:
                    continue
            if "hcl" in passport:
                if not (passport["hcl"][0] == "#" and len(passport["hcl"][1:]) == 6):
                    continue
                valid = True
                tmp = "0123456789abcdef"
                for c in passport["hcl"][1:]:
                    if c not in tmp:
                        valid = False
                        continue
                if not valid:
                    continue
            if "ecl" in passport and passport["ecl"] not in min_max["ecl"]:
                continue
            if "pid" in passport:
                if len(passport["pid"]) != 9:
                    continue
                valid = True
                for c in passport["pid"]:
                    if not c.isdigit():
                        valid = False
                        continue
                if not valid:
                    continue

            res += 1

    print("Res: " + res.__str__())

if __name__ == "__main__":

    main2()