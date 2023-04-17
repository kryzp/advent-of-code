
# r e c u r s i o n
# m u y
# b u e n o
# : )

ll = open("input.txt").read().split(" ")

total = 0

def search(i, data):
	global total
	nch = int(data[i + 0])
	nen = int(data[i + 1])
	j = i + 2
	for k in range(nch):
		j = search(j, data)
	if nen != 0:
		total += sum(int(x) for x in data[j:(j+nen)])
	return j + nen

search(0, ll)

print(total)
