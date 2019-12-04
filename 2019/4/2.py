import sys

count = 0
for i in range(265275, 781584 + 1):
# for i in range(int(sys.argv[1]), int(sys.argv[1]) + 1):

    bad = False

    adj_met = False

    bad_adj = False

    s = str(i)
    for pos in range(1, 6):
        # if s[pos] == s[pos - 1]: adj_met = True
        
        if int(s[pos]) < int(s[pos - 1]):
            bad = True
            break
    
    if s[0] == s[1] and s[1] != s[2]:
        adj_met = True

    if s[1] == s[2] and s[0] != s[1] and s[2] != s[3]:
        adj_met = True

    if s[2] == s[3] and s[1] != s[2] and s[3] != s[4]:
        adj_met = True

    if s[3] == s[4] and s[2] != s[3] and s[4] != s[5]:
        adj_met = True

    if s[4] == s[5] and s[3] != s[4]:
        adj_met = True

    if adj_met and not bad and not bad_adj:
        # print(i)
        count += 1


print(count)