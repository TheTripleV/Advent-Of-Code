paths = []

sets = []
steps = []

with open('input.txt', 'r') as file:
    for path in file:
        paths.append(path.split(','))
        sets.append(set())
        steps.append(dict())

idx = -1
for path in paths:
    idx += 1
    curr_y, curr_x = 0, 0

    curr_steps = 0
    for seg in path:
        dir = seg[0]
        dist = int(seg[1:])

        if dir == "U":
            for y in range(curr_y - 1, curr_y - dist - 1, -1):
                curr_steps += 1
                sets[idx].add((y, curr_x))
                if (y, curr_x) not in steps[idx]:
                    steps[idx][(y, curr_x)] = curr_steps
            curr_y -= dist                
        if dir == "D":
            for y in range(curr_y + 1, curr_y + dist + 1):
                curr_steps += 1
                sets[idx].add((y, curr_x))
                if (y, curr_x) not in steps[idx]:
                    steps[idx][(y, curr_x)] = curr_steps
            curr_y += dist
        if dir == "L":
            for x in range(curr_x - 1, curr_x - dist - 1, -1):
                curr_steps += 1
                sets[idx].add((curr_y, x))
                if (curr_y, x) not in steps[idx]:
                    steps[idx][(curr_y, x)] = curr_steps
            curr_x -= dist   
        if dir == "R":
            for x in range(curr_x + 1, curr_x + dist + 1):
                curr_steps += 1
                sets[idx].add((curr_y, x))
                if (curr_y, x) not in steps[idx]:
                    steps[idx][(curr_y, x)] = curr_steps
            curr_x += dist

intersections = sets[0].intersection(*(sets[1:]))

if (0,0) in intersections: intersections.remove((0,0))

min_step_dist = 0

for cord in intersections:
    step_dist = sum(steps[idx][cord] for idx in range(len(steps)))
    if min_step_dist == 0 or step_dist < min_step_dist:
        min_step_dist = step_dist


# for coord in intersections:
#     print(coord[0], coord[1], steps[0][coord], steps[1][coord])

# print('-------')

# for tup in steps[0]:
#     print(tup, steps[0][tup])

# print()
# print(intersections)
print(min_step_dist)