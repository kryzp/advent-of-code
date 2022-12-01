
f = open("input.txt")
counter = 0
maxima = [0, 0, 0]

def add_to_minimum_in_list(n, m):
    idx = 0
    for i in range(1, len(m)):
        if m[i] < m[idx]:
            idx = i
    m[idx] = max(m[idx], n)

for line in f.readlines():
    line2 = line.strip()
    if line2 != "":
        counter += int(line2)
    else:
        add_to_minimum_in_list(counter, maxima)
        counter = 0

add_to_minimum_in_list(counter, maxima)

total = 0
for i in range(3):
    total += maxima[i]
print(total)
