
f = open("input.txt")
counter = 0
maximum = 0

for line in f.readlines():
    line2 = line.strip()
    if line2 != "":
        counter += int(line2)
    else:
        maximum = max(counter, maximum)
        counter = 0

print(maximum)
