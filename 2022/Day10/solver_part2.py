import itertools as it

ll = [x for x in open("input.txt").read().strip().split("\n")]

g_register = 1
g_instructions = []
g_cycle = 0

def add_instruction(inst, cycles_to_complete):
    g_instructions.append([inst, cycles_to_complete])

for l in ll:
    if l.startswith("addx"):
        add_instruction(l, 2)
    elif l.startswith("noop"):
        add_instruction(l, 1)

image = []
for i in range(6):
    ll = []
    for j in range(40):
        ll.append(" ")
    image.append(ll)

row = 0
offset = 0

while len(g_instructions) >= 1:
    g_cycle += 1
    if g_cycle in [40, 80, 120, 160, 200, 240]:
        row += 1
        offset = g_cycle
        if row >= 6:
            break
    for i in [-1, 0, 1]:
        curr = g_register + i
        if curr == g_cycle - offset - 1:
            image[row][curr] = "#"
    g_instructions[0][1] -= 1
    inst = g_instructions[0][0]
    cycl = g_instructions[0][1]
    if cycl == 0:
        if inst.startswith("addx"):
            g_register += int(inst.split(" ")[1])
        g_instructions.remove(g_instructions[0])

for line in image:
    for c in line:
        print(c, end='')
    print()
