from collections import defaultdict

ll = [x for x in open("input.txt").read().strip().split("\n")]

INF = 99999999

def parse_bp(line):
	w = line.split(" ")
	return [
		(int(w[6]),  0,          0),
		(int(w[12]), 0,          0),
		(int(w[18]), int(w[21]), 0),
		(int(w[27]), 0,          int(w[30]))
	]

def a_star(start_state, blueprint):
	def heuristic(st):
		ore, clay, obs, geo = st[1]
		ore_robots, clay_robots, obs_robots, geo_robots = st[2]
		return max(0.1, 5*ore + 0.1*clay + 0.8*obs - geo)
	def neighbours(st, bp):
		t = st[0] + 1
		if t > 24:
			return []
		res = st[1]
		rb = st[2]
		all_n =         [(t, (res[0] + rb[0]           , res[1] + rb[1]           , res[2] + rb[2]           , res[3] + rb[3]), (rb[0]    , rb[1]    , rb[2]    , rb[3]    ))]
		if res[0] >= bp[0][0]:
			all_n.append((t, (res[0] + rb[0] - bp[0][0], res[1] + rb[1]           , res[2] + rb[2]           , res[3] + rb[3]), (rb[0] + 1, rb[1]    , rb[2]    , rb[3]    )))
		if res[0] >= bp[1][0]:
			all_n.append((t, (res[0] + rb[0] - bp[1][0], res[1] + rb[1]           , res[2] + rb[2]           , res[3] + rb[3]), (rb[0]    , rb[1] + 1, rb[2]    , rb[3]    )))
		if res[0] >= bp[2][0] and res[1] >= bp[2][1]:
			all_n.append((t, (res[0] + rb[0] - bp[2][0], res[1] + rb[1] - bp[2][1], res[2] + rb[2]           , res[3] + rb[3]), (rb[0]    , rb[1]    , rb[2] + 1, rb[3]    )))
		if res[0] >= bp[3][0] and res[2] >= bp[3][2]:
			all_n.append((t, (res[0] + rb[0] - bp[3][0], res[1] + rb[1]           , res[2] + rb[2] - bp[3][2], res[3] + rb[3]), (rb[0]    , rb[1]    , rb[2]    , rb[3] + 1)))
		if (1, 4, 2, 2) in [x[2] for x in all_n]:
			print("E")
		return all_n
	discovered = {start_state}
	costs = {start_state: 0}
	while len(discovered) > 0:
		cur = None
		smallest_value = INF
		for st in discovered:
			val = costs[st] + heuristic(st)
			if val < smallest_value:
				smallest_value = val
				cur = st
		if cur[0] == 24:
			print(cur)
			discovered.remove(cur)
			continue
			#return cur[1][3]
		discovered.remove(cur)
		for n in neighbours(cur, blueprint):
			n_score = costs[cur] + (heuristic(n) - heuristic(cur))
			if n not in costs or n_score < costs[n]:
				costs[n] = n_score
				discovered.add(n)
	raise RuntimeError("ffuck")

blueprints = [parse_bp(l) for l in ll]
start_st = (0, (0, 0, 0, 0), (1, 0, 0, 0))

for bp in blueprints:
	print(a_star(start_st, bp))
