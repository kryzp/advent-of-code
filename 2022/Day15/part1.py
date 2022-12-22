
ll = [x for x in open("input.txt").read().strip().split("\n")]

ROW_Y = 2_000_000

beacon_positions = set()
scanned = set()

def points_covered_by_sensor_on_line(spos, bpos):
	sx, sy = spos
	bx, by = bpos
	dx = sx - bx
	dy = sy - by
	mhd = abs(dx) + abs(dy)
	yd = abs(ROW_Y - sy)
	xd = mhd - yd
	if xd < 0:
		return set()
	else:
		points = range(sx - xd, sx + xd + 1)
		return set(points)

for l in ll:
	splitted = l.split(" ")
	sensor_pos = (
		int(splitted[2].split("=")[1][:-1]),
		int(splitted[3].strip().split("=")[1][:-1])
	)
	beacon_pos = (
		int(splitted[8].strip().split("=")[1][:-1]),
		int(splitted[9].strip().split("=")[1])
	)
	scanned |= points_covered_by_sensor_on_line(sensor_pos, beacon_pos)
	beacon_positions.add(beacon_pos)

beacons = set([b[0] for b in beacon_positions if b[1] == ROW_Y])
print(len(scanned - beacons))
