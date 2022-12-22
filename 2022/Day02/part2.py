
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

def get_opposing(str1, str2):
    if str1 == 'A' and str2 == 'X':
        return 'Z'
    if str1 == 'A' and str2 == 'Y':
        return 'X'
    if str1 == 'A' and str2 == 'Z':
        return 'Y'

    if str1 == 'B' and str2 == 'X':
        return 'X'
    if str1 == 'B' and str2 == 'Y':
        return 'Y'
    if str1 == 'B' and str2 == 'Z':
        return 'Z'

    if str1 == 'C' and str2 == 'X':
        return 'Y'
    if str1 == 'C' and str2 == 'Y':
        return 'Z'
    if str1 == 'C' and str2 == 'Z':
        return 'X'

def calc_score(str1, str2):
    outcome = 0
    s2 = get_opposing(str1, str2)
    add = score2[s2]
    if (str1 == 'A' and s2 == 'Y') or (str1 == 'B' and s2 == 'Z') or (str1 == 'C' and s2 == 'X'):
        outcome = 6
    elif (str1 == 'A' and s2 == 'X') or (str1 == 'B' and s2 == 'Y') or (str1 == 'C' and s2 == 'Z'):
        outcome = 3
        add = score1[str1]
    return add + outcome

for line in f.readlines():
    line2 = line.strip()
    split = line2.split(' ')
    scoretotal += calc_score(split[0], split[1])

print(scoretotal)
