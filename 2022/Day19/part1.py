from collections import defaultdict
from collections import deque
import heapq

ll = [x for x in open("input.txt").read().strip().split("\n")]

def parse_bp(line):
	w = line.split(" ")
	return [
		(int(w[6]),  0,          0         ),
		(int(w[12]), 0,          0         ),
		(int(w[18]), int(w[21]), 0         ),
		(int(w[27]), 0,          int(w[30]))
	]

def is_even_possible(st, cur_geo_max):
    return (((24 - st[0]) * ((24 - st[0]) - 1)) // 2 + st[2][3] * (24 - st[0]) + st[1][3]) > cur_geo_max

def neighbours(st, bp):
	res = st[1]
	rb = st[2]
	st_build_ore_rb  = ((res[0] + rb[0] - bp[0][0], res[1] + rb[1]           , res[2] + rb[2]           , res[3] + rb[3]), (rb[0] + 1, rb[1]    , rb[2]    , rb[3]    ))
	st_build_clay_rb = ((res[0] + rb[0] - bp[1][0], res[1] + rb[1]           , res[2] + rb[2]           , res[3] + rb[3]), (rb[0]    , rb[1] + 1, rb[2]    , rb[3]    ))
	st_build_obs_rb  = ((res[0] + rb[0] - bp[2][0], res[1] + rb[1] - bp[2][1], res[2] + rb[2]           , res[3] + rb[3]), (rb[0]    , rb[1]    , rb[2] + 1, rb[3]    ))
	st_build_geo_rb  = ((res[0] + rb[0] - bp[3][0], res[1] + rb[1]           , res[2] + rb[2] - bp[3][2], res[3] + rb[3]), (rb[0]    , rb[1]    , rb[2]    , rb[3] + 1))
	all_n            = ((res[0] + rb[0]           , res[1] + rb[1]           , res[2] + rb[2]           , res[3] + rb[3]), (rb[0]    , rb[1]    , rb[2]    , rb[3]    ))
	if res[0] >= bp[0][0]:
		yield st_build_ore_rb
	if res[0] >= bp[1][0]:
		yield st_build_clay_rb
	if res[0] >= bp[2][0] and res[1] >= bp[2][1]:
		yield st_build_obs_rb
	if res[0] >= bp[3][0] and res[2] >= bp[3][2]:
		yield st_build_geo_rb
	yield all_n

def bfs(start_state, blueprint):
	queue = [start_state]
	visited = { (queue[0][1], queue[0][2]): 0 }
	max_geodes = -1
	while len(queue) != 0:
		state = heapq.heappop(queue)
		t = state[0]
		max_geodes = max(max_geodes, state[1][3])
		if t >= 24:
			continue
		if visited[(state[1], state[2])] != t:
			continue
		if not is_even_possible(state, max_geodes):
			continue
		for next_state in neighbours(state, blueprint):
			if next_state not in visited or t + 1 < visited[next_state]:
				heapq.heappush(queue, (t + 1, next_state[0], next_state[1]))
				visited[next_state] = t + 1
	return max_geodes

blueprints = [parse_bp(l) for l in ll]
start_st = (0, (0, 0, 0, 0), (1, 0, 0, 0))

quality = 0

print("0%")

for i in range(len(blueprints)):
	bp = blueprints[i]
	largest_num_geodes = bfs(start_st, bp)
	quality += (i + 1) * largest_num_geodes
	print(str(int((i + 1) / len(blueprints) * 100)) + '%' + " : " + str((i + 1) * largest_num_geodes))

print()
print("====")
print()

print("Final answer: " + str(quality))
