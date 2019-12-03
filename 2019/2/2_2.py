import sys

data = []

with open('input_modified.txt', 'r') as file:
    for line in file:
        data.append(int(line))


data[1] = int(sys.argv[1])
data[2] = int(sys.argv[2])

curr_pos = 0
while True:
    # print(data)
    op = data[curr_pos]

    # print(op)

    if op == 1:
        data[data[curr_pos + 3]] = data[data[curr_pos + 1]] + data[data[curr_pos + 2]]
    elif op == 2:
        data[data[curr_pos + 3]] = data[data[curr_pos + 1]] * data[data[curr_pos + 2]]
    elif op == 99:
        break
    else:
        print('uh oh')

    curr_pos += 4

print(data[0])

# Steps -> manually try -> increment pos 1 until ans is close -> increment pos 2

