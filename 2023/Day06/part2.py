import itertools

ll = [x for x in open("input.txt").read().strip().split("\n")]

times = [int(x) for x in ll[0].split(" ")[1:] if x != '']
distances = [int(x) for x in ll[1].split(" ")[1:] if x != '']

def n_beat_record(time, dist):
	n = 0
	last = False
	for possible_time in range(time + 1):
		held_down = time - possible_time
		distance_travelled = possible_time * held_down
		if distance_travelled > dist:
			n += 1
			last = True
		elif last:
			break
	return n

time = int("".join([x.strip() for x in ll[0].split(" ")[1:]]))
dist = int("".join([x.strip() for x in ll[1].split(" ")[1:]]))
x = n_beat_record(time, dist)

print(x)
