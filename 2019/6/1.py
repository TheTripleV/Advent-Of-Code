
graph = {}
# graph['COM'] = None

with open('input.txt', 'r') as file:
    for line in file:
        spl = line.split(')')

        if spl[1][-1] == '\n':
            spl[1] = spl[1][:-1]

        graph[spl[1]] = spl[0]

# print(graph)

count = 0

for key in graph:

    while True:
        parent = graph[key]
        count += 1
        if parent == 'COM':
            break
        key = parent


print(count)


