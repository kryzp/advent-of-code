import itertools as it

ll = [x for x in open("input.txt").read().strip().split("\n")]

g_register = 1
g_instructions = []
g_cycle = 1

def add_instruction(inst, cycles_to_complete):
    g_instructions.append([inst, cycles_to_complete])

strengths = []

for l in ll:
    if l.startswith("addx"):
        add_instruction(l, 2)
    elif l.startswith("noop"):
        add_instruction(l, 1)

image = [[]]

while len(g_instructions) >= 1:
    signal_strength = g_cycle * g_register
    print(str(g_cycle) + " * " + str(g_register) + " = " + str(signal_strength))
    if g_cycle in [20, 60, 100, 140, 180, 220]:
        strengths.append(signal_strength)
        image.append([])
    g_cycle += 1 # todo: above or below sig str
    g_instructions[0][1] -= 1
    inst = g_instructions[0][0]
    cycl = g_instructions[0][1]
    if cycl == 0:
        if inst.startswith("addx"):
            g_register += int(inst.split(" ")[1])
        elif inst.startswith("noop"):
            pass
        g_instructions.remove(g_instructions[0])

print("sum of strengths = " + str(sum(strengths)))
