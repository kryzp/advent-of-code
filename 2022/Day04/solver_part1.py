
def contains(a1, a2, b1, b2):
    return ((a1 >= b1) and (a2 <= b2)) or ((a1 <= b1) and (a2 >= b2))

total = 0
ll = [x for x in open("input.txt").read().strip().split('\n')]

for l in ll:
    t1, t2 = l .split(",")
    a1, a2 = t1.split("-")
    b1, b2 = t2.split("-")
    a1 = int(a1)
    a2 = int(a2)
    b1 = int(b1)
    b2 = int(b2)
    if contains(a1, a2, b1, b2):
        total += 1

print(total)
