
highest = 0
highest_bin = ""
bin_seats = []

with open("input1.txt") as f:
    for line in f.readlines():
        bin_line = ""
        for b in line.strip():
            bin_line += "0" if b == "F" else "1" if b == "B" else "0" if b == "L" else "1"
        bin_seats.append(bin_line)

    bin_seats.append(bin_line)

id_list = []
for seat in bin_seats:
    new = int(seat[:7], 2) * 8 + int(seat[7:], 2)
    id_list.append(new)
    if new > highest:
        highest = new
        highest_bin = seat

print("Highest BIN: " + highest_bin)
print("Highest ID: " + highest.__str__())

i = 0
while i < 255 * 8 + 8:
    if (i not in id_list) and (i-1 in id_list) and (i+1 in id_list):
        print("Empty seat ID: " + i.__str__())
        break
    i += 1


