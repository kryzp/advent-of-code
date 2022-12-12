import math

ll = [x for x in open("input.txt").read().strip().split("\n")]

monkeys = []
inspection_counters = []

def add_monkey(items, operation, test, if_true, if_false, lhsop, rhsop, optype):
    global monkeys
    global inspection_counters
    inspection_counters.append(0)
    monkeys.append([items, operation, test, if_true, if_false, lhsop, rhsop, optype])

for i in range(0, len(ll), 7):
    items = []
    operation = None
    test = None
    if_true = 0
    if_false = 0
    lhsop = 0
    rhsop = 0
    optype = ' '
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
                optype = operator
                if lhs == "old" and rhs == "old":
                    operation = lambda x, monkey: x + x
                elif lhs == "old":
                    rhsop = rhs
                    operation = lambda x, monkey: x + int(monkey[6])
                elif rhs == "old":
                    lhsop = lhs
                    operation = lambda x, monkey: int(monkey[5]) + x
            elif operator == '*':
                optype = operator
                if lhs == "old" and rhs == "old":
                    operation = lambda x, monkey: x * x
                elif lhs == "old":
                    rhsop = rhs
                    operation = lambda x, monkey: x * int(monkey[6])
                elif rhs == "old":
                    lhsop = lhs
                    operation = lambda x, monkey: int(monkey[5]) * x
        if split[0] == "Test":
            test = int(split[1].split(" ")[-1])
            if_true_case = ll[i + j + 1].split(" ")
            if_false_case = ll[i + j + 2].split(" ")
            if_true = int(if_true_case[-1])
            if_false = int(if_false_case[-1])
    add_monkey(items, operation, test, if_true, if_false, lhsop, rhsop, optype)

for current_round in range(10000):
    for n in range(len(monkeys)):
        m = monkeys[n]
        m_items = m[0]
        m_op = m[1]
        m_test = m[2]
        m_if_true = m[3]
        m_if_false = m[4]
        for i in range(len(m_items)):
            new_item = m_items[i]
            new_item = m_op(new_item, m) % math.lcm(*(m[2] for m in monkeys))
            inspection_counters[n] += 1
            if new_item % m_test == 0:
                monkeys[m_if_true][0].append(new_item)
            else:
                monkeys[m_if_false][0].append(new_item)
        m[0].clear()

sorted_inspections = sorted([(i, inspection_counters[i]) for i in range(len(inspection_counters))], key=lambda x: x[1])
monkey_business = sorted_inspections[-1][1] * sorted_inspections[-2][1]
print("monkey business 1 = " + str(sorted_inspections[-1][1]))
print("monkey business 2 = " + str(sorted_inspections[-2][1]))
print("monkey business = " + str(monkey_business))
