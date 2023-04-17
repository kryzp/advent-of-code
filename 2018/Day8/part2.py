
# r e c u r s i o n
# m u y
# b u e n o
# : )

ll = open("input.txt").read().split(" ")

def search(i, data):
	value = 0
	nch = int(data[i + 0])
	nen = int(data[i + 1])
	j = i + 2
	children = []
	for k in range(nch):
		j, vv = search(j, data)
		children.append(vv)
	if nen != 0:
		if nch == 0:	
			value = sum(int(x) for x in data[j:(j+nen)])
		else:
			for index in data[j:(j+nen)]:
				idx = int(index) - 1
				if idx >= 0 and idx < len(children):
					value += children[idx]
	return j + nen, value

total = search(0, ll)[1]

print(total)
