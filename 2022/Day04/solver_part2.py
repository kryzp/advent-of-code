
f = open("input.txt")
all_lines = f.readlines()

def get_tasks(dat):
    parts2 = dat.split("-")
    return [*range(int(parts2[0]), int(parts2[1]) + 1)]

def contains(a, b):
    for element in a:
        if element in b:
            return True
    return False

total = 0

for raw in all_lines:
    line = raw.strip()
    parts = line.split(",")
    p1 = get_tasks(parts[0])
    p2 = get_tasks(parts[1])
    if contains(p1, p2) or contains(p2, p1):
        total += 1

print(total)
