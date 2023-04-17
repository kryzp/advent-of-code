from collections import defaultdict

ll = [(x.split(" ")[1], x.split(" ")[7]) for x in open("input.txt").read().strip().split("\n")]

children_of = defaultdict(lambda: set())
parents_of = defaultdict(lambda: set())

def char_t(c):
	aup = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	return aup.index(c) + 1 + 60

for l in ll:
	parents_of[l[1]].add(l[0])
	children_of[l[0]].add(l[1])

result = 0
queue = list(set((n[0], char_t(n[0])) for n in ll if len(parents_of[n[0]]) == 0))
visited = set()
workers = 5

while queue:
	for j in range(len(queue)):
		if j >= workers:
			break
		queue[j] = (queue[j][0], queue[j][1] - 1)
	for x, t in queue:
		if t == 0:
			visited.add(x)
			for child in sorted(children_of[x]):
				if all(parent in visited for parent in parents_of[child]):
					queue.append((child, char_t(child)))
	removals = set()
	for i in range(len(queue)):
		x, t = queue[i]
		if t <= 0:
			removals.add(i)
	for r in removals:
		queue.pop(r)
	result += 1

print(result)
