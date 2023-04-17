
alo = "abcdefghijklmnopqrstuvwxyz"
aup = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

data = open("input.txt").read().strip()

mn = 9999

for c in alo:
	data1 = data
	data1 = data1.replace(c.lower(), '')
	data1 = data1.replace(c.upper(), '')
	data2 = ""
	while data2 != data1:
		data2 = data1
		for c1, c2 in zip(alo, aup):
			data1 = data1.replace(c1 + c2, "")
			data1 = data1.replace(c2 + c1, "")
	mn = min(mn, len(data2))

print(mn)
