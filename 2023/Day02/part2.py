
ll = [x for x in open("input.txt").read().strip().split("\n")]

x = 0

# this question took me way too long
# brain not workign :(((
# kept trying to minimize not maximise
# will actually read the question next time lmao

IDXS = {
	"red": 0,
	"blue": 1,
	"green": 2
}

for l in ll:
	ID_DATA = l.split(': ')
	idd = ID_DATA[0]
	data = ID_DATA[1]
	datas = data.split(';')
	minima = [0, 0, 0]
	for i in datas:
		split3 = i.split(',')
		for j in split3:
			n, name = j.strip().split(' ')
			n = int(n)
			minima[IDXS[name]] = max(minima[IDXS[name]], n)
	x += minima[0]*minima[1]*minima[2]

print(x)
