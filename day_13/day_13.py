
buses = open("input.txt").readlines()
arrival = int(buses[0].strip())
all_buses = [int(i) if i != "x" else 0 for i in buses[1].split(",")]
buses = [int(i) for i in buses[1].split(",") if i != "x"]

# Part 1
close_deps = {}
for bus in buses:
    close_deps[arrival + (bus - (arrival % bus))] = bus
print("Part 1: " + (close_deps[min(close_deps.keys())] * (min(close_deps.keys()) - arrival)).__str__())


# Part 2
def find_step(sp, first, second, ind_diff):
    start = sp
    # Find the start of the loop
    while (start + ind_diff) % second != 0:
        start += first
    end = start+first
    # Find where the loop repeats itself
    while (end + ind_diff) % second != 0:
        end += first

    # Return the start of the loop and the step-size
    return start, end - start


indexes = [all_buses.index(i) for i in buses if i != 0]
starts = []
steps = []
step = all_buses[indexes[0]]
start_point = 0
for i in indexes[1:]:
    tmp_start, tmp_step = find_step(start_point, step, all_buses[i], i)
    starts.append(tmp_start)
    steps.append(tmp_step)
    step = tmp_step
    start_point = tmp_start

# The last "start" is the final answer
print("Part 2: " + (starts[-1]).__str__())

