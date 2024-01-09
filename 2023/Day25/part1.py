import networkx
import random

ll = [x for x in open("input.txt").read().strip().split("\n")]

graph = networkx.Graph()
components = set()

for l in ll:
	spl = l.split(": ")
	name = spl[0]
	conn = spl[1].split(" ")
	for c in conn:
		graph.add_edge(name, c, capacity=1.0)
	components.add(name)

l1 = 0
l2 = 0

while True:
	c1 = random.choice(list(components))
	c2 = c1
	while c2 == c1:
		c2 = random.choice(list(components))
	n, subgraphs = networkx.minimum_cut(graph, c1, c2)
	if n == 3:
		l1 = len(subgraphs[0])
		l2 = len(subgraphs[1])
		break

print(l1 * l2)
