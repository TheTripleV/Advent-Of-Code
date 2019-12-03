sum = 0
with open('input.txt', 'r') as file:
    for line in file:
        mass = int(line)
        while True:
            mass = mass // 3 - 2
            if mass <= 0: break
            sum += mass
print(sum)