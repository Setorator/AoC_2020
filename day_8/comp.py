
def get_gode():
    code = []
    with open("input.txt") as f:
        for line in f.readlines():
            line_split = line.split(" ")
            op = line_split[0]
            arg = line_split[1].strip()
            code.append([op, arg])
    return code


def run_code(code):
    acc = 0
    prog_count = 0
    code_lines = []

    while prog_count < len(code):
        op = code[prog_count][0]
        arg = code[prog_count][1]
        if prog_count not in code_lines:
            code_lines.append(int(prog_count))
            if op == "acc":
                acc += int(arg)
                prog_count += 1
            elif op == "jmp":
                prog_count += int(arg)
            elif op == "nop":
                prog_count += 1
        else:
            # replace with "print(acc) for part 1
            return "error"

    # Remove for part 1
    return acc.__str__()


if __name__ == "__main__":
    lines = get_gode()
    run_code(lines)

    # Part 2
    i = 0
    while i < len(lines):
        if lines[i][0] in ("jmp", "nop"):
            res = "error"
            if lines[i][0] == "jmp":
                lines[i][0] = "nop"
                res = run_code(lines)
                lines[i][0] = "jmp"
            elif lines[i][0] == "nop":
                lines[i][0] = "jmp"
                res = run_code(lines)
                lines[i][0] = "nop"

            if res != "error":
                print("Acc = " + res)
                break
        i += 1
