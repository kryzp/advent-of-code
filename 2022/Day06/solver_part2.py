data = open("input.txt").read().strip()

for n in range(len(data)-14):
	if len(set(data[n:n+14])) == 14:
		print(n+14)
		break
