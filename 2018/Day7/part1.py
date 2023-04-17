from collections import defaultdict

ll = [(x.split(" ")[1], x.split(" ")[7]) for x in open("input.txt").read().strip().split("\n")]

connects_to = defaultdict(lambda: set())
comes_from = defaultdict(lambda: set())

for l in ll:
	comes_from[l[1]].add(l[0])
	connects_to[l[0]].add(l[1])

result = []
searching = list(set(n[0] for n in ll if len(comes_from[n[0]]) == 0))
cur_node = None

while len(searching) != 0:
	searching = sorted(searching)
	nn = searching.pop(0)
	cur_node = (nn, connects_to[nn])
	result.append(cur_node[0])
	for t in sorted(cur_node[1]):
		comes_from[t].remove(cur_node[0])
		if len(comes_from[t]) == 0:
			searching.append(t)

print("".join(result))
