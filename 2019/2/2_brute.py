import copy

data = []

with open('input_modified.txt', 'r') as file:
    for line in file:
        data.append(int(line))


data_backup = copy.deepcopy(data)


result = 19690720

for data1 in range(100):
    for data2 in range(100):

        data = copy.deepcopy(data_backup)

        data[1] = data1
        data[2] = data2

        curr_pos = 0
        while True:
            op = data[curr_pos]
            if op == 1:
                data[data[curr_pos + 3]] = data[data[curr_pos + 1]] + data[data[curr_pos + 2]]
            elif op == 2:
                data[data[curr_pos + 3]] = data[data[curr_pos + 1]] * data[data[curr_pos + 2]]
            elif op == 99:
                break
            else:
                print('uh oh')

            curr_pos += 4

            if data[0] == result:
                print(100 * data1 + data2)

        # print(data[0])