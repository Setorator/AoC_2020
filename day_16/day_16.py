
val_range = []
tickets = []
fields = []
froms = []
tos = []
my_ticket = []
with open("input.txt") as f:
    input_part = 0
    for line in f.readlines():
        if len(line.strip()) == 0:
            input_part += 1
            continue

        if input_part == 0:
            tmp_line = line.split(" or ")
            fields.append(tmp_line[0].split(": ")[0])
            first_part = tmp_line[0].split(": ")[1]
            first_part = first_part.split("-")
            second_part = tmp_line[1].strip()
            second_part = second_part.split("-")
            froms.extend([int(first_part[0]), int(second_part[0])])
            tos.extend([int(first_part[1]), int(second_part[1])])

        if input_part == 1:
            if "your ticket" in line:
                continue
            my_ticket.extend([int(i.strip()) for i in line.split(",")])

        if input_part == 2:
            if "nearby tickets" in line:
                continue
            tickets.append([int(i.strip()) for i in line.split(",")])


# Part 1
legit_range = []
for i in range(len(froms)):
    for j in range(froms[i], tos[i]+1):
        if j not in legit_range:
            legit_range.append(j)

invalid = []
for tick in tickets:
    for val in tick:
        if val not in legit_range:
            invalid.append(val)

print("Part 1: " + sum(invalid).__str__())


# Part 2
valid_tickets = []
for tick in tickets:
    valid = True
    for val in tick:
        if val not in legit_range:
            valid = False
            break
    if valid:
        valid_tickets.append(tick)

field_ranges = {i: [] for i in range(len(fields))}
for i in range(len(froms)):
    field_ranges[i // 2].extend([j for j in range(froms[i], tos[i]+1)])


possible_field = {i: [j for j in range(len(fields))] for i in fields}
for tick in valid_tickets:
    for i in range(len(tick)):
        for key, vals in field_ranges.items():
            if tick[i] not in vals:
                if i in possible_field[fields[key]]:
                    possible_field[fields[key]].remove(i)

field_pos = {}
used_keys = []
while len(possible_field) > 0:
    for key, val in possible_field.items():
        for used in used_keys:
            if used in val:
                possible_field[key].remove(used)
        if len(val) == 1:
            field_pos[key] = val[0]
            used_keys.append(val[0])
            possible_field.pop(key)
            break

res = 1
for key, val in field_pos.items():
    if "departure" in key:
        res *= my_ticket[val]

print("Part 2: " + res.__str__())
