
graph = {}
# graph['COM'] = None

with open('input.txt', 'r') as file:
    for line in file:
        spl = line.split(')')

        if spl[1][-1] == '\n':
            spl[1] = spl[1][:-1]

        graph[spl[1]] = spl[0]

# print(graph)

SAN_trail = set()

key = 'SAN'
while True:
    parent = graph[key]
    SAN_trail.add(parent)
    if parent == 'COM':
        break
    key = parent

# print(SAN_trail)

common_ancestor = None
you_count = 0
key = 'YOU'
while True:
    parent = graph[key]
    # print(parent)
    if parent in SAN_trail:
        common_ancestor = parent
        break
    key = parent
    you_count += 1

# print('d2')

san_count = 0
key='SAN'
while True:
    parent = graph[key]
    if parent == common_ancestor:
        break
    key = parent
    san_count += 1


print(you_count, san_count)
print(you_count + san_count)


