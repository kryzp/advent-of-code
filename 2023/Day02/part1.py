
ll = [x for x in open("input.txt").read().strip().split("\n")]

x = 0

for l in ll:
	ID_DATA = l.split(': ')
	idd = ID_DATA[0]
	data = ID_DATA[1]
	datas = data.split(';')
	valid = True
	for i in datas:
		split3 = i.split(',')
		for j in split3:
			n, name = j.strip().split(' ')
			n = int(n)
			if (n > 12 and name == "red") or (n > 13 and name == "green") or (n > 14 and name == "blue"):
				valid = False
				break
		if not valid:
			break
	if valid:
		x += int(idd.split(' ')[1])

print(x)
