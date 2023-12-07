
ll = [x for x in open("input.txt").read().strip().split("\n")]

n = 0

for l in ll:
	first_digit = -1
	last_digit = -1
	for i in range(len(l)):
		c = l[i]
		if c.isdigit():
			first_digit = i
			break
	for i in range(len(l)):
		c = l[len(l) - i - 1]
		if c.isdigit():
			last_digit = len(l) - i - 1
			break
	n += int(str(l[first_digit]) + str(l[last_digit]))

print(n)
