
ll = [x for x in open("input.txt").read().strip().split("\n")]

SIZE = 4_000_000
LARGE = 9999999

def sensor_covered_point_range(spos, bpos, line):
	sx, sy = spos
	bx, by = bpos
	dx = sx - bx
	dy = sy - by
	mhd = abs(dx) + abs(dy)
	yd = abs(line - sy)
	xd = mhd - yd
	if xd < 0:
		return LARGE, -LARGE
	else:
		return sx - xd, sx + xd

def is_point_scanned(px, py, sensor_beacons):
	for s, b in sensor_beacons:
		sx, sy = s
		bx, by = b
		mhd_maximum = abs(sx - bx) + abs(sy - by)
		mhd_point = abs(sx - px) + abs(sy - py)
		if mhd_maximum >= mhd_point:
			return True
	return False

def get_sensor_and_beacon_pair(l):
	comp = [x.strip() for x in l.split(" ")]
	s = (
		int(comp[2].split("=")[1][:-1]),
		int(comp[3].split("=")[1][:-1])
	)
	b = (
		int(comp[8].split("=")[1][:-1]),
		int(comp[9].split("=")[1])
	)
	return s, b

sensor_beacons = [get_sensor_and_beacon_pair(l) for l in ll]
possible_positions = set()

for y in range(SIZE):
	print("%.2f%%" % (y / SIZE * 100))
	for s1, b1 in sensor_beacons:
		for s2, b2 in sensor_beacons:
			if s1 == s2:
				continue
			mn1, mx1 = sensor_covered_point_range(s1, b1, y)
			mn2, mx2 = sensor_covered_point_range(s2, b2, y)
			if mn2 - mx1 == 2:
				possible_positions.add((mx1 + 1, y))
				break

for px, py in possible_positions:
	if not is_point_scanned(px, py, sensor_beacons) and is_point_scanned(px, py - 1, sensor_beacons) and is_point_scanned(px, py + 1, sensor_beacons):
		tuning_frequency = (px * 4_000_000) + py
		print("final scanner =", px, py)
		print("tuning frequency =", tuning_frequency)
		break
