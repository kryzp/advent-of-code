data = open("input.txt").read().strip()

for n in range(len(data)-4):
	if len(set(data[n:n+4])) == 4:
		print(n+4)
		break
