
ll = list(enumerate(int(x) for x in open("input.txt").read().strip().split("\n")))
SIZE = len(ll)

for i in range(SIZE):
	for j in range(SIZE):
		pair = ll[j]
		index, number = pair
		if index == i:
			ll.pop(j)
			idx = (j + number) % (SIZE - 1)
			ll.insert(idx, pair)

zero_idx = 0
for i in range(SIZE):
	if ll[i][1] == 0:
		zero_idx = i
		break

result = sum(ll[(x + zero_idx) % len(ll)][1] for x in [1000, 2000, 3000])
print("sum = " + str(result))
