
f = open("input.txt")

scoretotal = 0

score1 = {
    'A' : 1,
    'B' : 2,
    'C' : 3
}

score2 = {
    'X' : 1,
    'Y' : 2,
    'Z' : 3
}

def calc_score(str1, str2):
    outcome = 0
    add = score2[str2]
    if (str1 == 'A' and str2 == 'Y') or (str1 == 'B' and str2 == 'Z') or (str1 == 'C' and str2 == 'X'):
        outcome = 6
    elif (str1 == 'A' and str2 == 'X') or (str1 == 'B' and str2 == 'Y') or (str1 == 'C' and str2 == 'Z'):
        outcome = 3
        add = score1[str1]
    return add + outcome

for line in f.readlines():
    line2 = line.strip()
    split = line2.split(' ')
    scoretotal += calc_score(split[0], split[1])

print(scoretotal)
