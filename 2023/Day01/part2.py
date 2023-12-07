
ll = [x for x in open("input.txt").read().strip().split("\n")]

digs = [
	("one", 1),
	("two", 2),
	("three", 3),
	("four", 4),
	("five", 5),
	("six", 6),
	("seven", 7),
	("eight", 8),
	("nine", 9),
	("zero", 0)
]

n = 0

for l in ll:
	V1 = ""
	for i in range(len(l)):
		strstr = l[i:]
		for k, v in digs:
			if strstr.startswith(k):
				V1 = str(v)
				break
		if strstr[0].isdigit():
			V1 = strstr[0]
			break
		if V1 != "":
			break
	V2 = ""
	for i in range(len(l)):
		strstr = l[(len(l) - i - 1):]
		for k, v in digs:
			if strstr.startswith(k):
				V2 = str(v)
				break
		if strstr[0].isdigit():
			V2 = strstr[0]
			break
		if V2 != "":
			break
	n += int(V1 + V2)

print(n)
