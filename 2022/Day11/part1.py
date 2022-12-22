
ll = [x for x in open("input.txt").read().strip().split("\n")]

monkeys = []
inspection_counters = []

def add_monkey(items, operation, test, if_true, if_false, lhsop, rhsop):
    global monkeys
    global inspection_counters
    inspection_counters.append(0)
    monkeys.append([items, operation, test, if_true, if_false, lhsop, rhsop])

for i in range(0, len(ll), 7):
    items = []
    operation = None
    test = None
    if_true = 0
    if_false = 0
    lhsop = 0
    rhsop = 0
    for j in range(1, 4):
        l = ll[i + j]
        split = l.strip().split(":")
        if split[0] == "Starting items":
            split2 = split[1].split(",")
            items = [int(x.strip()) for x in split2]
        if split[0] == "Operation":
            operation_string = split[1].strip()
            splitGG = operation_string.split(" ")
            lhs = splitGG[2]
            rhs = splitGG[4]
            operator = splitGG[3]
            if operator == '+':
                if lhs == "old" and rhs == "old":
                    operation = lambda x, idx: x + x
                elif lhs == "old":
                    rhsop = rhs
                    operation = lambda x, idx: x + int(monkeys[idx][6])
                elif rhs == "old":
                    lhsop = lhs
                    operation = lambda x, idx: int(monkeys[idx][5]) + x
            elif operator == '*':
                if lhs == "old" and rhs == "old":
                    operation = lambda x, idx: x * x
                elif lhs == "old":
                    rhsop = rhs
                    operation = lambda x, idx: x * int(monkeys[idx][6])
                elif rhs == "old":
                    lhsop = lhs
                    operation = lambda x, idx: int(monkeys[idx][5]) * x
        if split[0] == "Test":
            test = int(split[1].split(" ")[-1])
            if_true_case = ll[i + j + 1].split(" ")
            if_false_case = ll[i + j + 2].split(" ")
            if_true = int(if_true_case[-1])
            if_false = int(if_false_case[-1])
    add_monkey(items, operation, test, if_true, if_false, lhsop, rhsop)

for current_round in range(20):
    for n in range(len(monkeys)):
        m = monkeys[n]
        m_items = m[0]
        m_op = m[1]
        m_test = m[2]
        m_if_true = m[3]
        m_if_false = m[4]
        for i in range(len(m_items)):
            item = m_items[i]
            new_item = m_op(item, n)
            new_item = new_item // 3
            inspection_counters[n] += 1
            if new_item % m_test == 0:
                monkeys[m_if_true][0].append(new_item)
            else:
                monkeys[m_if_false][0].append(new_item)
        m[0].clear()

inspections_with_idx = [(i, inspection_counters[i]) for i in range(len(inspection_counters))]
sorted_inspections = sorted(inspections_with_idx, key=lambda x: x[1])

print("monkey business = " + str(sorted_inspections[-1][1] * sorted_inspections[-2][1]))
