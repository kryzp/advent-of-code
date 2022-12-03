
def get_overlapping(l1, l2):
    result = []
    for c1 in l1:
        for c2 in l2:
            if c1 == c2 and (c1 not in result):
                result.append(c1)
    return result

def get_prio(c):
    if c.isupper():
        return ord(c) - ord('A') + 27
    elif c.islower():
        return ord(c) - ord('a') + 1

f = open("input.txt")
result = 0


for raw in f.readlines():
    line = raw.strip()
    n = len(line) // 2
    line1 = line[0:n]
    line2 = line[n:]
    overlapping = get_overlapping(line1, line2)
    for cc in overlapping:
        result += get_prio(cc)

print(result)
