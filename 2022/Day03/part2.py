
def get_overlapping(l1, l2, l3):
    result = []
    for c1 in l1:
        for c2 in l2:
            for c3 in l3:
                if c1 == c2 and c1 == c3 and (c1 not in result):
                    result.append(c1)
    return result

def get_prio(c):
    if c.isupper():
        return ord(c) - ord('A') + 27
    elif c.islower():
        return ord(c) - ord('a') + 1

f = open("input.txt")
result = 0
all_lines = f.readlines()

for n in range(len(all_lines) // 3):
    l1 = all_lines[n*3 + 0].strip()
    l2 = all_lines[n*3 + 1].strip()
    l3 = all_lines[n*3 + 2].strip()

    n = len(l1) // 2

    overlapping = get_overlapping(l1, l2, l3)
    for cc in overlapping:
        result += get_prio(cc)

print(result)
