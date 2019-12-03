sum = 0
with open('input.txt', 'r') as file:
    for line in file:
        sum += (int(line) // 3) - 2
print(sum)