paths = []

sets = []


with open('input.txt', 'r') as file:
    for path in file:
        paths.append(path.split(','))
        sets.append(set())

idx = -1
for path in paths:
    idx += 1
    curr_y, curr_x = 0, 0

    for seg in path:
        dir = seg[0]
        dist = int(seg[1:])

        if dir == "U":
            for y in range(curr_y - dist, curr_y + 1):
                sets[idx].add((y, curr_x))
            curr_y -= dist                
        if dir == "D":
            for y in range(curr_y, curr_y + dist + 1):
                sets[idx].add((y, curr_x))
            curr_y += dist
        if dir == "L":
            for x in range(curr_x - dist, curr_x + 1):
                sets[idx].add((curr_y, x))
            curr_x -= dist   
        if dir == "R":
            for x in range(curr_x, curr_x + dist + 1):
                sets[idx].add((curr_y, x))
            curr_x += dist   

intersections = sets[0].intersection(*(sets[1:]))
intersections.remove((0,0))

min_man_dist = 0

for cord in intersections:
    man_dist = abs(cord[0]) + abs(cord[1])
    min_man_dist = min(min_man_dist, man_dist)
    if min_man_dist == 0:
        min_man_dist = man_dist

# print()
# print(intersections)
print(min_man_dist)