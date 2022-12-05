
ll = [x for x in open("input.txt").read().split('\n')]
start_of = -1

for l in ll:
    if l.startswith(" 1"):
        start_of = ll.index(l)
        break

count = int(ll[start_of].strip()[-1])
stacks = []

for i in range(count):
    stacks.append([])

for n in range(start_of):
    l2 = ll[n]
    for k in range(count):
        str_index = k * 4
        if len(l2) >= str_index:
            l2t = l2[str_index + 1]
            if l2t != " ":
                stacks[k].insert(0, l2t)

for m in range(len(ll)-start_of-1):
    l = ll[m+start_of+1].strip()
    if l != "":
        split = l.split(" ")
        amount_to_move = int(split[1])
        from_stack = int(split[3])
        to_stack = int(split[5])
        add = []
        for i in range(amount_to_move):
            item = stacks[from_stack-1].pop()
            add.insert(0, item)
        stacks[to_stack-1].extend(add)

for n in range(len(stacks)):
    print(stacks[n][-1], end='')

print()
