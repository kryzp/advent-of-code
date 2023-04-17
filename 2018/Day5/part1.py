
alo = "abcdefghijklmnopqrstuvwxyz"
aup = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

data = open("input.txt").read().strip()

data1 = data
data2 = ""
while data2 != data1:
	data2 = data1
	for c1, c2 in zip(alo, aup):
		data1 = data1.replace(c1 + c2, "")
		data1 = data1.replace(c2 + c1, "")

print(len(data2))
