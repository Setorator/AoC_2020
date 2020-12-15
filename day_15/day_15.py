
numbers = [1, 0, 15, 2, 10, 13]
num_ind = {}
for i in range(len(numbers)):
    num_ind[numbers[i]] = [0, i+1]

turn = len(numbers)+1
while turn < 30000001:  # Part 1 = 2021
    # Next number is either 0 or the diff between indexes for the earlier number
    if num_ind[numbers[-1]][0] == 0:
        numbers.append(0)
    else:
        numbers.append(num_ind[numbers[-1]][1] - num_ind[numbers[-1]][0])

    # Update indexes or simply add it anew
    if numbers[-1] in num_ind:
        num_ind[numbers[-1]][0] = num_ind[numbers[-1]][1]
        num_ind[numbers[-1]][1] = turn
    else:
        num_ind[numbers[-1]] = [0, turn]

    turn += 1

print("2020th number: " + numbers[-1].__str__())
