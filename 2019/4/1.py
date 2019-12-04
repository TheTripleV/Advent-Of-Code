
count = 0
for i in range(265275, 781584 + 1):
# for i in range(265275, 781584 + 1):

    bad = False

    adj_met = False

    s = str(i)
    for pos in range(1, 6):
        if s[pos] == s[pos - 1]: adj_met = True
        
        if int(s[pos]) < int(s[pos - 1]):
            bad = True
            break

    if adj_met and not bad:
        count += 1


print(count)