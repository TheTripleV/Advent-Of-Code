paths = []


with open('input.txt', 'r') as file:
    for path in file:
        paths.append(path.split(','))

arr_width = 0
arr_height = 0

neg_width_offset = 0
pos_width_offset = 0

neg_height_offset = 0
pos_height_offset = 0


for path in paths:
    tmp_w = 0
    tmp_h = 0

    for seg in path:
        dir = seg[0]
        dist = int(seg[1:])

        if dir == "U":
            tmp_h -= dist
        if dir == "D":
            tmp_h += dist
        if dir == "L":
            tmp_w -= dist
        if dir == "R":
            tmp_w += dist

        neg_width_offset = min(tmp_w, neg_width_offset, 0)
        pos_width_offset = max(tmp_w, pos_width_offset, 0)

        neg_height_offset = min(tmp_h, neg_height_offset, 0)
        pos_height_offset = max(tmp_h, pos_height_offset, 0)

# print(neg_width_offset)
# print(pos_width_offset)
# print(neg_height_offset)
# print(pos_height_offset)

arr_height = -neg_height_offset + pos_height_offset + 1
arr_width = -neg_width_offset + pos_width_offset + 1

import numpy as np

arr = np.zeros((arr_height, arr_width))

idx = 0
for path in paths:
    idx += 1

    curr_y = -neg_height_offset
    curr_x = -neg_width_offset

    # print('vv')
    # print(curr_y)
    # print(curr_x)

    for seg in path:
        dir = seg[0]
        dist = int(seg[1:])

        if dir == "U":
            for y in range(curr_y - dist, curr_y + 1):
                if arr[y, curr_x] == 0 or arr[y, curr_x] == idx:
                    arr[y, curr_x] = idx
                else:
                    arr[y, curr_x] = -1

            curr_y -= dist
        if dir == "D":
            for y in range(curr_y, curr_y + dist + 1):
                if arr[y, curr_x] == 0 or arr[y, curr_x] == idx:
                    arr[y, curr_x] = idx
                else:
                    arr[y, curr_x] = -1

            curr_y += dist
        if dir == "L":
            for x in range(curr_x - dist, curr_x + 1):
                if arr[curr_y, x] == 0 or arr[curr_y, x] == idx:
                    arr[curr_y, x] = idx
                else:
                    arr[curr_y, x] = -1

            curr_x -= dist
        if dir == "R":
            for x in range(curr_x, curr_x + dist + 1):
                if arr[curr_y, x] == 0 or arr[curr_y, x] == idx:
                    arr[curr_y, x] = idx
                else:
                    arr[curr_y, x] = -1
            curr_x += dist
        # print('S')
        # print('{}, {}, {}, {}'.format(dir, dist, curr_y, curr_x))

curr_y = -neg_height_offset    
curr_x = -neg_width_offset

arr[curr_y, curr_x] = -2

# print(arr)


import tqdm

min_man_dist = 0

for y in tqdm.tqdm(range(arr.shape[0])):
    for x in range(arr.shape[1]):
        if arr[y,x] == -1:
            # print(y, x)
            ydist = -(y + neg_height_offset)
            xdist = (x + neg_width_offset)

            # print(y, x, ydist, xdist)

            if ydist != 0 and xdist != 0:
                tdist = ydist + xdist
                min_man_dist = min(min_man_dist, tdist)
                if min_man_dist == 0:
                    min_man_dist = tdist

print(min_man_dist)
