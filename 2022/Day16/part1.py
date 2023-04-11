from collections import defaultdict

ll = [x for x in open("input.txt").read().strip().split("\n")]

valves = set()
tunnels = set()
flow_rates = {}

MAX_TIME = 30

def floyd_warsh_algorithm():
	global valves
	global tunnels
	global flow_rates
	dist = defaultdict(lambda: defaultdict(int))
	for u in valves:
		for v in valves:
			dist[u][v] = len(valves) + 1
	for u, v in tunnels:
		dist[u][v] = 1
	for u in valves:
		dist[u][u] = 0
	for k in valves:
		for i in valves:
			for j in valves:
				if dist[i][j] > dist[i][k] + dist[k][j]:
					dist[i][j] = dist[i][k] + dist[k][j]
	return dist

def parse_line(line):
	global valves
	global tunnels
	global flow_rates
	split = [x.strip() for x in line.split(" ")]
	fromv = split[1]
	rate = int(split[4].split("=")[1][:-1])
	tovs = "".join(split[9:]).split(",")
	flow_rates.update({fromv : rate})
	valves.add(fromv)
	for tov in tovs:
		tunnels.add((fromv, tov))

for l in ll:
	parse_line(l)

def calc_flow(valves):
	result = 0
	for v in valves:
		result += flow_rates[v]
	return result

connections = floyd_warsh_algorithm()

def max_score(curr, t, total, open_valves, viable_valves):
	global finish_timer
	global connections
	maximum = total + (calc_flow(open_valves) * (MAX_TIME - t))
	for new in viable_valves:
		if new in open_valves:
			continue
		dt = connections[curr][new] + 1
		if t + dt >= MAX_TIME:
			continue
		new_total = total + (dt * calc_flow(open_valves))
		open_valves.add(new)
		val = max_score(new, t + dt, new_total, open_valves, viable_valves)
		maximum = max(maximum, val)
		open_valves.remove(new)
	return maximum

viable_valves = set(v for v in valves if flow_rates[v] != 0)
print(max_score("AA", 0, 0, set(), viable_valves))
