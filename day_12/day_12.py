import math

lines = []
with open("input.txt") as f:
    for line in f.readlines():
        lines.append([line[0], int(line[1:].strip())])

directions = {"N": 0, "E": 1, "S": 2, "W": 3}
headings = {0: [0, -1],
            1: [1, 0],
            2: [0, 1],
            3: [-1, 0]}

# Part 1
x, y = 0, 0
faces = 1

for heading, dist in lines:
    if heading == "R":
        faces = (faces + (dist // 90)) % 4
    elif heading == "L":
        # One left turn is three right turns
        faces = (faces + (dist*3 // 90)) % 4
    elif heading == "F":
        # Move in the heading we faces
        x += headings[faces][0] * dist
        y += headings[faces][1] * dist
    else:
        # Move in the heading told
        x += headings[directions[heading]][0] * dist
        y += headings[directions[heading]][1] * dist

manhattan = abs(x) + abs(y)
print("Manhattan distance: " + manhattan.__str__())


# Part 2
ferry_x, ferry_y = 0, 0
wp_x, wp_y = 10, -1

for heading, dist in lines:
    if heading == "R":
        angle = dist * (math.pi / 180)
        wp_xp = round(wp_x * math.cos(angle) - wp_y * math.sin(angle))
        wp_yp = round(wp_x * math.sin(angle) + wp_y * math.cos(angle))
        wp_x = wp_xp
        wp_y = wp_yp
    elif heading == "L":
        # One left turn is three right turns
        angle = -dist * (math.pi / 180)
        wp_xp = round(wp_x * math.cos(angle) - wp_y * math.sin(angle))
        wp_yp = round(wp_x * math.sin(angle) + wp_y * math.cos(angle))
        wp_x = wp_xp
        wp_y = wp_yp
    elif heading == "F":
        # Move in the heading of the waypoint
        ferry_x += wp_x * dist
        ferry_y += wp_y * dist
    else:
        # Move in the heading told
        wp_x += headings[directions[heading]][0] * dist
        wp_y += headings[directions[heading]][1] * dist

manhattan = abs(ferry_x) + abs(ferry_y)
print("Manhattan distance: " + manhattan.__str__())
