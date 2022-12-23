
ll = [x for x in open("input.txt").read().strip().split("\n")]

finished = set()
monkeys = {}
monkey_values = {}

equation = ""

def apply(name):
	global monkeys
	operation = monkeys[name]
	split = operation.split(" ")
	if name == "humn":
		return "(-1j)"
	if len(split) == 1:
		return "(" + split[0] + ")"
	lhs, operator, rhs = split
	lhsval = apply(lhs)
	rhsval = apply(rhs)
	if name == "root":
		return lhsval + "-" + rhsval
	if operator == '+':
		return "(" + lhsval + "+" + rhsval + ")"
	elif operator == '-':
		return "(" + lhsval + "-" + rhsval + ")"
	elif operator == '*':
		return "(" + lhsval + "*" + rhsval + ")"
	elif operator == '/':
		return "(" + lhsval + "/" + rhsval + ")"

for l in ll:
	split = l.split(": ")
	name = split[0]
	op = split[1]
	monkeys.update({name: op})

equation = apply("root")
print(equation)

evaled = eval(equation)
print(evaled)
result = evaled.real / evaled.imag

print("root value = " + str(result))
