from heapq import heappush, heappop

ll = [[int(i) for i in x] for x in open("input.txt").read().strip().split("\n")]

DIRS = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def is_valid_x(xc):
	return xc >= 0 and xc < len(ll[0])

def is_valid_y(yc):
	return yc >= 0 and yc < len(ll)

def next_states(dist, st):
	px, py, move_counter, curr_dir_idx = st

	curr_dir_x, curr_dir_y = DIRS[curr_dir_idx]

	if move_counter < 2 and is_valid_x(px + curr_dir_x) and is_valid_y(py + curr_dir_y):
		disthere = ll[py + curr_dir_y][px + curr_dir_x]
		yield dist + disthere, (px + curr_dir_x, py + curr_dir_y, move_counter + 1, curr_dir_idx)

	dir1 = DIRS[(curr_dir_idx + 1) % 4]
	dir2 = DIRS[(curr_dir_idx + 3) % 4]

	if is_valid_x(px + dir1[0]) and is_valid_y(py + dir1[1]):
		disthere = ll[py + dir1[1]][px + dir1[0]]
		yield dist + disthere, (px + dir1[0], py + dir1[1], 0, (curr_dir_idx + 1) % 4)

	if is_valid_x(px + dir2[0]) and is_valid_y(py + dir2[1]):
		disthere = ll[py + dir2[1]][px + dir2[0]]
		yield dist + disthere, (px + dir2[0], py + dir2[1], 0, (curr_dir_idx + 3) % 4)

#positions = []

result = 9999999

for start_state in [(0, 0, 0, 2), (0, 0, 0, 3)]:
	nodes = [(0, start_state)]
	discovered = {start_state: None}
	distance = {start_state: 0}

	while nodes:
		dist_st_curr, curr = heappop(nodes)

		if curr[0] >= len(ll[0]) - 1 and curr[1] >= len(ll) - 1:
			result = min(result, dist_st_curr)
	#		path = [curr]
	#		while discovered[curr] is not None:
	#			curr = discovered[curr]
	#			path.append(curr)
	#		for cc in path[::-1]:
	#			positions.append((cc[0], cc[1]))
			break

		for dist_st_next, next_st in next_states(dist_st_curr, curr):
			if next_st not in discovered or distance[next_st] > dist_st_next:
				heappush(nodes, (dist_st_next, next_st))
				discovered[next_st] = curr
				distance[next_st] = dist_st_next

print(result)

#for y in range(len(ll)):
#	for x in range(len(ll[0])):
#		if (x, y) in positions:
#			print('.', end='')
#		else:
#			print(ll[y][x], end='')
#	print()
